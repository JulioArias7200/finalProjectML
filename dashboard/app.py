from flask import Flask, render_template, jsonify, request
import os
import pandas as pd

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EDSA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

SOURCES = [
    ("Mujer", "EDSA2023_Mujer.csv", "Mujer + Hogar + Vivienda + Peso/talla/hemo", "M1"),
    ("Hogar", "EDSA2023_Hogar.csv", "Mujer + Hogar + Vivienda + Peso/talla/hemo", "M1"),
    ("Vivienda", "EDSA2023_Vivienda.csv", "Mujer + Hogar + Vivienda + Peso/talla/hemo", "M1"),
    ("Peso, talla y hemo", "EDSA2023_Peso_talla_hemo.csv", "Mujer + Hogar + Vivienda + Peso/talla/hemo", "M1"),
    ("Historial de paridad", "EDSA2023_HistorialParidad.csv", "HistorialParidad + Mujer", "M10"),
]

MODELS = {
    "M1": {"title": "Anemia en mujeres", "target": "anemia_mujer", "task": "Clasificación binaria", "baseline": "Regresión logística", "alternatives": "Random Forest · Gradient Boosting"},
    "M10": {"title": "Controles prenatales", "target": "controles_prenatales", "task": "Regresión de conteo", "baseline": "Regresión lineal", "alternatives": "Polinomial grado 2 · Random Forest · Gradient Boosting"},
}

def _source_profile():
    profile = []
    for label, filename, join, model in SOURCES:
        path = os.path.join(EDSA_DIR, filename)
        rows = columns = None
        if os.path.exists(path):
            try:
                sample = pd.read_csv(path, nrows=0)
                rows = int(sum(1 for _ in open(path, encoding="utf-8", errors="ignore")) - 1)
                columns = len(sample.columns)
            except (OSError, pd.errors.ParserError):
                pass
        profile.append({"name": label, "file": filename, "rows": rows, "columns": columns, "join": join, "model": model})
    return profile

@app.route('/')
def index():
    return render_template('index.html', active_page='index', models=MODELS)

@app.route('/boosting')
def boosting():
    return render_template('preprocessing.html', active_page='preprocessing')

@app.route('/bagging')
def bagging():
    return render_template('quality.html', active_page='quality', sources=_source_profile())

@app.route('/comparative')
def comparative():
    return render_template('comparative.html', active_page='comparative', models=MODELS)

# --------- API ---------
@app.route('/api/summary')
def api_summary():
    return jsonify({"project": "EDSA 2023", "sources": _source_profile(), "models": MODELS, "status": "perfilado"})

@app.route('/api/train/classification', methods=['GET','POST'])
def api_train_classification():
    return jsonify(_experiment("M1"))

@app.route('/api/train/regression', methods=['GET','POST'])
def api_train_regression():
    return jsonify(_experiment("M10"))

@app.route('/api/train/compare', methods=['GET','POST'])
def api_train_compare():
    return jsonify({"M1": _experiment("M1"), "M10": _experiment("M10")})

def _experiment(model_key):
    model = MODELS[model_key]
    return {"model": model_key, "target": model["target"], "status": "pendiente de ejecución sobre tabla analítica", "baseline": model["baseline"], "alternative": model["alternatives"], "test_policy": "test congelado"}

@app.route('/demo')
def demo():
    return render_template('m1.html', active_page='m1', model=MODELS['M1'])

@app.route('/m10')
def m10():
    return render_template('m10.html', active_page='m10', model=MODELS['M10'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
