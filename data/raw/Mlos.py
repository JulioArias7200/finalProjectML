import os
import sys
import time
import subprocess
import numpy as np
import pandas as pd

# Intentar cargar serializadores
try:
    import joblib
    HAS_JOBLIB = True
except ImportError:
    HAS_JOBLIB = False

try:
    import skops.io as sio
    HAS_SKOPS = True
except ImportError:
    HAS_SKOPS = False

import pickle
import sklearn
import sklearn.ensemble
import sklearn.tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Parches para retrocompatibilidad
sys.modules['sklearn.ensemble.forest'] = sklearn.ensemble
sys.modules['sklearn.tree.tree'] = sklearn.tree

import gradio as gr
import mlflow
import mlflow.sklearn

# ==========================================
# 1. FUNCIÓN DE ENTRENAMIENTO Y REGISTRO
# ==========================================
MODEL_PATH = "ingresos_model.pkl"

def train_log_and_save_model():
    print("⚡ Cargando datasets y entrenando modelo de Regresión con registro en MLflow...")
    
    # Rutas locales basadas en la carpeta actual 'raw'
    ruta_general = "MOD_ANUAL_S01-07_12_general_i.csv"
    ruta_materiales = "MOD_ANUAL_S10_materiales_i.csv"
    
    try:
        # Cargar los datos reales
        df_general = pd.read_csv(ruta_general)
        df_materiales = pd.read_csv(ruta_materiales)
        
        # ⚠️ IMPORTANTE: Aquí debes poner el nombre de la columna que une ambos CSV (ej. 'ID', 'NRO_ENCUESTA')
        columna_id = 'ID' 
        
        # Unir los datasets si comparten un ID
        if columna_id in df_general.columns and columna_id in df_materiales.columns:
            df = pd.merge(df_general, df_materiales, on=columna_id, how='inner')
        else:
            print(f"⚠️ No se encontró la columna '{columna_id}'. Usando solo datos generales por ahora.")
            df = df_general

        # ⚠️ IMPORTANTE: Reemplaza estos nombres por los códigos REALES del diccionario del INE
        # Por ejemplo: 'S05_04' para ingresos, 'S02_09' para sueldos, etc.
        columna_target = 'ingresos_operativos' # Cambiar por el real
        columnas_features = ['personal_ocupado', 'sueldos_salarios', 'gasto_energia', 'activos_fijos', 'inventarios', 'almacenamiento']
        
        # Verificar si las columnas existen, de lo contrario lanzar un error controlado
        if columna_target not in df.columns or not all(c in df.columns for c in columnas_features):
            raise ValueError("Las columnas especificadas no coinciden con los nombres reales en el CSV del INE.")

        X = df[columnas_features].fillna(0) # Manejo básico de nulos
        y = df[columna_target].fillna(0)

    except Exception as e:
        print(f"⚠️ Error al procesar los CSV reales ({e}). Generando datos simulados estructurados como la EAIM para probar la aplicación...")
        # Generación de datos simulados temporales para evitar que la app colapse si las columnas no coinciden aún
        np.random.seed(42)
        n_samples = 500
        X = pd.DataFrame({
            'personal_ocupado': np.random.randint(10, 500, n_samples),
            'sueldos_salarios': np.random.uniform(50000, 2000000, n_samples),
            'gasto_energia': np.random.uniform(10000, 500000, n_samples),
            'activos_fijos': np.random.uniform(100000, 10000000, n_samples),
            'inventarios': np.random.uniform(20000, 3000000, n_samples),
            'almacenamiento': np.random.randint(100, 5000, n_samples)
        })
        # Variable objetivo simulada
        y = (X['personal_ocupado'] * 15000) + (X['activos_fijos'] * 0.2) + np.random.normal(0, 50000, n_samples)
        columnas_features = X.columns.tolist()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Hiperparámetros
    n_estimators = 100
    max_depth = 8
    random_state = 42
    
    # ✅ SOLUCIÓN AL ERROR DE MLFLOW Y WINDOWS: Usar base de datos SQLite local
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("Prediccion_Ingresos_Bolivia")
    
    with mlflow.start_run(run_name="RandomForestRegressor_v1") as run:
        # Entrenamiento
        new_model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
        new_model.fit(X_train, y_train)
        
        # Evaluación
        y_pred = new_model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        
        # Registro en MLflow
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("features", columnas_features)
        
        mlflow.log_metric("MAE", mae)
        mlflow.log_metric("RMSE", rmse)
        mlflow.log_metric("R2_score", r2)
        
        mlflow.sklearn.log_model(
            new_model, 
            artifact_path="model",
            skops_trusted_types=["sklearn.tree._tree.Tree"]
        )       
        print(f"✅ Experimento guardado en MLflow (Run ID: {run.info.run_id})")
        print(f"📊 R² Score obtenido: {r2:.4f}")
    
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(new_model, f)
        
    return new_model

# ==========================================
# 2. CARGA DEL MODELO
# ==========================================
model = None
if os.path.exists(MODEL_PATH):
    print(f"🔍 Intentando cargar modelo local existente ({MODEL_PATH})...")
    if HAS_JOBLIB and model is None:
        try:
            model = joblib.load(MODEL_PATH)
            print("✅ Carga limpia con joblib.")
        except Exception: pass
    if model is None:
        try:
            with open(MODEL_PATH, "rb") as f:
                model = pickle.load(f)
            print("✅ Carga limpia con pickle.")
        except Exception:
            print("⚠️ El modelo local falló. Se volverá a entrenar...")

if model is None:
    model = train_log_and_save_model()

# ==========================================
# 3. LANZAR SERVIDOR MLFLOW UI
# ==========================================
try:
    subprocess.run(["pkill", "-f", "mlflow"], check=False)
except Exception: pass

try:
    # ✅ SOLUCIÓN AL ERROR DE MLFLOW EN EL UI: Usar la misma URI de SQLite
    subprocess.Popen(
        ["mlflow", "ui", "--backend-store-uri", "sqlite:///mlflow.db", "--port", "5002", "--host", "0.0.0.0"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(2)
    print("📊 Servidor MLflow UI corriendo en: http://localhost:5002")
except Exception as e:
    print(f"⚠️ No se pudo levantar la interfaz de MLflow automáticamente: {e}")

# ==========================================
# 4. FUNCIÓN DE PREDICCIÓN (GRADIO)
# ==========================================
def predict_ingresos(personal, sueldos, energia, activos, inventarios, almacen):
    features = np.array([[personal, sueldos, energia, activos, inventarios, almacen]])
    prediccion = model.predict(features)[0]
    return f"Bs. {prediccion:,.2f}"

# ==========================================
# 5. INTERFAZ INTERACTIVA GRADIO
# ==========================================
with gr.Blocks(title="Predicción de Ingresos Operativos", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🏢 Proyección de Ingresos Operativos (EAIM)")
    gr.Markdown("Modelo de *Regresión* registrado en **MLflow**.")

    with gr.Row():
        with gr.Column():
            in_personal = gr.Number(value=50, label="Personal Ocupado (Cant.)")
            in_sueldos = gr.Number(value=150000, label="Sueldos y Salarios Anuales (Bs.)")
            in_energia = gr.Number(value=35000, label="Gasto en Energía y Combustible (Bs.)")
        with gr.Column():
            in_activos = gr.Number(value=500000, label="Valor de Activos Fijos (Bs.)")
            in_inventarios = gr.Number(value=120000, label="Valor de Inventarios (Bs.)")
            in_almacen = gr.Number(value=500, label="Capacidad de Almacenamiento")

    predict_btn = gr.Button("📊 Estimar Ingresos Operativos", variant="primary", size="lg")
    result = gr.Textbox(label="Ingresos Operativos Proyectados", lines=2, text_align="center")

    predict_btn.click(
        fn=predict_ingresos,
        inputs=[in_personal, in_sueldos, in_energia, in_activos, in_inventarios, in_almacen],
        outputs=result
    )

    gr.Markdown("---")
    gr.Markdown("### 📈 Panel MLflow de Métricas: [http://localhost:5002](http://localhost:5002)")

# ==========================================
# 6. EJECUCIÓN
# ==========================================
print("🚀 MLOps y Gradio listos para usar!")
demo.launch(share=True, show_error=True)