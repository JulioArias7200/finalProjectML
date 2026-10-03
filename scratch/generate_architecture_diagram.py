"""
Generador de Diagrama de Arquitectura Empresarial de Datos (Estilo Informatica / AWS)
Versión Optimizada: Posicionamiento perfecto, sin superposiciones de texto o flechas.
Produce: informe/imagenes/pipeline_linaje_datos.png en 300 DPI
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, BoxStyle, Circle, Polygon
import numpy as np

def draw_database_icon(ax, x, y, width=0.048, height=0.075, color="#0284C7", label="DB"):
    """Dibuja un icono estilizado de base de datos relacional tipo MS SQL / Informatica."""
    disc_h = height / 3.0
    for i in range(3):
        cy = y - (i * disc_h * 0.85)
        rect = FancyBboxPatch((x - width/2, cy - disc_h/2), width, disc_h,
                              boxstyle=BoxStyle("Round", pad=0.004, rounding_size=0.008),
                              facecolor=color, edgecolor="#0369A1", linewidth=1.2, zorder=5)
        ax.add_patch(rect)
    badge = Circle((x + width*0.35, y - height*0.25), width*0.26, facecolor="#0F172A", edgecolor="white", linewidth=1.2, zorder=6)
    ax.add_patch(badge)
    ax.text(x + width*0.35, y - height*0.25, label, color="white", fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=7)

def draw_storage_cube_icon(ax, x, y, size=0.048, color="#D96B27"):
    """Dibuja un icono de cubos apilados estilo Amazon EMR / Block Storage."""
    pts_top = np.array([
        [x, y + size*0.5],
        [x + size*0.6, y + size*0.2],
        [x, y - size*0.1],
        [x - size*0.6, y + size*0.2]
    ])
    poly_top = Polygon(pts_top, facecolor="#FF9900", edgecolor="#B25000", linewidth=1.2, zorder=6)
    ax.add_patch(poly_top)
    
    for dy, col in [(-size*0.35, color), (-size*0.7, "#A34700")]:
        pts_layer = np.array([
            [x, y + dy + size*0.3],
            [x + size*0.6, y + dy],
            [x + size*0.6, y + dy - size*0.25],
            [x, y + dy + size*0.05],
            [x - size*0.6, y + dy - size*0.25],
            [x - size*0.6, y + dy]
        ])
        poly_layer = Polygon(pts_layer, facecolor=col, edgecolor="#662900", linewidth=1.2, zorder=5)
        ax.add_patch(poly_layer)

def draw_server_gear_icon(ax, x, y, width=0.046, height=0.072, color="#475569"):
    """Dibuja un servidor torre con un engranaje de procesamiento."""
    rect = FancyBboxPatch((x - width/2, y - height/2), width, height,
                          boxstyle=BoxStyle("Round", pad=0.004, rounding_size=0.008),
                          facecolor=color, edgecolor="#1E293B", linewidth=1.3, zorder=5)
    ax.add_patch(rect)
    for dy in [0.018, 0.004, -0.010]:
        ax.plot([x - width*0.35, x + width*0.08], [y + dy, y + dy], color="#CBD5E1", linewidth=1.5, zorder=6)
    gear_center = (x + width*0.30, y + height*0.25)
    g_outer = Circle(gear_center, width*0.30, facecolor="#94A3B8", edgecolor="#334155", linewidth=1.2, zorder=7)
    g_inner = Circle(gear_center, width*0.11, facecolor="#FFFFFF", edgecolor="#334155", linewidth=1.0, zorder=8)
    ax.add_patch(g_outer)
    ax.add_patch(g_inner)
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        tx = gear_center[0] + width*0.32 * np.cos(angle)
        ty = gear_center[1] + width*0.32 * np.sin(angle)
        ax.plot([gear_center[0], tx], [gear_center[1], ty], color="#334155", linewidth=2.2, zorder=6)

def draw_padlock_icon(ax, x, y, size=0.018, color="#F59E0B"):
    """Dibuja un candado de seguridad / blindaje."""
    rect = FancyBboxPatch((x - size*0.7, y - size*0.8), size*1.4, size*1.1,
                          boxstyle=BoxStyle("Round", pad=0.002, rounding_size=0.004),
                          facecolor=color, edgecolor="#92400E", linewidth=1.1, zorder=6)
    ax.add_patch(rect)
    arc = patches.Arc((x, y + size*0.12), size*0.9, size*1.1, angle=0, theta1=0, theta2=180,
                      color="#92400E", linewidth=1.8, zorder=5)
    ax.add_patch(arc)

def draw_gateway_icon(ax, x, y, radius=0.035, color="#F97316"):
    """Dibuja la pasarela de internet / API Gateway."""
    circ = Circle((x, y), radius, facecolor=color, edgecolor="#C2410C", linewidth=1.4, zorder=6)
    ax.add_patch(circ)
    ax.scatter([x-0.012, x, x+0.012], [y-0.003, y+0.006, y-0.003], s=170, color="white", zorder=7)
    ax.scatter([x-0.006, x+0.006], [y-0.007, y-0.007], s=150, color="white", zorder=7)

def draw_workstation_icon(ax, x, y, width=0.065, height=0.045, color="#475569"):
    """Dibuja una estación de trabajo / laptop y usuarios corporativos."""
    screen = FancyBboxPatch((x - width*0.45, y - height*0.15), width*0.9, height*0.75,
                            boxstyle=BoxStyle("Round", pad=0.003, rounding_size=0.006),
                            facecolor="#FFFFFF", edgecolor="#1E293B", linewidth=1.4, zorder=6)
    ax.add_patch(screen)
    base = FancyBboxPatch((x - width*0.55, y - height*0.42), width*1.1, height*0.18,
                          boxstyle=BoxStyle("Round", pad=0.002, rounding_size=0.004),
                          facecolor="#CBD5E1", edgecolor="#1E293B", linewidth=1.1, zorder=6)
    ax.add_patch(base)
    user_y = y + height*0.95
    for dx, sc, col in [(-0.022, 0.75, "#94A3B8"), (0.022, 0.75, "#94A3B8"), (0, 0.95, "#1E293B")]:
        ux = x + dx
        head = Circle((ux, user_y + 0.015*sc), 0.009*sc, facecolor=col, zorder=7)
        body = patches.Arc((ux, user_y - 0.008*sc), 0.028*sc, 0.024*sc, angle=0, theta1=0, theta2=180,
                           color=col, linewidth=3.2*sc, zorder=7)
        ax.add_patch(head)
        ax.add_patch(body)

def main():
    fig, ax = plt.subplots(figsize=(16.5, 9.2), dpi=300)
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 1.0)
    ax.axis("off")

    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")

    # =========================================================================
    # 1. CONTENEDOR IZQUIERDA: PERÍMETRO DE DATOS CRUDOS INE
    # =========================================================================
    rect_raw = FancyBboxPatch((0.02, 0.04), 0.28, 0.92,
                              boxstyle=BoxStyle("Round", pad=0.008, rounding_size=0.02),
                              facecolor="#F8FAFC", edgecolor="#0F172A", linewidth=1.8, zorder=1)
    ax.add_patch(rect_raw)
    
    badge_raw = FancyBboxPatch((0.032, 0.915), 0.14, 0.038,
                               boxstyle=BoxStyle("Round", pad=0.003, rounding_size=0.008),
                               facecolor="#0F172A", edgecolor="#0F172A", linewidth=1.0, zorder=2)
    ax.add_patch(badge_raw)
    ax.text(0.102, 0.934, "INE RAW STORAGE", color="#F8FAFC", fontsize=8.8, fontweight="bold", ha="center", va="center", zorder=3)
    draw_padlock_icon(ax, 0.19, 0.934, size=0.013, color="#F59E0B")

    # --- SUB-CARD 1: DATASET PRIMARIO ---
    card_dp = FancyBboxPatch((0.038, 0.52), 0.244, 0.37,
                             boxstyle=BoxStyle("Round", pad=0.006, rounding_size=0.012),
                             facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.3, zorder=2)
    ax.add_patch(card_dp)
    draw_database_icon(ax, 0.16, 0.79, width=0.052, height=0.082, color="#0284C7", label="DP")
    
    ax.text(0.16, 0.705, "DATASET PRIMARIO", color="#0F172A", fontsize=11.2, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.675, "MOD_ANUAL_S01-07_12_general_i.csv", color="#0369A1", fontsize=8.2, fontfamily="monospace", fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.645, "Base Maestra Censal (167 variables)", color="#475569", fontsize=8.4, ha="center", va="center", zorder=3)
    ax.text(0.16, 0.615, "N = 3,153 empresas | Clave: ID (1:1)", color="#0F172A", fontsize=8.8, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.585, "SHA-256: e711b839... (3.61 MB)", color="#64748B", fontsize=7.4, fontfamily="monospace", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.555, "Integridad: 100% IDs Unicos (0 duplicados)", color="#059669", fontsize=7.6, fontweight="bold", ha="center", va="center", zorder=3)

    # --- SUB-CARD 2: DATASET SECUNDARIO ---
    card_ds = FancyBboxPatch((0.038, 0.07), 0.244, 0.42,
                             boxstyle=BoxStyle("Round", pad=0.006, rounding_size=0.012),
                             facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.3, zorder=2)
    ax.add_patch(card_ds)
    draw_storage_cube_icon(ax, 0.16, 0.39, size=0.050, color="#EA580C")
    
    ax.text(0.16, 0.295, "DATASET SECUNDARIO", color="#0F172A", fontsize=11.2, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.265, "MOD_ANUAL_S10_materiales_i.csv", color="#C2410C", fontsize=8.2, fontfamily="monospace", fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.235, "Detalle Desagregado de Materias Primas", color="#475569", fontsize=8.4, ha="center", va="center", zorder=3)
    ax.text(0.16, 0.205, "6,428 lineas fisicas (8 cols) | Clave: ID (N:1)", color="#0F172A", fontsize=8.4, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.175, "Fila 6,429 vacia de origen (descartada)", color="#DC2626", fontsize=8.0, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.145, "6,427 registros validos | Negativos a NaN", color="#D97706", fontsize=8.0, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.115, "SHA-256: b41ad4ed... (495 KB)", color="#64748B", fontsize=7.4, fontfamily="monospace", ha="center", va="center", zorder=3)
    ax.text(0.16, 0.088, "Subconjunto: 1,614 manufactureras fabriles", color="#4F46E5", fontsize=7.6, fontweight="bold", ha="center", va="center", zorder=3)

    # =========================================================================
    # 2. CONTENEDOR CENTRAL: MOTOR DE INTEGRACIÓN Y GOBERNANZA
    # =========================================================================
    rect_engine = FancyBboxPatch((0.34, 0.04), 0.44, 0.92,
                                boxstyle=BoxStyle("Round", pad=0.008, rounding_size=0.02),
                                facecolor="#F8FAFC", edgecolor="#0F172A", linewidth=1.8, zorder=1)
    ax.add_patch(rect_engine)
    
    badge_engine = FancyBboxPatch((0.352, 0.915), 0.21, 0.038,
                                  boxstyle=BoxStyle("Round", pad=0.003, rounding_size=0.008),
                                  facecolor="#2563EB", edgecolor="#2563EB", linewidth=1.0, zorder=2)
    ax.add_patch(badge_engine)
    ax.text(0.457, 0.934, "DATA INTEGRATION & GOVERNANCE", color="#FFFFFF", fontsize=8.5, fontweight="bold", ha="center", va="center", zorder=3)
    draw_padlock_icon(ax, 0.58, 0.934, size=0.013, color="#F59E0B")

    # --- PASO 1 INTERNO: Saneamiento Secundario ---
    card_clean = FancyBboxPatch((0.355, 0.61), 0.185, 0.26,
                                boxstyle=BoxStyle("Round", pad=0.005, rounding_size=0.010),
                                facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.2, zorder=2)
    ax.add_patch(card_clean)
    draw_server_gear_icon(ax, 0.447, 0.78, width=0.044, height=0.070, color="#475569")
    ax.text(0.447, 0.710, "SANEAMIENTO SECUNDARIO", color="#0F172A", fontsize=9.2, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.447, 0.680, "Exclusión Fila 6,429 Vacía", color="#DC2626", fontsize=8.0, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.447, 0.655, "6,428 líneas -> 6,427 analíticas", color="#334155", fontsize=7.6, ha="center", va="center", zorder=3)
    ax.text(0.447, 0.630, "Importes negativos a NaN", color="#D97706", fontsize=7.6, fontweight="bold", ha="center", va="center", zorder=3)

    # --- PASO 2 INTERNO: Agregación Relacional N:1 ---
    card_agg = FancyBboxPatch((0.575, 0.61), 0.19, 0.26,
                              boxstyle=BoxStyle("Round", pad=0.005, rounding_size=0.010),
                              facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.2, zorder=2)
    ax.add_patch(card_agg)
    draw_database_icon(ax, 0.67, 0.78, width=0.048, height=0.072, color="#4F46E5", label="N:1")
    ax.text(0.67, 0.710, "AGREGACIÓN RELACIONAL", color="#0F172A", fontsize=9.2, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.67, 0.680, "Colapso N:1 por ID Empresa", color="#4338CA", fontsize=8.0, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.67, 0.655, "6,427 insumos -> 1,614 fabriles", color="#0F172A", fontsize=8.0, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.67, 0.630, "n_insumos, total_valor_co, uti", color="#475569", fontsize=7.4, fontfamily="monospace", ha="center", va="center", zorder=3)

    # Flecha interna Limpieza -> Agregación
    arrow_clean_agg = patches.FancyArrowPatch((0.542, 0.74), (0.572, 0.74),
                                              arrowstyle="-|>,head_length=5,head_width=3",
                                              color="#334155", linewidth=1.6, zorder=4)
    ax.add_patch(arrow_clean_agg)

    # --- NÚCLEO INFERIOR: Fusión, Anti-Leakage, log1p y Muestreo ---
    card_core = FancyBboxPatch((0.355, 0.07), 0.41, 0.49,
                               boxstyle=BoxStyle("Round", pad=0.006, rounding_size=0.012),
                               facecolor="#FFFFFF", edgecolor="#2563EB", linewidth=1.6, zorder=2)
    ax.add_patch(card_core)
    
    ax.text(0.56, 0.535, "PROCESAMIENTO CENTRAL & GOBERNANZA ESTADÍSTICA", color="#1E3A8A", fontsize=9.8, fontweight="bold", ha="center", va="center", zorder=3)
    
    # 4 Cajas en Grid 2x2
    # 1. Left Join
    box_join = FancyBboxPatch((0.368, 0.40), 0.185, 0.105, boxstyle=BoxStyle("Round", pad=0.003, rounding_size=0.006),
                              facecolor="#EFF6FF", edgecolor="#BFDBFE", linewidth=1.0, zorder=3)
    ax.add_patch(box_join)
    ax.text(0.460, 0.478, "CRUCE LEFT JOIN & CAEB", color="#1E40AF", fontsize=8.4, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(0.460, 0.452, "Preserva 3,153 empresas base", color="#334155", fontsize=7.5, ha="center", va="center", zorder=4)
    ax.text(0.460, 0.428, "1,539 comercio: n_insumos = 0", color="#059669", fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=4)

    # 2. Anti-Leakage
    box_leak = FancyBboxPatch((0.565, 0.40), 0.188, 0.105, boxstyle=BoxStyle("Round", pad=0.003, rounding_size=0.006),
                              facecolor="#FEF2F2", edgecolor="#FECACA", linewidth=1.0, zorder=3)
    ax.add_patch(box_leak)
    draw_padlock_icon(ax, 0.582, 0.478, size=0.008, color="#DC2626")
    ax.text(0.665, 0.478, "BLINDAJE ANTI-LEAKAGE", color="#991B1B", fontsize=8.2, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(0.658, 0.452, "19 variables contables excluidas", color="#DC2626", fontsize=7.4, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(0.658, 0.428, "VBP, VA, CI, S05_01 a S05_04", color="#475569", fontsize=7.0, fontfamily="monospace", ha="center", va="center", zorder=4)

    # 3. Log1p
    box_log = FancyBboxPatch((0.368, 0.275), 0.185, 0.105, boxstyle=BoxStyle("Round", pad=0.003, rounding_size=0.006),
                             facecolor="#F0FDF4", edgecolor="#BBF7D0", linewidth=1.0, zorder=3)
    ax.add_patch(box_log)
    ax.text(0.460, 0.352, "ESTABILIZACIÓN ln(1+x)", color="#166534", fontsize=8.4, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(0.460, 0.327, "Varianza Homogénea Residual", color="#334155", fontsize=7.5, ha="center", va="center", zorder=4)
    ax.text(0.460, 0.302, "Corrección Asimetría Pareto", color="#15803D", fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=4)

    # 4. Partición
    box_split = FancyBboxPatch((0.565, 0.275), 0.188, 0.105, boxstyle=BoxStyle("Round", pad=0.003, rounding_size=0.006),
                               facecolor="#FAF5FF", edgecolor="#E9D5FF", linewidth=1.0, zorder=3)
    ax.add_patch(box_split)
    ax.text(0.658, 0.352, "PARTICIÓN ESTRATIFICADA", color="#6B21A8", fontsize=8.4, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(0.658, 0.327, "Train 60% (1,891) | Deciles", color="#334155", fontsize=7.5, ha="center", va="center", zorder=4)
    ax.text(0.658, 0.302, "Calib 20% (631) | Test 20% (631)", color="#7E22CE", fontsize=7.4, fontweight="bold", ha="center", va="center", zorder=4)

    # Dataset Procesado Barra Inferior
    rect_proc = FancyBboxPatch((0.368, 0.09), 0.385, 0.165, boxstyle=BoxStyle("Round", pad=0.003, rounding_size=0.006),
                               facecolor="#0F172A", edgecolor="#0F172A", linewidth=1.0, zorder=3)
    ax.add_patch(rect_proc)
    ax.text(0.56, 0.218, "DATASET PROCESADO INMUTABLE (dataset_procesado.csv)", color="#38BDF8", fontsize=8.8, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(0.56, 0.188, "3,153 empresas x 184 columnas | Peso: 4.30 MB | Clave: ID (1:1)", color="#F8FAFC", fontsize=8.0, ha="center", va="center", zorder=4)
    ax.text(0.56, 0.158, "SHA-256: 753510bc65b4be2fbe3c5727a7b7b3702ebf6e8fdf826d1558a3d121ccadbc08", color="#94A3B8", fontsize=6.8, fontfamily="monospace", ha="center", va="center", zorder=4)
    ax.text(0.56, 0.125, "Gobernanza: Validado para Entrenamiento, Calibración Conformal y Monitoreo Drift", color="#10B981", fontsize=7.2, fontweight="bold", ha="center", va="center", zorder=4)

    # =========================================================================
    # 3. FLECHAS DE CONEXIÓN CON ETIQUETAS DESPEJADAS
    # =========================================================================
    # Conector Dataset Primario -> Left Join
    conn_dp = patches.FancyArrowPatch((0.282, 0.65), (0.355, 0.46),
                                     arrowstyle="-|>,head_length=6,head_width=3.5",
                                     connectionstyle="arc3,rad=-0.10",
                                     color="#0284C7", linewidth=2.0, zorder=4)
    ax.add_patch(conn_dp)
    ax.text(0.312, 0.585, "1:1 Base", color="#0284C7", fontsize=8.0, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#BFDBFE", lw=0.8), zorder=5)

    # Conector Dataset Secundario -> Saneamiento
    conn_ds = patches.FancyArrowPatch((0.282, 0.28), (0.355, 0.72),
                                     arrowstyle="-|>,head_length=6,head_width=3.5",
                                     connectionstyle="arc3,rad=0.18",
                                     color="#EA580C", linewidth=2.0, zorder=4)
    ax.add_patch(conn_ds)
    ax.text(0.312, 0.455, "N:1 Crudo", color="#EA580C", fontsize=8.0, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#FED7AA", lw=0.8), zorder=5)

    # Conector Agregación -> Cruce Left Join (Ruta despejada)
    conn_agg_join = patches.FancyArrowPatch((0.67, 0.61), (0.465, 0.51),
                                           arrowstyle="-|>,head_length=6,head_width=3.5",
                                           connectionstyle="arc3,rad=-0.12",
                                           color="#4F46E5", linewidth=2.0, zorder=4)
    ax.add_patch(conn_agg_join)
    ax.text(0.605, 0.575, "1,614 Fabriles", color="#4F46E5", fontsize=7.8, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#C7D2FE", lw=0.8), zorder=5)

    # =========================================================================
    # 4. REST API GATEWAY
    # =========================================================================
    draw_gateway_icon(ax, 0.818, 0.54, radius=0.030, color="#F97316")
    ax.text(0.818, 0.485, "REST API GATEWAY", color="#0F172A", fontsize=8.2, fontweight="bold", ha="center", va="center", zorder=6)
    ax.text(0.818, 0.458, "/api/dataset/metadata", color="#475569", fontsize=6.8, fontfamily="monospace", ha="center", va="center", zorder=6)
    ax.text(0.818, 0.436, "/api/dataset/lineage", color="#475569", fontsize=6.8, fontfamily="monospace", ha="center", va="center", zorder=6)

    # Flechas bidireccionales Motor <-> Gateway
    arrow_eng_gw = patches.FancyArrowPatch((0.78, 0.54), (0.788, 0.54),
                                          arrowstyle="<|-|>,head_length=5,head_width=3",
                                          color="#1E293B", linewidth=1.6, zorder=5)
    ax.add_patch(arrow_eng_gw)

    # =========================================================================
    # 5. CONTENEDOR DERECHA: CONSUMIDORES CORPORATIVOS
    # =========================================================================
    rect_corp = FancyBboxPatch((0.865, 0.04), 0.118, 0.92,
                              boxstyle=BoxStyle("Round", pad=0.008, rounding_size=0.02),
                              facecolor="#F8FAFC", edgecolor="#0F172A", linewidth=1.8, zorder=1)
    ax.add_patch(rect_corp)

    badge_corp = FancyBboxPatch((0.874, 0.915), 0.10, 0.038,
                                boxstyle=BoxStyle("Round", pad=0.003, rounding_size=0.008),
                                facecolor="#0F172A", edgecolor="#0F172A", linewidth=1.0, zorder=2)
    ax.add_patch(badge_corp)
    ax.text(0.924, 0.934, "CONSUMERS", color="#FFFFFF", fontsize=8.2, fontweight="bold", ha="center", va="center", zorder=3)

    draw_workstation_icon(ax, 0.924, 0.68, width=0.065, height=0.045, color="#334155")
    ax.text(0.924, 0.615, "USUARIOS /", color="#0F172A", fontsize=9.0, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(0.924, 0.592, "AUDITORES", color="#0F172A", fontsize=9.0, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(0.924, 0.568, "Inspección Fiscal", color="#64748B", fontsize=7.4, ha="center", va="center", zorder=4)

    card_dash = FancyBboxPatch((0.874, 0.18), 0.10, 0.32,
                               boxstyle=BoxStyle("Round", pad=0.004, rounding_size=0.008),
                               facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.2, zorder=2)
    ax.add_patch(card_dash)
    ax.text(0.924, 0.468, "DASHBOARD", color="#2563EB", fontsize=8.8, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.924, 0.446, "Flask / Render", color="#64748B", fontsize=7.0, fontfamily="monospace", ha="center", va="center", zorder=3)
    ax.text(0.924, 0.415, "5 Módulos Web", color="#0F172A", fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.924, 0.388, "Inferencia 90%", color="#059669", fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.924, 0.362, "Conformal Bands", color="#475569", fontsize=7.0, ha="center", va="center", zorder=3)
    ax.text(0.924, 0.336, "Alerta Riesgo", color="#DC2626", fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.924, 0.310, "Drift KS / PSI", color="#D97706", fontsize=7.0, ha="center", va="center", zorder=3)
    ax.text(0.924, 0.258, "Metadatos &", color="#4338CA", fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(0.924, 0.235, "Linaje Dinámico", color="#4338CA", fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=3)

    arrow_gw_client = patches.FancyArrowPatch((0.848, 0.54), (0.865, 0.54),
                                              arrowstyle="<|-|>,head_length=5,head_width=3",
                                              color="#1E293B", linewidth=1.6, zorder=5)
    ax.add_patch(arrow_gw_client)

    arrow_user_dash = patches.FancyArrowPatch((0.924, 0.55), (0.924, 0.505),
                                              arrowstyle="<|-|>,head_length=4,head_width=2.5",
                                              color="#64748B", linewidth=1.2, zorder=5)
    ax.add_patch(arrow_user_dash)

    out_path = os.path.abspath("informe/imagenes/pipeline_linaje_datos.png")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print("Diagrama refinado generado exitosamente en:", out_path)

if __name__ == "__main__":
    main()
