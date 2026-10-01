"""Agregaciones descriptivas compartidas por todas las vistas del dashboard."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


MIN_CELL_N = 5


def select_rows(df: pd.DataFrame, depto: str | None = None, sector: str | None = None) -> pd.DataFrame:
    """Aplica filtros exactos sobre el mismo conjunto para KPI, tabla y gráficos."""
    selected = df
    for column, requested in (("depto", depto), ("sector_macro", sector)):
        if requested:
            if requested not in set(df[column].dropna().astype(str)):
                raise ValueError(f"Valor desconocido para {column}: {requested}")
            selected = selected[selected[column] == requested]
    return selected


def summarize_kpis(df: pd.DataFrame) -> dict[str, Any]:
    values = pd.to_numeric(df["target"], errors="coerce").dropna()
    return {
        "total_empresas": int(len(df)),
        "ingreso_mediano": float(values.median()) if not values.empty else None,
        "ingreso_promedio": float(values.mean()) if not values.empty else None,
        "ingreso_total_agregado": float(values.sum()) if not values.empty else None,
        "num_departamentos": int(df["depto"].nunique()),
        "num_macrosectores": int(df["sector_macro"].nunique()),
        "top_departamento": str(df["depto"].value_counts().index[0]) if len(df) else None,
        "top_sector": str(df["sector_macro"].value_counts().index[0]) if len(df) else None,
        "denominador": int(len(df)),
        "unidad_ingresos": "Bs",
        "poblacion": "Empresas del extracto EAIMCS; sin expansión poblacional",
        "periodo": "EAIMCS 2017; cierre fiscal según actividad",
    }


def summarize_groups(df: pd.DataFrame, column: str, min_n: int = MIN_CELL_N) -> list[dict[str, Any]]:
    """Incluye todos los grupos observados, suprimiendo estadísticos de N pequeño."""
    if column not in {"depto", "sector_macro"}:
        raise ValueError("Agrupación no permitida")
    result = []
    for name, group in df.groupby(column):
        n = len(group)
        visible = n >= min_n
        values = group["target"].to_numpy(dtype=float) if visible else np.array([])
        result.append({
            "name": str(name),
            "count": n if visible else None,
            "count_label": str(n) if visible else f"<{min_n}",
            "status": "ok" if visible else "suppressed",
            "median_bs": float(np.median(values)) if visible else None,
            "q25_bs": float(np.percentile(values, 25)) if visible else None,
            "q75_bs": float(np.percentile(values, 75)) if visible else None,
            "sample_bs": [float(v) for v in values],
            "sample_log": [float(v) for v in np.log1p(values)],
        })
    return sorted(result, key=lambda item: item["name"])


def department_sector_heatmap(df: pd.DataFrame, min_n: int = MIN_CELL_N) -> dict[str, Any]:
    """Celdas sin datos y suprimidas son null; solo cero real es numérico cero."""
    deptos = sorted(df["depto"].dropna().astype(str).unique())
    sectores = sorted(df["sector_macro"].dropna().astype(str).unique())
    grouped = df.groupby(["depto", "sector_macro"])["target"]
    cells = {(str(d), str(s)): values for (d, s), values in grouped}
    counts: list[list[int | None]] = []
    medians: list[list[float | None]] = []
    totals: list[list[float | None]] = []
    statuses: list[list[str]] = []
    for depto in deptos:
        count_row, median_row, total_row, status_row = [], [], [], []
        for sector in sectores:
            values = cells.get((depto, sector))
            if values is None or len(values) == 0:
                count_row.append(None); median_row.append(None); total_row.append(None); status_row.append("empty")
            elif len(values) < min_n:
                count_row.append(None); median_row.append(None); total_row.append(None); status_row.append("suppressed")
            else:
                count_row.append(int(len(values)))
                median_row.append(float(values.median() / 1e6))
                total_row.append(float(values.sum() / 1e6))
                status_row.append("ok")
        counts.append(count_row); medians.append(median_row); totals.append(total_row); statuses.append(status_row)
    return {
        "deptos": deptos,
        "sectores": sectores,
        "counts": counts,
        "median_bs_millions": medians,
        "total_bs_millions": totals,
        "matrix_count": counts,
        "matrix_median": medians,
        "matrix_total": totals,
        "cell_status": statuses,
        "min_cell_n": min_n,
        "denominador": int(len(df)),
        "unidad_conteo": "empresas",
        "unidad_montos": "millones de Bs",
    }
