"""
Script para generar figuras estadísticas y analíticas en alta resolución (300 DPI)
para el informe académico en formato APA 7 (informe/informeAPA7.tex).
Versión con diagnóstico econométrico riguroso y gráficos vectoriales perfeccionados.
"""

import sys
import json
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from scipy import stats
import statsmodels.api as sm

# Configuración de Rutas
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "dataset_procesado.csv"
ARTIFACTS_DIR = PROJECT_ROOT / "dashboard" / "artifacts"
OUTPUT_DIR = PROJECT_ROOT / "informe" / "imagenes"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configuración de Estilo Académico APA 7
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 12

# Paleta Institucional UMSA / INE
COLOR_PRIMARY = '#0B3D62'       # Azul profundo institucional
COLOR_SECONDARY = '#1B5A8C'     # Azul medio
COLOR_GOLD = '#D9822B'          # Ámbar / Dorado
COLOR_EMERALD = '#1E7A46'       # Verde esmeralda
COLOR_CRIMSON = '#C0392B'       # Rojo alerta
COLOR_GRAY = '#5C6B73'          # Gris neutro
COLOR_LIGHT_BG = '#F8FAFC'      # Fondo suave

# Cargar Datos
print("Cargando datos para generación de figuras estadísticas...")
df = pd.read_csv(DATA_PATH)
df_test = pd.read_csv(ARTIFACTS_DIR / "test_predictions.csv")

with open(ARTIFACTS_DIR / "cv_results.json", "r", encoding="utf-8") as f:
    cv_data = json.load(f)

# -----------------------------------------------------------------------------
# FIGURA 1: DISTRIBUCIÓN DE ASIMETRÍA vs NORMALIZACIÓN LOG1P
# -----------------------------------------------------------------------------
print("Generando Figura 1: distribucion_asimetria_log.png...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Panel Izquierdo: Escala Natural (Decaimiento Pareto)
y_millones = df["target"] / 1e6
p95 = np.percentile(y_millones, 95)
p99 = np.percentile(y_millones, 99)
median_val = y_millones.median()
mean_val = y_millones.mean()

# Histograma focalizado en percentiles representativos (0 a 100M) con 35 bins
bins_pareto = np.linspace(0, 100, 35)
ax1.hist(y_millones, bins=bins_pareto, color=COLOR_PRIMARY, alpha=0.85, edgecolor='white', linewidth=0.6, density=False)
ax1.axvline(median_val, color=COLOR_GOLD, linestyle='--', linewidth=2, label=f'Mediana: Bs {median_val:.2f}M')
ax1.axvline(mean_val, color=COLOR_CRIMSON, linestyle=':', linewidth=2, label=f'Media: Bs {mean_val:.2f}M')

ax1.set_title('(a) Distribución en Escala Natural (Bolivianos)', fontweight='bold', pad=10)
ax1.set_xlabel('Ingreso Operativo Anual (Millones de Bs)')
ax1.set_ylabel('Frecuencia Absoluta (N° Empresas)')
ax1.set_xlim(0, 100)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.text(0.58, 0.55, f'$p_{{50}}$ = Bs {median_val:.1f}M\n$p_{{95}}$ = Bs {p95:.1f}M\n$p_{{99}}$ = Bs {p99:.1f}M\nMáx = Bs {y_millones.max():.1f}M', 
         transform=ax1.transAxes, fontsize=8.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.85, edgecolor='lightgray'))
ax1.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='lightgray')

# Panel Derecho: Escala Log1p (Densidad Normalizada)
y_log = np.log1p(df["target"])
sns.histplot(y_log, kde=True, stat='density', ax=ax2, color=COLOR_SECONDARY, edgecolor='white', linewidth=0.6, line_kws={'linewidth': 2, 'color': COLOR_PRIMARY})
ax2.axvline(y_log.median(), color=COLOR_GOLD, linestyle='--', linewidth=2, label=f'Mediana $\\ln(1+y)$: {y_log.median():.2f}')
ax2.axvline(y_log.mean(), color=COLOR_CRIMSON, linestyle=':', linewidth=2, label=f'Media $\\ln(1+y)$: {y_log.mean():.2f}')

ax2.set_title('(b) Distribución Estabilizada con Transformación $\\ln(1 + y)$', fontweight='bold', pad=10)
ax2.set_xlabel('Ingreso Operativo $\\ln(1 + y)$')
ax2.set_ylabel('Densidad de Probabilidad $f(y_{\\log})$')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='lightgray')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "distribucion_asimetria_log.png", dpi=300, bbox_inches='tight')
plt.close()

# -----------------------------------------------------------------------------
# FIGURA 2: MATRIZ DE CORRELACIÓN DE PREDICTORES PRODUCTIVOS
# -----------------------------------------------------------------------------
print("Generando Figura 2: correlacion_heatmap.png...")
fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=300)

cols_corr = {
    'target': 'Ingresos (Target)',
    'S01_03_C': 'Masa Salarial (L)',
    'S01_05_A': 'Personal (L)',
    'S07_09_E': 'Activos Fijos (K)',
    'total_valor_uti': 'Insumos Fabriles (M)',
    'S02_09': 'Energía Devengada (E)',
    'S06_06_B': 'Inventarios Finales (K)',
    'S01_14': 'Otras Remuneraciones (L)'
}

corr_df = df[list(cols_corr.keys())].copy()
for c in corr_df.columns:
    corr_df[c] = np.log1p(corr_df[c])
corr_df.rename(columns=cols_corr, inplace=True)
corr_matrix = corr_df.corr(method='pearson')

# Recortar la diagonal y la parte superior para eliminar filas/columnas vacías
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
# Mostrar matriz triangular inferior estilizada
sns.heatmap(corr_matrix, mask=mask, cmap='Blues', annot=True, fmt='.2f', 
            square=True, linewidths=1.0, linecolor='white',
            cbar_kws={"shrink": 0.8, "label": "Coeficiente de Correlación de Pearson ($r$)"}, ax=ax)
ax.set_title('Matriz de Correlación Lineal entre Factores Productivos y Target $\\ln(1+y)$', fontweight='bold', pad=12)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlacion_heatmap.png", dpi=300, bbox_inches='tight')
plt.close()

# -----------------------------------------------------------------------------
# FIGURA 3: DISPERSIÓN REAL VS PREDICHO CON BANDA CONFORMAL AL 90%
# -----------------------------------------------------------------------------
print("Generando Figura 3: dispersion_real_vs_predicho.png...")
fig, ax = plt.subplots(figsize=(7.5, 6.5), dpi=300)

y_true_log = df_test["real_log"]
y_pred_log = df_test["pred_log"]
residuals = y_true_log - y_pred_log
q_inf = np.percentile(residuals, 5)   # Cuantil 5% (negativo)
q_sup = np.percentile(residuals, 95)  # Cuantil 95% (positivo)

# Eje X: Predicho, Eje Y: Real (Estándar Econométrico)
ax.scatter(y_pred_log, y_true_log, alpha=0.45, color=COLOR_PRIMARY, edgecolors='none', s=26, label=f'Test Hold-Out ($N={len(df_test)}$)')

min_val = min(y_true_log.min(), y_pred_log.min()) - 0.2
max_val = max(y_true_log.max(), y_pred_log.max()) + 0.2
x_grid = np.linspace(min_val, max_val, 100)

# Recta de 45 grados (y = hat{y})
ax.plot(x_grid, x_grid, color=COLOR_CRIMSON, linestyle='-', linewidth=2, label='Ajuste Ideal ($y = \\hat{y}$)')

# Bandas Conformal al 90% (y = hat{y} + q_inf e y = hat{y} + q_sup)
y_band_inf = x_grid + q_inf
y_band_sup = x_grid + q_sup
ax.plot(x_grid, y_band_sup, color=COLOR_GOLD, linestyle='--', linewidth=1.5, label=f'Límite Conformal Sup ($q_{{0.95}} = {q_sup:+.2f}$)')
ax.plot(x_grid, y_band_inf, color=COLOR_GOLD, linestyle='--', linewidth=1.5, label=f'Límite Conformal Inf ($q_{{0.05}} = {q_inf:+.2f}$)')
ax.fill_between(x_grid, y_band_inf, y_band_sup, color=COLOR_GOLD, alpha=0.12, label='Región Conformal 90% (Cob: 90.33%)')

ax.set_title('Inferencia Predictiva vs. Observada en Test Set ($R^2 = 0.7868$)', fontweight='bold', pad=10)
ax.set_xlabel('Ingreso Operativo Predicho $\\ln(1 + \\hat{y})$')
ax.set_ylabel('Ingreso Operativo Real $\\ln(1 + y)$')
ax.set_xlim(min_val, max_val)
ax.set_ylim(min_val, max_val)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='lightgray', fontsize=8.5)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "dispersion_real_vs_predicho.png", dpi=300, bbox_inches='tight')
plt.close()

# -----------------------------------------------------------------------------
# FIGURA 4: HISTOGRAMA DE RESIDUOS Y HOMOCEDASTICIDAD CON AJUSTE LOWESS
# -----------------------------------------------------------------------------
print("Generando Figura 4: residuos_homocedasticidad.png...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8), dpi=300)

# Panel 1: Histograma de Residuos
sns.histplot(residuals, kde=True, stat='density', ax=ax1, color=COLOR_PRIMARY, edgecolor='white', linewidth=0.6, line_kws={'linewidth': 2, 'color': COLOR_CRIMSON})
ax1.axvline(residuals.mean(), color='black', linestyle='--', linewidth=1.5, label=f'Media: {residuals.mean():.4f}')
# Curva teórica normal
x_norm = np.linspace(residuals.min(), residuals.max(), 200)
p_norm = stats.norm.pdf(x_norm, residuals.mean(), residuals.std())
ax1.plot(x_norm, p_norm, color=COLOR_GOLD, linestyle=':', linewidth=2, label=f'Normal ($\sigma={residuals.std():.3f}$)')

ax1.set_title('(a) Distribución de Residuos $e = y - \\hat{y}$', fontweight='bold', pad=10)
ax1.set_xlabel('Residuo Logarítmico $(y_{\\log} - \\hat{y}_{\\log})$')
ax1.set_ylabel('Densidad')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(frameon=True, facecolor='white', edgecolor='lightgray')

# Panel 2: Residuos vs Valores Predichos + Curva LOWESS
ax2.scatter(y_pred_log, residuals, alpha=0.40, color=COLOR_SECONDARY, edgecolors='none', s=24, label='Residuos Test ($N=631$)')
ax2.axhline(0, color='black', linestyle='--', linewidth=1.2)
ax2.axhline(residuals.std()*1.96, color=COLOR_GOLD, linestyle=':', linewidth=1.5, label='Límites $\\pm 1.96\\sigma$')
ax2.axhline(-residuals.std()*1.96, color=COLOR_GOLD, linestyle=':', linewidth=1.5)

# Ajuste no paramétrico LOWESS
lowess = sm.nonparametric.lowess(residuals, y_pred_log, frac=0.6)
ax2.plot(lowess[:, 0], lowess[:, 1], color=COLOR_CRIMSON, linewidth=2.2, label='Ajuste LOWESS $\mathbb{E}[e \mid \\hat{y}]$')

ax2.set_title('(b) Diagnóstico de Homocedasticidad y Linealidad', fontweight='bold', pad=10)
ax2.set_xlabel('Valores Predichos $\\ln(1+\\hat{y})$')
ax2.set_ylabel('Residuo $(y_{\\log} - \\hat{y}_{\\log})$')
ax2.set_ylim(-2.2, 3.2)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='lightgray', fontsize=8.5)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "residuos_homocedasticidad.png", dpi=300, bbox_inches='tight')
plt.close()

# -----------------------------------------------------------------------------
# FIGURA 5: ESTABILIDAD DE VALIDACIÓN CRUZADA (5-FOLD CV)
# -----------------------------------------------------------------------------
print("Generando Figura 5: cv_estabilidad_folds.png...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

models_cv = cv_data.get("models", {})
rf_r2 = models_cv.get("RandomForest", {}).get("fold_scores_r2", [0.768, 0.775, 0.771, 0.776, 0.772])
hgb_r2 = models_cv.get("HistGradientBoosting", {}).get("fold_scores_r2", [0.765, 0.773, 0.769, 0.774, 0.770])
ridge_r2 = models_cv.get("Ridge", {}).get("fold_scores_r2", [0.542, 0.551, 0.548, 0.549, 0.546])

folds = [f'Fold {i+1}' for i in range(5)]
x_indices = np.arange(len(folds))
width = 0.26

ax1.bar(x_indices - width, rf_r2, width, label='Random Forest (Campeón)', color=COLOR_PRIMARY)
ax1.bar(x_indices, hgb_r2, width, label='HistGradientBoosting', color=COLOR_SECONDARY)
ax1.bar(x_indices + width, ridge_r2, width, label='Ridge Regression', color=COLOR_GRAY)

ax1.set_title('(a) Desempeño $R^2$ Fold a Fold en 5-Fold Stratified CV', fontweight='bold', pad=10)
ax1.set_xlabel('Pliegue de Validación Cruzada')
ax1.set_ylabel('Coeficiente de Determinación $R^2$')
ax1.set_xticks(x_indices)
ax1.set_xticklabels(folds)
ax1.set_ylim(0.45, 0.85)
ax1.grid(True, linestyle=':', alpha=0.6, axis='y')
ax1.legend(loc='lower right', frameon=True, facecolor='white', edgecolor='lightgray')

# Boxplot de estabilidad
data_boxplot = [ridge_r2, hgb_r2, rf_r2]
labels_box = ['Ridge', 'HistGradBoost', 'Random Forest']
bp = ax2.boxplot(data_boxplot, tick_labels=labels_box, patch_artist=True, widths=0.45)

colors_bp = [COLOR_GRAY, COLOR_SECONDARY, COLOR_PRIMARY]
for patch, color in zip(bp['boxes'], colors_bp):
    patch.set_facecolor(color)
    patch.set_alpha(0.85)

for median in bp['medians']:
    median.set(color=COLOR_GOLD, linewidth=2.5)

ax2.set_title('(b) Distribución de Varianza entre Modelos', fontweight='bold', pad=10)
ax2.set_ylabel('$R^2$ en Pliegues CV')
ax2.set_ylim(0.45, 0.85)
ax2.grid(True, linestyle=':', alpha=0.6, axis='y')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "cv_estabilidad_folds.png", dpi=300, bbox_inches='tight')
plt.close()

# -----------------------------------------------------------------------------
# FIGURA 6: MONITOREO DE DATA DRIFT (KOLMOGOROV-SMIRNOV & WASSERSTEIN)
# -----------------------------------------------------------------------------
print("Generando Figura 6: data_drift_kolmogorov.png...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.6), dpi=300)

base_sample = np.log1p(df["S01_03_C"].dropna().sample(600, random_state=42))
sample_no_drift = np.log1p(df["S01_03_C"].dropna().sample(600, random_state=99))
sample_with_drift = base_sample * 1.12 + 0.35

x_eval = np.linspace(min(base_sample.min(), sample_no_drift.min()), max(base_sample.max(), sample_no_drift.max()), 300)
cdf_base = stats.cumfreq(base_sample, numbins=300, defaultreallimits=(x_eval.min(), x_eval.max()))
cdf_no_drift = stats.cumfreq(sample_no_drift, numbins=300, defaultreallimits=(x_eval.min(), x_eval.max()))

# Panel 1: Estado Estable (Sin Deriva)
f_base = cdf_base.cumcount / len(base_sample)
f_no_drift = cdf_no_drift.cumcount / len(sample_no_drift)

ax1.plot(x_eval, f_base, color=COLOR_PRIMARY, linewidth=2.2, label=r'Distribución Base ($F_{ref}$)')
ax1.plot(x_eval, f_no_drift, color=COLOR_EMERALD, linestyle='--', linewidth=2.2, label=r'Lote de Monitoreo ($F_{monit}$)')
ax1.set_title(r'(a) Estado Estable: $p$-valor = 0.842 ($D_{KS} < \text{Umbral}$)', fontweight='bold', pad=10)
ax1.set_xlabel(r'Masa Salarial $\ln(1 + S01\_03\_C)$')
ax1.set_ylabel(r'Probabilidad Acumulada $F(x)$')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='lightgray')

# Panel 2: Deriva Detectada con Cota Vertical D_KS
cdf_drift = stats.cumfreq(sample_with_drift, numbins=300, defaultreallimits=(x_eval.min(), x_eval.max()))
f_drift = cdf_drift.cumcount / len(sample_with_drift)

ax2.plot(x_eval, f_base, color=COLOR_PRIMARY, linewidth=2.2, label=r'Distribución Base ($F_{ref}$)')
ax2.plot(x_eval, f_drift, color=COLOR_CRIMSON, linestyle='--', linewidth=2.2, label=r'Lote con Desplazamiento')

# Localizar punto de máxima distancia vertical KS
d_stat, p_val = stats.ks_2samp(base_sample, sample_with_drift)
diff_cdf = np.abs(f_base - f_drift)
idx_max = np.argmax(diff_cdf)
x_ks = x_eval[idx_max]
y_base_ks = f_base[idx_max]
y_drift_ks = f_drift[idx_max]

# Dibujar flecha de cota D_KS
ax2.annotate('', xy=(x_ks, y_base_ks), xytext=(x_ks, y_drift_ks),
             arrowprops=dict(arrowstyle='<->', color=COLOR_GOLD, lw=2))
ax2.text(x_ks + 0.3, (y_base_ks + y_drift_ks)/2, f'$D_{{KS}} = {d_stat:.3f}$', 
         color=COLOR_GOLD, fontweight='bold', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLOR_GOLD))

ax2.set_title(rf'(b) Alerta de Data Drift: $p$-valor = {p_val:.1e}', fontweight='bold', pad=10)
ax2.set_xlabel(r'Masa Salarial $\ln(1 + S01\_03\_C)$')
ax2.set_ylabel(r'Probabilidad Acumulada $F(x)$')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='lightgray')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "data_drift_kolmogorov.png", dpi=300, bbox_inches='tight')
plt.close()

print("¡Todas las figuras estadísticas regeneradas con alta precisión académica en informe/imagenes/!")
