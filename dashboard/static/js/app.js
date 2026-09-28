/**
 * LÓGICA CLIENTE: DASHBOARD DE APRENDIZAJE SUPERVISADO (EAIMCS - INE BOLIVIA)
 * Control de navegación SPA en 5 grupos, renderizado dinámico con Plotly.js,
 * auditoría de riesgos de empresas, alertas de bunching y monitoreo MLOps.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Quitar la clase no-transition tras el primer frame (doble rAF) para evitar transiciones en carga inicial
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      document.documentElement.classList.remove('no-transition');
    });
  });

  // ==========================================================================
  // ESTADO GLOBAL DE LA APLICACIÓN
  // ==========================================================================
  const state = {
    theme: document.documentElement.getAttribute('data-theme') || localStorage.getItem('theme') || 'light',
    activeSection: 'panorama',
    heatmapMetric: 'count', // 'count' | 'median' | 'total'
    distributionScale: 'log', // 'raw' | 'log'
    distributionData: null,
    boxDeptosData: null,
    boxSectorsData: null,
    correlationData: null,
    outliersData: null,
    dictionaryEntries: [],
    modelsData: null,
    bitacoraModelosData: null,
    prepBitacoraData: null,
    companiesRiskData: null,
    bunchingData: null,
    monitoringData: null,
    heatmapData: null,
    cvResults: null,
    plotlyLayoutBase: {},
    colors: {
      primary: '#0B3D62',
      primaryLight: '#1B5A8C',
      secondary: '#F4B400',
      alertAlta: '#C0392B',
      alertMedia: '#E1A100',
      alertBaja: '#1E7A46'
    }
  };

  // Formateador de moneda en Bs
  function formatMoney(num) {
    if (num === null || num === undefined || isNaN(num)) return '--';
    if (Math.abs(num) >= 1e6) {
      return `${(num / 1e6).toFixed(2)} M`;
    }
    return Math.round(num).toLocaleString('es-BO');
  }

  // ==========================================================================
  // 1. GESTIÓN DE TEMA (CLARO / OSCURO) Y PALETA INSTITUCIONAL
  // ==========================================================================
  const htmlEl = document.documentElement;
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const themeIcon = document.getElementById('themeIcon');

  function getPlotlyThemeLayout() {
    const computed = getComputedStyle(document.documentElement);
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    const paperBg = computed.getPropertyValue('--bg-surface').trim() || (isDark ? '#141C28' : '#FFFFFF');
    const textColor = computed.getPropertyValue('--text-primary').trim() || (isDark ? '#F0F4F8' : '#1A1A1A');
    const gridColor = isDark ? '#223042' : '#E1E4E8';
    const zeroColor = isDark ? '#33465E' : '#C5CBD5';

    return {
      paper_bgcolor: paperBg,
      plot_bgcolor: paperBg,
      font: { color: textColor, family: 'Inter, sans-serif' },
      xaxis: { gridcolor: gridColor, zerolinecolor: zeroColor },
      yaxis: { gridcolor: gridColor, zerolinecolor: zeroColor }
    };
  }

  function updateThemeIcon(theme) {
    if (!themeToggleBtn || !themeIcon) return;
    themeToggleBtn.classList.add('animating');
    setTimeout(() => {
      if (theme === 'dark') {
        themeIcon.innerHTML = `<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>`;
        themeToggleBtn.setAttribute('aria-label', 'Cambiar a modo claro');
        themeToggleBtn.setAttribute('aria-pressed', 'true');
        themeToggleBtn.title = 'Cambiar a modo claro';
      } else {
        themeIcon.innerHTML = `
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        `;
        themeToggleBtn.setAttribute('aria-label', 'Cambiar a modo oscuro');
        themeToggleBtn.setAttribute('aria-pressed', 'false');
        themeToggleBtn.title = 'Cambiar a modo oscuro';
      }
      themeToggleBtn.classList.remove('animating');
    }, 125);
  }

  function applyTheme(theme) {
    state.theme = theme;
    htmlEl.setAttribute('data-theme', theme);
    try {
      localStorage.setItem('theme', theme);
    } catch (e) {
      console.warn('No se pudo guardar la preferencia de tema:', e);
    }

    updateThemeIcon(theme);
    state.plotlyLayoutBase = getPlotlyThemeLayout();

    // Sincronizar todos los gráficos renderizados en el DOM con Plotly.relayout
    if (window.chartsRegistry) {
      for (const chartId of Object.keys(window.chartsRegistry)) {
        const el = document.getElementById(chartId);
        if (el && el.data && el.data.length > 0) {
          Plotly.relayout(chartId, {
            paper_bgcolor: state.plotlyLayoutBase.paper_bgcolor,
            plot_bgcolor: state.plotlyLayoutBase.plot_bgcolor,
            'font.color': state.plotlyLayoutBase.font.color,
            'xaxis.gridcolor': state.plotlyLayoutBase.xaxis.gridcolor,
            'xaxis.zerolinecolor': state.plotlyLayoutBase.xaxis.zerolinecolor,
            'yaxis.gridcolor': state.plotlyLayoutBase.yaxis.gridcolor,
            'yaxis.zerolinecolor': state.plotlyLayoutBase.yaxis.zerolinecolor
          }).catch(() => {});
        }
      }
    }
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = htmlEl.getAttribute('data-theme') || 'light';
      const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';

      const prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      if (!document.startViewTransition || prefersReduced) {
        applyTheme(nextTheme);
        return;
      }

      const rect = themeToggleBtn.getBoundingClientRect();
      const x = rect.left + rect.width / 2;
      const y = rect.top + rect.height / 2;
      const endRadius = Math.hypot(
        Math.max(x, window.innerWidth - x),
        Math.max(y, window.innerHeight - y)
      );

      const transition = document.startViewTransition(() => {
        applyTheme(nextTheme);
      });

      transition.ready.then(() => {
        document.documentElement.animate(
          {
            clipPath: [
              `circle(0px at ${x}px ${y}px)`,
              `circle(${endRadius}px at ${x}px ${y}px)`
            ]
          },
          {
            duration: 320,
            easing: 'cubic-bezier(0.4, 0, 0.2, 1)',
            pseudoElement: '::view-transition-new(root)'
          }
        );
      }).catch(() => {});
    });
  }

  // ==========================================================================
  // REGISTRO Y RECARGA INDIVIDUAL DE GRÁFICOS (PLOTLY.REACT)
  // ==========================================================================
  const chartsLoading = {};

  const chartsRegistry = {
    chartHeatmapDeptoSector: {
      endpoint: '/api/eda/heatmap_depto_sector',
      stateProp: 'heatmapData',
      render: () => renderHeatmapDeptoSector(state.heatmapMetric)
    },
    chartRealVsPred: {
      endpoint: '/api/models',
      stateProp: 'modelsData',
      render: () => renderRealVsPredChart()
    },
    chartResidualsHist: {
      endpoint: '/api/models',
      stateProp: 'modelsData',
      render: () => renderResidualsHistChart()
    },
    chartModelsBarComparison: {
      endpoint: '/api/bitacora_modelos',
      stateProp: 'bitacoraModelosData',
      render: () => renderModelsBarComparison()
    },
    chartFeatureImportance: {
      endpoint: '/api/models',
      stateProp: 'modelsData',
      render: () => renderFeatureImportanceChart()
    },
    chartCvFolds: {
      endpoint: '/api/cross_validation',
      stateProp: 'cvResults',
      render: () => renderCvFoldsChart()
    },
    chartCvStability: {
      endpoint: '/api/cross_validation',
      stateProp: 'cvResults',
      render: () => renderCvStabilityChart()
    },
    chartCvBoxplot: {
      endpoint: '/api/cross_validation',
      stateProp: 'cvResults',
      render: () => renderCvBoxplotChart()
    },
    chartCvVsTest: {
      endpoint: '/api/cross_validation',
      stateProp: 'cvResults',
      render: () => renderCvVsTestChart()
    },
    chartTrafficVolume: {
      endpoint: '/api/mlops/monitoring',
      stateProp: 'monitoringData',
      render: () => renderTrafficChart()
    },
    chartDistribution: {
      endpoint: '/api/eda/distribution',
      stateProp: 'distributionData',
      render: () => renderDistributionChart(state.distributionScale)
    },
    chartBoxDeptos: {
      endpoint: '/api/eda/boxplot_deptos',
      stateProp: 'boxDeptosData',
      render: () => renderBoxplotDeptos()
    },
    chartBoxSectors: {
      endpoint: '/api/eda/boxplot_sectors',
      stateProp: 'boxSectorsData',
      render: () => renderBoxplotSectors()
    },
    chartCorrelation: {
      endpoint: '/api/eda/correlations',
      stateProp: 'correlationData',
      render: () => renderCorrelationChart()
    },
    chartOutliers: {
      endpoint: '/api/eda/outliers',
      stateProp: 'outliersData',
      render: () => renderOutliersChart()
    }
  };
  window.chartsRegistry = chartsRegistry;

  window.reloadChart = async function(chartId, force = true) {
    const cfg = chartsRegistry[chartId];
    if (!cfg) return;

    if (chartsLoading[chartId]) return;
    chartsLoading[chartId] = true;

    const loadingEl = document.getElementById(`loading-${chartId}`);
    const errorEl = document.getElementById(`error-${chartId}`);
    const btn = document.querySelector(`.chart-refresh-btn[data-chart="${chartId}"]`);

    if (loadingEl) loadingEl.style.display = 'flex';
    if (errorEl) errorEl.style.display = 'none';
    if (btn) btn.classList.add('spinning');

    try {
      if (force || !state[cfg.stateProp]) {
        const url = cfg.endpoint + (force ? `?_t=${Date.now()}` : '');
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        state[cfg.stateProp] = await res.json();
      }
      await cfg.render();
      if (loadingEl) loadingEl.style.display = 'none';
    } catch (err) {
      console.error(`Error al cargar o renderizar gráfico ${chartId}:`, err);
      if (loadingEl) loadingEl.style.display = 'none';
      if (errorEl) errorEl.style.display = 'flex';
    } finally {
      chartsLoading[chartId] = false;
      if (btn) btn.classList.remove('spinning');
    }
  };

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.chart-refresh-btn');
    if (btn) {
      const chartId = btn.getAttribute('data-chart');
      if (chartId && typeof window.reloadChart === 'function') {
        window.reloadChart(chartId, true);
      }
    }
  });

  applyTheme(state.theme);

  // ==========================================================================
  // 2. NAVEGACIÓN EN 5 GRUPOS PRINCIPALES & SUB-TABS
  // ==========================================================================
  const navBtns = document.querySelectorAll('.nav-item-btn');
  const panels = document.querySelectorAll('.section-panel');
  const sectionTitle = document.getElementById('currentSectionTitle');
  const sectionSubtitle = document.getElementById('currentSectionSubtitle');

  const titlesMap = {
    'panorama': {
      title: 'Panorama General',
      sub: 'Indicadores macroeconómicos y mapa de calor territorial-sectorial'
    },
    'riesgo': {
      title: 'Empresas & Riesgo',
      sub: 'Auditoría de consistencia de ingresos y detección de bunching sectorial'
    },
    'modelo_validez': {
      title: 'Modelo & Validez',
      sub: 'Diagnóstico de algoritmos, validación cruzada y simulador predictivo'
    },
    'monitoreo': {
      title: 'Monitoreo & Seguridad',
      sub: 'Gobernanza MLOps, monitoreo de consultas y detección de data drift'
    },
    'gobernanza': {
      title: 'Metodología & Gobernanza',
      sub: 'Bitácora de preprocesamiento, análisis exploratorio y marco lógico'
    }
  };

  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.getAttribute('data-section');
      switchSection(target);
    });
  });

  function switchSection(sectionId) {
    state.activeSection = sectionId;

    navBtns.forEach(b => b.classList.toggle('active', b.getAttribute('data-section') === sectionId));
    panels.forEach(p => p.classList.toggle('active', p.id === `panel-${sectionId}`));

    const meta = titlesMap[sectionId] || { title: 'Dashboard', sub: '' };
    sectionTitle.textContent = meta.title;
    sectionSubtitle.textContent = meta.sub;

    // Disparar carga bajo demanda en paralelo (Promise.all) solo de los gráficos visibles
    if (sectionId === 'panorama') {
      Promise.all([
        loadKPIs(),
        reloadChart('chartHeatmapDeptoSector', false)
      ]);
    } else if (sectionId === 'riesgo') {
      loadCompaniesRisk();
      loadBunchingAlerts();
    } else if (sectionId === 'modelo_validez') {
      // Subtab activo por defecto: mv-diagnostico
      Promise.all([
        loadBitacoraModelos(),
        reloadChart('chartRealVsPred', false),
        reloadChart('chartResidualsHist', false),
        reloadChart('chartModelsBarComparison', false),
        reloadChart('chartFeatureImportance', false)
      ]);
    } else if (sectionId === 'monitoreo') {
      // Subtab activo por defecto: mon-trafico
      loadMLOps();
      Promise.all([
        loadMonitoring(),
        reloadChart('chartTrafficVolume', false)
      ]);
    } else if (sectionId === 'gobernanza') {
      // Subtab activo por defecto: gob-pipeline
      loadBitacoraPreprocesamiento();
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(() => window.dispatchEvent(new Event('resize')), 150);
  }

  // Toggle colapsar sidebar
  const sidebarToggle = document.getElementById('sidebarToggle');
  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', () => {
      document.body.classList.toggle('sidebar-collapsed');
      setTimeout(() => window.dispatchEvent(new Event('resize')), 200);
    });
  }

  // Gestión de Sub-navegación dentro de cada panel con carga diferida (lazy loading)
  const subnavBtns = document.querySelectorAll('.subnav-tab-btn');
  subnavBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const parentPanel = btn.closest('.section-panel');
      if (!parentPanel) return;

      const subtabTarget = btn.getAttribute('data-subtab');
      // Actualizar botones del subnav en este panel
      parentPanel.querySelectorAll('.subnav-tab-btn').forEach(b => b.classList.toggle('active', b === btn));

      // Ocultar todos los subtab-contents y mostrar el seleccionado
      parentPanel.querySelectorAll('[id^="subtab-content-"]').forEach(content => {
        if (content.id === `subtab-content-${subtabTarget}`) {
          content.style.display = 'block';
        } else {
          content.style.display = 'none';
        }
      });

      // Refrescar tamaño de gráficos Plotly
      setTimeout(() => window.dispatchEvent(new Event('resize')), 100);

      // Si se abre CV, cargar de forma diferida (lazy) los 4 gráficos de validación cruzada
      if (subtabTarget === 'mv-cv') {
        Promise.all([
          reloadChart('chartCvFolds', false),
          reloadChart('chartCvStability', false),
          reloadChart('chartCvBoxplot', false),
          reloadChart('chartCvVsTest', false)
        ]);
      }
      // Si se abre EDA, cargar de forma diferida (lazy) los 5 gráficos de análisis exploratorio
      if (subtabTarget === 'gob-eda') {
        Promise.all([
          reloadChart('chartDistribution', false),
          reloadChart('chartBoxDeptos', false),
          reloadChart('chartBoxSectors', false),
          reloadChart('chartCorrelation', false),
          reloadChart('chartOutliers', false)
        ]);
      }
      // Si se abre diccionario, cargar si vacío
      if (subtabTarget === 'gob-diccionario' && state.dictionaryEntries.length === 0) {
        loadDictionary();
      }
    });
  });

  // ==========================================================================
  // 3. MÓDULO 1: PANORAMA GENERAL & HEATMAP DEPTO X SECTOR
  // ==========================================================================
  async function loadKPIs() {
    try {
      const res = await fetch('/api/kpis');
      const data = await res.json();
      document.getElementById('kpiTotalEmpresas').textContent = Number(data.total_empresas).toLocaleString('es-BO');
      document.getElementById('kpiIngresoMediano').textContent = `Bs ${(data.ingreso_mediano / 1e6).toFixed(2)} M`;
      document.getElementById('kpiIngresoPromedio').textContent = `Bs ${(data.ingreso_promedio / 1e6).toFixed(2)} M`;
      document.getElementById('kpiDeptos').textContent = `${data.num_departamentos} Deptos`;
    } catch (e) {
      console.error('Error al cargar KPIs:', e);
    }
  }
  loadKPIs();

  const btnHeatmapMetricCount = document.getElementById('btnHeatmapMetricCount');
  const btnHeatmapMetricMedian = document.getElementById('btnHeatmapMetricMedian');
  const btnHeatmapMetricTotal = document.getElementById('btnHeatmapMetricTotal');

  function updateHeatmapMetricBtns(activeMetric) {
    state.heatmapMetric = activeMetric;
    const btns = [
      { el: btnHeatmapMetricCount, key: 'count' },
      { el: btnHeatmapMetricMedian, key: 'median' },
      { el: btnHeatmapMetricTotal, key: 'total' }
    ];

    btns.forEach(b => {
      if (!b.el) return;
      if (b.key === activeMetric) {
        b.el.className = 'status-pill active';
        b.el.style.background = '';
        b.el.style.color = '';
      } else {
        b.el.className = 'status-pill';
        b.el.style.background = 'var(--bg-surface-elevated)';
        b.el.style.color = 'var(--text-primary)';
      }
    });
  }

  if (btnHeatmapMetricCount) {
    btnHeatmapMetricCount.addEventListener('click', () => {
      updateHeatmapMetricBtns('count');
      renderHeatmapDeptoSector('count');
    });
  }
  if (btnHeatmapMetricMedian) {
    btnHeatmapMetricMedian.addEventListener('click', () => {
      updateHeatmapMetricBtns('median');
      renderHeatmapDeptoSector('median');
    });
  }
  if (btnHeatmapMetricTotal) {
    btnHeatmapMetricTotal.addEventListener('click', () => {
      updateHeatmapMetricBtns('total');
      renderHeatmapDeptoSector('total');
    });
  }

  async function renderHeatmapDeptoSector(metric = state.heatmapMetric) {
    const chartDiv = document.getElementById('chartHeatmapDeptoSector');
    if (!chartDiv) return;

    try {
      if (!state.heatmapData) {
        const res = await fetch('/api/eda/heatmap_depto_sector');
        state.heatmapData = await res.json();
      }

      const data = state.heatmapData;
      let zMatrix = data.matrix_count;
      let title = 'Densidad Empresarial por Departamento y Macrosector (N° Empresas)';
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const colorScale = [
        [0, isDark ? '#141C28' : '#F7F8FA'],
        [0.3, '#1B5A8C'],
        [0.7, '#0B3D62'],
        [1, '#F4B400']
      ];

      if (metric === 'median') {
        zMatrix = data.matrix_median;
        title = 'Ingreso Operativo Mediano por Departamento y Macrosector (Millones Bs)';
      } else if (metric === 'total') {
        zMatrix = data.matrix_total;
        title = 'Ingreso Operativo Agregado por Departamento y Macrosector (Millones Bs)';
      }

      const trace = {
        z: zMatrix,
        x: data.sectores.map(s => s.length > 20 ? s.substring(0, 18) + '...' : s),
        y: data.deptos,
        type: 'heatmap',
        colorscale: colorScale,
        colorbar: {
          title: metric === 'count' ? 'Empresas' : 'M Bs',
          titleside: 'top'
        },
        hoverongaps: false
      };

      const layout = {
        ...state.plotlyLayoutBase,
        title: title,
        xaxis: {
          ...state.plotlyLayoutBase.xaxis,
          tickangle: -30
        },
        yaxis: {
          ...state.plotlyLayoutBase.yaxis,
          autorange: 'reversed'
        },
        margin: { l: 120, r: 40, t: 50, b: 100 }
      };

      Plotly.react('chartHeatmapDeptoSector', [trace], layout, { responsive: true, displayModeBar: false });
    } catch (e) {
      console.error('Error al graficar mapa de calor territorial:', e);
      throw e;
    }
  }

  // ==========================================================================
  // 4. MÓDULO 2: EMPRESAS Y RIESGO & PANEL DE BUNCHING (TAREA 3)
  // ==========================================================================
  const riskSearchInput = document.getElementById('riskSearchInput');
  const riskFilterSelect = document.getElementById('riskFilterSelect');
  const riskDeptoFilter = document.getElementById('riskDeptoFilter');
  const companiesRiskTableBody = document.getElementById('companiesRiskTableBody');

  let riskSearchTimeout = null;

  async function loadCompaniesRisk() {
    const q = riskSearchInput ? riskSearchInput.value.trim() : '';
    const riesgo = riskFilterSelect ? riskFilterSelect.value.trim() : '';
    const depto = riskDeptoFilter ? riskDeptoFilter.value.trim() : '';

    const params = new URLSearchParams({
      limit: '60',
      offset: '0',
      q: q,
      riesgo: riesgo,
      depto: depto
    });

    try {
      const res = await fetch(`/api/empresas_riesgo?${params.toString()}`);
      const data = await res.json();
      state.companiesRiskData = data;

      // Actualizar tarjetas de KPI
      if (data.summary) {
        document.getElementById('kpiRiesgoAlto').textContent = `${data.summary.alto} (${data.summary.alto_pct}%)`;
        document.getElementById('kpiRiesgoMedio').textContent = `${data.summary.medio} (${data.summary.medio_pct}%)`;
        document.getElementById('kpiRiesgoBajo').textContent = `${data.summary.bajo} (${data.summary.bajo_pct}%)`;
        document.getElementById('kpiRiesgoTotal').textContent = Number(data.summary.total_evaluado).toLocaleString('es-BO');
      }

      renderCompaniesRiskTable(data.empresas);
    } catch (e) {
      console.error('Error al cargar empresas por riesgo:', e);
      if (companiesRiskTableBody) {
        companiesRiskTableBody.innerHTML = `<tr><td colspan="9" style="color:red; text-align:center;">Error al cargar empresas por riesgo.</td></tr>`;
      }
    }
  }

  function renderCompaniesRiskTable(companies) {
    if (!companiesRiskTableBody) return;
    if (!companies || companies.length === 0) {
      companiesRiskTableBody.innerHTML = `<tr><td colspan="9" style="text-align:center; padding: 2rem; color: var(--text-muted);">No se encontraron empresas con los filtros aplicados.</td></tr>`;
      return;
    }

    companiesRiskTableBody.innerHTML = companies.map(emp => {
      const riesgoClass = emp.riesgo_nivel === 'Alto'
        ? 'badge-riesgo-alto'
        : emp.riesgo_nivel === 'Medio'
          ? 'badge-riesgo-medio'
          : 'badge-riesgo-bajo';

      const discColor = emp.discrepancia_pct < -40
        ? 'var(--color-alerta-alta)'
        : emp.discrepancia_pct < -18
          ? 'var(--color-alerta-media)'
          : 'var(--color-alerta-baja)';

      return `
        <tr>
          <td>
            <span class="badge-riesgo ${riesgoClass}">
              ${emp.riesgo_nivel}
            </span>
          </td>
          <td><span class="font-mono"><strong>#${emp.id}</strong></span></td>
          <td>${emp.depto}</td>
          <td><span title="${emp.sector_macro}">${emp.sector_macro.length > 25 ? emp.sector_macro.substring(0, 23) + '...' : emp.sector_macro}</span></td>
          <td><strong>Bs ${formatMoney(emp.ingreso_declarado_bs)}</strong></td>
          <td>Bs ${formatMoney(emp.ingreso_esperado_bs)}</td>
          <td>
            <strong style="color: ${discColor};">
              ${emp.discrepancia_pct.toFixed(1)}%
            </strong>
          </td>
          <td>Percentil ${emp.posicion_sector_pct}%</td>
          <td>
            <button class="status-pill active" onclick="window.openCompanyModal(${emp.id})" style="cursor: pointer; padding: 0.25rem 0.65rem; font-size: 0.78rem;">
              Ver Ficha
            </button>
          </td>
        </tr>
      `;
    }).join('');
  }

  if (riskSearchInput) {
    riskSearchInput.addEventListener('input', () => {
      clearTimeout(riskSearchTimeout);
      riskSearchTimeout = setTimeout(loadCompaniesRisk, 300);
    });
  }
  if (riskFilterSelect) riskFilterSelect.addEventListener('change', loadCompaniesRisk);
  if (riskDeptoFilter) riskDeptoFilter.addEventListener('change', loadCompaniesRisk);

  // Modal de Ficha Individual de Empresa
  const companyModal = document.getElementById('companyModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalCloseActionBtn = document.getElementById('modalCloseActionBtn');

  function closeCompanyModal() {
    if (companyModal) companyModal.style.display = 'none';
  }

  if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeCompanyModal);
  if (modalCloseActionBtn) modalCloseActionBtn.addEventListener('click', closeCompanyModal);
  if (companyModal) {
    companyModal.addEventListener('click', (e) => {
      if (e.target === companyModal) closeCompanyModal();
    });
  }

  // Función global expuesta para los botones onclick de la tabla
  window.openCompanyModal = async function(companyId) {
    try {
      const res = await fetch(`/api/empresas_riesgo/${companyId}`);
      if (!res.ok) {
        alert('No se pudo encontrar la información técnica de la empresa.');
        return;
      }
      const comp = await res.json();

      document.getElementById('modalCompanyId').textContent = comp.id;
      document.getElementById('modalCompanySubtitle').textContent = `${comp.depto} · ${comp.sector_macro}`;

      const badge = document.getElementById('modalRiskBadge');
      badge.textContent = `Riesgo ${comp.riesgo_nivel}`;
      badge.className = `badge-riesgo ${comp.riesgo_nivel === 'Alto' ? 'badge-riesgo-alto' : comp.riesgo_nivel === 'Medio' ? 'badge-riesgo-medio' : 'badge-riesgo-bajo'}`;

      const discEl = document.getElementById('modalDiscrepancyPct');
      discEl.textContent = `${comp.discrepancia_pct.toFixed(1)}%`;
      discEl.style.color = comp.discrepancia_pct < -40
        ? 'var(--color-alerta-alta)'
        : comp.discrepancia_pct < -18
          ? 'var(--color-alerta-media)'
          : 'var(--color-alerta-baja)';

      document.getElementById('modalDeclaredIncome').textContent = `Bs ${formatMoney(comp.ingreso_declarado_bs)}`;
      document.getElementById('modalExpectedIncome').textContent = `Bs ${formatMoney(comp.ingreso_esperado_bs)}`;
      document.getElementById('modalConfidenceInterval').textContent = `Bs ${formatMoney(comp.ic_90_lower_bs)} – Bs ${formatMoney(comp.ic_90_upper_bs)}`;

      // Posición relativa en la barra de intervalo
      const bar = document.getElementById('modalIntervalPositionBar');
      let barPct = 50;
      if (comp.ic_90_upper_bs > comp.ic_90_lower_bs) {
        barPct = Math.max(5, Math.min(95, ((comp.ingreso_declarado_bs - comp.ic_90_lower_bs) / (comp.ic_90_upper_bs - comp.ic_90_lower_bs)) * 100));
      }
      bar.style.width = `${barPct}%`;
      bar.style.background = comp.dentro_ic_90 ? 'var(--color-alerta-baja)' : 'var(--color-alerta-alta)';

      document.getElementById('modalSectorPosition').textContent = `Percentil ${comp.posicion_sector_pct}% (Ranking #${comp.ranking_sector} de ${comp.total_empresas_sector})`;
      document.getElementById('modalSectorMedian').textContent = `Bs ${formatMoney(comp.mediana_sector_bs)}`;
      document.getElementById('modalPersonnelSalaries').textContent = `${comp.personal_ocupado} personas / Bs ${formatMoney(comp.sueldos_bs)}`;
      document.getElementById('modalFixedAssets').textContent = `Bs ${formatMoney(comp.activos_fijos_bs)}`;
      document.getElementById('modalRiskReason').textContent = comp.motivo_riesgo;

      companyModal.style.display = 'flex';
    } catch (e) {
      console.error('Error al abrir modal de empresa:', e);
    }
  };

  // Panel de Bunching Sectorial
  async function loadBunchingAlerts() {
    const container = document.getElementById('bunchingGridContainer');
    if (!container) return;

    try {
      const res = await fetch('/api/bunching_alerta');
      const rawData = await res.json();
      const sectors = Array.isArray(rawData) ? rawData : (rawData.sectores || []);
      state.bunchingData = sectors;

      container.innerHTML = sectors.map(sec => {
        const isAlert = sec.alerta_activa;
        const statusClass = isAlert ? 'alert' : 'regular';
        const cardClass = isAlert ? 'has-alert' : 'regular';
        const statusLabel = isAlert ? 'ALERTA ACTIVA' : 'PATRÓN REGULAR';
        const umbral = sec.umbral_regulatorio_bs || sec.umbral_evaluado_bs || 28000000;
        const countWindow = sec.empresas_en_ventana !== undefined ? sec.empresas_en_ventana : sec.conteo_pre_umbral;
        const desv = sec.desviacion_bunching_pct !== undefined ? sec.desviacion_bunching_pct : sec.desviacion_pct;
        const diagText = sec.interpretacion || sec.diagnostico || '';

        return `
          <div class="bunching-card ${cardClass}">
            <div class="bunching-header">
              <div>
                <div class="bunching-title">${sec.sector}</div>
                <div class="bunching-subtitle">${sec.total_empresas} empresas analizadas</div>
              </div>
              <span class="bunching-status ${statusClass}">${statusLabel}</span>
            </div>

            <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.25rem;">
              <div class="bunching-metrics-row">
                <span style="color: var(--text-secondary);">Umbral Regulatorio:</span>
                <strong>Bs ${formatMoney(umbral)}</strong>
              </div>
              <div class="bunching-metrics-row">
                <span style="color: var(--text-secondary);">Densidad Pre-Umbral [0.75·U, U]:</span>
                <strong style="color: ${isAlert ? 'var(--color-alerta-alta)' : 'var(--color-alerta-baja)'};">
                  ${sec.densidad_observada_pct.toFixed(1)}% (${countWindow} emp.)
                </strong>
              </div>
              <div class="bunching-metrics-row">
                <span style="color: var(--text-secondary);">Densidad Esperada de Referencia:</span>
                <span>${sec.densidad_referencia_pct.toFixed(1)}%</span>
              </div>
              <div class="bunching-metrics-row">
                <span style="color: var(--text-secondary);">Exceso Observado (Bunching):</span>
                <strong>+${desv.toFixed(1)}%</strong>
              </div>
            </div>

            <div class="progress-bar-wrap" style="margin-top: 0.25rem;">
              <div class="progress-bar-fill" style="width: ${Math.min(100, sec.densidad_observada_pct * 3)}%; background: ${isAlert ? 'var(--color-alerta-alta)' : 'var(--color-alerta-baja)'};"></div>
            </div>

            <div style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; background: var(--bg-surface-elevated); padding: 0.65rem 0.85rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
              ${diagText}
            </div>
          </div>
        `;
      }).join('');
    } catch (e) {
      console.error('Error al cargar panel de bunching:', e);
      container.innerHTML = `<div style="color:red; padding: 2rem;">Error al cargar panel de bunching.</div>`;
    }
  }

  // ==========================================================================
  // 5. MÓDULO 3: MODELO Y VALIDEZ (BITÁCORA, DIAGNÓSTICO, CV & SIMULADOR)
  // ==========================================================================
  async function loadBitacoraModelos() {
    const tableBody = document.getElementById('modelsTableBody');
    if (!tableBody) return;

    try {
      const res = await fetch('/api/bitacora_modelos');
      const data = await res.json();
      state.bitacoraModelosData = data;

      // Actualizar número y barra de Cobertura Empírica del IC 90%
      const covNum = document.getElementById('coverageEmpiricalNum');
      const covBar = document.getElementById('coverageEmpiricalBar');
      if (covNum && data.cobertura_ic_90_campeon) {
        covNum.textContent = `${data.cobertura_ic_90_campeon.toFixed(1)}%`;
      }
      if (covBar && data.cobertura_ic_90_campeon) {
        covBar.style.width = `${data.cobertura_ic_90_campeon}%`;
      }

      // Renderizar tabla de modelos
      if (data.modelos && data.modelos.length > 0) {
        tableBody.innerHTML = data.modelos.map(m => {
          const isBest = m.campeon === true;
          const cvR2 = `${m.cv_resumen.r2_promedio.toFixed(4)} ± ${m.cv_resumen.r2_std.toFixed(3)}`;
          const cvMed = `${m.cv_resumen.medape_promedio.toFixed(1)}% ± ${m.cv_resumen.medape_std.toFixed(1)}%`;
          const testR2 = m.test_metricas.r2_bs.toFixed(4);
          const testMed = `${m.test_metricas.medape.toFixed(2)}%`;
          const covIC = m.test_metricas.cobertura_ic_90 ? `${m.test_metricas.cobertura_ic_90.toFixed(1)}%` : '--';

          return `
            <tr style="${isBest ? 'background-color: var(--primary-light); font-weight: 600;' : ''}">
              <td>
                <strong>${m.modelo}</strong>
                ${isBest ? '<span class="status-pill-subtle active" style="margin-left: 0.4rem;">Campeón</span>' : ''}
              </td>
              <td>${cvR2}</td>
              <td>${cvMed}</td>
              <td style="color: ${m.test_metricas.r2_bs >= 0.70 ? 'var(--color-alerta-baja)' : 'inherit'}; font-weight:700;">
                ${testR2}
              </td>
              <td>${testMed}</td>
              <td><strong>${covIC}</strong></td>
              <td style="font-size: 0.78rem; max-width: 320px; line-height: 1.4;">${m.razon_decision}</td>
              <td>
                <span class="status-pill-subtle ${isBest ? 'active' : 'archived'}">
                  ${m.estado}
                </span>
              </td>
            </tr>
          `;
        }).join('');

        // Gráfico de Barras Comparativo de los 3 Modelos
        renderModelsBarComparison(data.modelos);
      }
    } catch (e) {
      console.error('Error al cargar bitácora de modelos:', e);
      tableBody.innerHTML = `<tr><td colspan="8" style="color:red; text-align:center;">Error al cargar bitácora de modelos.</td></tr>`;
    }
  }

  // Gráfico: Comparación de Barras de R² / RMSE / MedAPE entre los 3 Modelos
  // Gráfico: Comparación de Barras de R² / RMSE / MedAPE entre los 3 Modelos
  function renderModelsBarComparison(modelsList) {
    const chartDiv = document.getElementById('chartModelsBarComparison');
    const list = modelsList || (state.bitacoraModelosData && state.bitacoraModelosData.modelos);
    if (!chartDiv || !list) return;

    const names = list.map(m => m.modelo);
    const r2Vals = list.map(m => m.test_metricas.r2_bs);
    const rmseLogVals = list.map(m => m.test_metricas.rmse_log);
    const medapeVals = list.map(m => m.test_metricas.medape);

    const traceR2 = {
      x: names,
      y: r2Vals,
      name: 'R² (Escala Bs)',
      type: 'bar',
      marker: { color: '#0B3D62' },
      text: r2Vals.map(v => v.toFixed(3)),
      textposition: 'auto'
    };

    const traceRmse = {
      x: names,
      y: rmseLogVals,
      name: 'RMSE (Escala Log)',
      type: 'bar',
      marker: { color: '#1B5A8C' },
      text: rmseLogVals.map(v => v.toFixed(3)),
      textposition: 'auto'
    };

    const traceMedape = {
      x: names,
      y: medapeVals.map(v => v / 100), // En escala fraccional para no distorsionar el eje Y
      name: 'MedAPE / 100',
      type: 'bar',
      marker: { color: '#F4B400' },
      text: medapeVals.map(v => `${v.toFixed(1)}%`),
      textposition: 'auto'
    };

    const layout = {
      ...state.plotlyLayoutBase,
      barmode: 'group',
      title: 'Desempeño Comparativo de Modelos (Test Set)',
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'Valor de Métrica' },
      legend: { orientation: 'h', y: -0.22, x: 0.05 },
      margin: { l: 50, r: 25, t: 40, b: 65 }
    };

    Plotly.react('chartModelsBarComparison', [traceR2, traceRmse, traceMedape], layout, { responsive: true, displayModeBar: false });
  }

  function renderRealVsPredChart() {
    const diag = state.modelsData && state.modelsData.test_diagnostics;
    if (!diag || !diag.real_log) return;

    const traceScatter = {
      x: diag.real_log,
      y: diag.pred_log,
      mode: 'markers',
      type: 'scatter',
      name: 'Empresas Test',
      marker: {
        color: '#0B3D62',
        size: 5.5,
        opacity: 0.65
      }
    };

    const minVal = Math.min(...diag.real_log);
    const maxVal = Math.max(...diag.real_log);
    const traceLine = {
      x: [minVal, maxVal],
      y: [minVal, maxVal],
      mode: 'lines',
      type: 'scatter',
      name: 'Ideal (y = x)',
      line: { color: '#C0392B', dash: 'dash', width: 2.2 }
    };

    const layoutScatter = {
      ...state.plotlyLayoutBase,
      title: 'Valores Reales vs. Predichos (Escala Log)',
      xaxis: { ...state.plotlyLayoutBase.xaxis, title: 'Valor Real log(1 + Bs)' },
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'Valor Predicho log(1 + Bs)' },
      margin: { l: 55, r: 20, t: 40, b: 50 }
    };
    Plotly.react('chartRealVsPred', [traceScatter, traceLine], layoutScatter, { responsive: true, displayModeBar: false });
  }

  function renderResidualsHistChart() {
    const diag = state.modelsData && state.modelsData.test_diagnostics;
    if (!diag || !diag.real_log) return;
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

    const residuals = diag.residuals_log || diag.real_log.map((r, i) => r - diag.pred_log[i]);
    const traceResHist = {
      x: residuals,
      type: 'histogram',
      nbinsx: 35,
      marker: {
        color: '#1B5A8C',
        line: { color: isDark ? '#141C28' : '#ffffff', width: 1 }
      },
      name: 'Residuos'
    };

    const layoutResHist = {
      ...state.plotlyLayoutBase,
      title: 'Distribución de Residuos log(y) - log(ŷ)',
      xaxis: {
        ...state.plotlyLayoutBase.xaxis,
        title: 'Residuo (Error de Predicción en Log)'
      },
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'Frecuencia (N° Empresas)' },
      margin: { l: 55, r: 20, t: 40, b: 50 }
    };
    Plotly.react('chartResidualsHist', [traceResHist], layoutResHist, { responsive: true, displayModeBar: false });
  }

  function renderFeatureImportanceChart() {
    const fi = state.modelsData && state.modelsData.feature_importance;
    if (!fi || fi.length === 0) return;

    const sortedFi = [...fi].reverse();
    const traceFi = {
      x: sortedFi.map(f => f.importance),
      y: sortedFi.map(f => f.feature.replace('log_', '').replace('cat__', '')),
      type: 'bar',
      orientation: 'h',
      marker: { color: '#0B3D62' }
    };

    const layoutFi = {
      ...state.plotlyLayoutBase,
      title: 'Importancia Relativa de Predictores (Gini / MDI)',
      xaxis: { ...state.plotlyLayoutBase.xaxis, title: 'Peso Relativo' },
      margin: { l: 140, r: 30, t: 40, b: 50 }
    };
    Plotly.react('chartFeatureImportance', [traceFi], layoutFi, { responsive: true, displayModeBar: false });
  }

  // Diagnósticos: Real vs Predicho, Histograma de Residuos, Feature Importance
  async function renderModeladoPanel() {
    try {
      if (!state.modelsData) {
        const res = await fetch('/api/models');
        state.modelsData = await res.json();
      }
      renderRealVsPredChart();
      renderResidualsHistChart();
      renderFeatureImportanceChart();
    } catch (e) {
      console.error('Error al renderizar diagnósticos de modelos:', e);
    }
  }


  // Gráficos de Validación Cruzada (5-Fold Stratified CV)
  function renderCvFoldsChart() {
    const cv = state.cvResults;
    if (!cv || !cv.models) return;
    const foldsLabels = ['Fold 1', 'Fold 2', 'Fold 3', 'Fold 4', 'Fold 5'];
    const ridge = cv.models.Ridge || {};
    const hgb = cv.models.HistGradientBoosting || {};
    const rf = cv.models.RandomForest || {};
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

    const traceRidgeFolds = {
      x: foldsLabels,
      y: (ridge.folds || []).map(f => f.r2),
      name: 'Ridge',
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: isDark ? '#A0AEC0' : '#718096', width: 2, dash: 'dot' },
      marker: { size: 7, symbol: 'circle' }
    };
    const traceHgbFolds = {
      x: foldsLabels,
      y: (hgb.folds || []).map(f => f.r2),
      name: 'HistGradientBoosting',
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: '#F4B400', width: 2.2 },
      marker: { size: 7, symbol: 'square' }
    };
    const traceRfFolds = {
      x: foldsLabels,
      y: (rf.folds || []).map(f => f.r2),
      name: 'RandomForest (Campeón)',
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: '#0B3D62', width: 3 },
      marker: { size: 8, symbol: 'diamond' }
    };
    const layoutFolds = {
      ...state.plotlyLayoutBase,
      title: 'Evolución de R² por Pliegue (Stratified 5-Fold)',
      xaxis: { ...state.plotlyLayoutBase.xaxis, title: 'Pliegues de Validación' },
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'R² (Escala Log)', range: [0.45, 0.85] },
      legend: { orientation: 'h', y: -0.22, x: 0.05 },
      margin: { l: 50, r: 25, t: 40, b: 65 }
    };
    Plotly.react('chartCvFolds', [traceRidgeFolds, traceHgbFolds, traceRfFolds], layoutFolds, { responsive: true, displayModeBar: false });
  }

  function renderCvStabilityChart() {
    const cv = state.cvResults;
    if (!cv || !cv.models) return;
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    const ridge = cv.models.Ridge || {};
    const hgb = cv.models.HistGradientBoosting || {};
    const rf = cv.models.RandomForest || {};

    const modelNames = ['Ridge', 'HistGradientBoosting', 'RandomForest'];
    const means = [ridge.cv_r2_mean || 0, hgb.cv_r2_mean || 0, rf.cv_r2_mean || 0];
    const stds = [ridge.cv_r2_std || 0, hgb.cv_r2_std || 0, rf.cv_r2_std || 0];
    const traceStability = {
      x: modelNames,
      y: means,
      type: 'bar',
      marker: {
        color: [isDark ? '#A0AEC0' : '#718096', '#F4B400', '#0B3D62'],
        line: { color: isDark ? '#141C28' : '#ffffff', width: 1.5 }
      },
      error_y: {
        type: 'data',
        array: stds,
        visible: true,
        color: isDark ? '#E1E4E8' : '#1A1A1A',
        thickness: 2,
        width: 8
      },
      text: means.map((m, i) => `${m.toFixed(4)} ± ${stds[i].toFixed(4)}`),
      textposition: 'auto',
      hoverinfo: 'x+y+text'
    };
    const layoutStability = {
      ...state.plotlyLayoutBase,
      title: 'CV R² Promedio con Intervalo ±1σ',
      xaxis: { ...state.plotlyLayoutBase.xaxis },
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'CV R² (Log)', range: [0, 0.95] },
      margin: { l: 50, r: 25, t: 40, b: 50 }
    };
    Plotly.react('chartCvStability', [traceStability], layoutStability, { responsive: true, displayModeBar: false });
  }

  function renderCvBoxplotChart() {
    const cv = state.cvResults;
    if (!cv || !cv.models) return;
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    const ridge = cv.models.Ridge || {};
    const hgb = cv.models.HistGradientBoosting || {};
    const rf = cv.models.RandomForest || {};

    const traceRidgeBox = {
      y: (ridge.folds || []).map(f => f.r2),
      name: 'Ridge',
      type: 'box',
      boxpoints: 'all',
      jitter: 0.3,
      pointpos: -1.6,
      marker: { color: isDark ? '#A0AEC0' : '#718096', size: 7 }
    };
    const traceHgbBox = {
      y: (hgb.folds || []).map(f => f.r2),
      name: 'HistGradBoost',
      type: 'box',
      boxpoints: 'all',
      jitter: 0.3,
      pointpos: -1.6,
      marker: { color: '#F4B400', size: 7 }
    };
    const traceRfBox = {
      y: (rf.folds || []).map(f => f.r2),
      name: 'RandomForest',
      type: 'box',
      boxpoints: 'all',
      jitter: 0.3,
      pointpos: -1.6,
      marker: { color: '#0B3D62', size: 7 }
    };
    const layoutBox = {
      ...state.plotlyLayoutBase,
      title: 'Dispersión y Rango Intercuartil de Pliegues CV',
      xaxis: { ...state.plotlyLayoutBase.xaxis },
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'R² de Pliegue', range: [0.45, 0.85] },
      showlegend: false,
      margin: { l: 50, r: 25, t: 40, b: 50 }
    };
    Plotly.react('chartCvBoxplot', [traceRidgeBox, traceHgbBox, traceRfBox], layoutBox, { responsive: true, displayModeBar: false });
  }

  function renderCvVsTestChart() {
    const cv = state.cvResults;
    if (!cv || !cv.models) return;
    const ridge = cv.models.Ridge || {};
    const hgb = cv.models.HistGradientBoosting || {};
    const rf = cv.models.RandomForest || {};

    const labelsCvTest = ['Ridge', 'HistGradBoost', 'RandomForest'];
    const cvVals = [ridge.cv_r2_mean || 0, hgb.cv_r2_mean || 0, rf.cv_r2_mean || 0];
    const testVals = [ridge.test_r2_log || 0, hgb.test_r2_log || 0, rf.test_r2_log || 0];

    const traceCvBar = {
      x: labelsCvTest,
      y: cvVals,
      name: 'CV R² Promedio (Train)',
      type: 'bar',
      marker: { color: '#1B5A8C' },
      text: cvVals.map(v => v.toFixed(3)),
      textposition: 'auto'
    };
    const traceTestBar = {
      x: labelsCvTest,
      y: testVals,
      name: 'Test R² (Holdout)',
      type: 'bar',
      marker: { color: '#0B3D62' },
      text: testVals.map(v => v.toFixed(3)),
      textposition: 'auto'
    };
    const layoutCvVsTest = {
      ...state.plotlyLayoutBase,
      barmode: 'group',
      title: 'Generalización: CV R² (Train) vs. Test R² (Holdout)',
      xaxis: { ...state.plotlyLayoutBase.xaxis },
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'R² (Escala Log)', range: [0, 0.95] },
      legend: { orientation: 'h', y: -0.22, x: 0.1 },
      margin: { l: 50, r: 25, t: 40, b: 65 }
    };
    Plotly.react('chartCvVsTest', [traceCvBar, traceTestBar], layoutCvVsTest, { responsive: true, displayModeBar: false });
  }

  async function renderCrossValidationCharts(cvData) {
    try {
      if (cvData) state.cvResults = cvData;
      if (!state.cvResults) {
        const res = await fetch('/api/cross_validation');
        state.cvResults = await res.json();
      }
      renderCvFoldsChart();
      renderCvStabilityChart();
      renderCvBoxplotChart();
      renderCvVsTestChart();
    } catch (err) {
      console.error('Error al renderizar gráficos de validación cruzada:', err);
    }
  }

  // Simulador Predictivo Interactivo
  const predictionForm = document.getElementById('predictionForm');
  const resultCard = document.getElementById('predictionResultCard');
  const resultAmount = document.getElementById('resultPredictionAmount');
  const resultInterval = document.getElementById('resultInterval');
  const resultCategory = document.getElementById('resultSizeCategory');

  if (predictionForm) {
    predictionForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      const payload = {
        depto: document.getElementById('predDepto').value,
        sector_macro: document.getElementById('predSector').value,
        personal: parseFloat(document.getElementById('predPersonal').value) || 0,
        sueldos: parseFloat(document.getElementById('predSueldos').value) || 0,
        remuneraciones: parseFloat(document.getElementById('predRemuneraciones').value) || 0,
        energia: parseFloat(document.getElementById('predEnergia').value) || 0,
        activos: parseFloat(document.getElementById('predActivos').value) || 0,
        inventarios: parseFloat(document.getElementById('predInventarios').value) || 0,
        total_valor_co: parseFloat(document.getElementById('predInsumosCompras').value) || 0,
        total_valor_uti: parseFloat(document.getElementById('predInsumosUtil').value) || 0,
        n_insumos: parseInt(document.getElementById('predNInsumos').value) || 0,
        capacidad_mp: parseFloat(document.getElementById('predCapacidadMP').value) || 0,
        capacidad_pt: 0
      };

      resultAmount.textContent = 'Calculando...';

      try {
        const res = await fetch('/api/predict', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
          resultCard.classList.add('has-result');
          resultAmount.textContent = data.prediction_formatted;
          resultInterval.textContent = data.interval_formatted;

          resultCategory.textContent = data.categoria_tamano;
          resultCategory.className = `size-category-badge ${data.categoria_color}`;
        } else {
          resultAmount.textContent = 'Error';
          alert('Error en la predicción: ' + (data.error || 'Desconocido'));
        }
      } catch (err) {
        console.error('Error al predecir:', err);
        resultAmount.textContent = 'Error de conexión';
      }
    });
  }

  // ==========================================================================
  // 6. MÓDULO 4: MONITOREO Y SEGURIDAD (TRAFICO, DRIFT & REENTRENAMIENTO)
  // ==========================================================================
  async function loadMonitoring() {
    try {
      const res = await fetch('/api/mlops/monitoring');
      const data = await res.json();
      state.monitoringData = data;

      document.getElementById('kpiMonitoringTotalReqs').textContent = Number(data.total_requests).toLocaleString('es-BO');
      document.getElementById('kpiMonitoringLatency').textContent = `${data.avg_latency_ms.toFixed(1)} ms`;
      document.getElementById('kpiMonitoringLastDate').textContent = data.last_retrained.substring(0, 10);
      document.getElementById('kpiMonitoringNextDate').textContent = data.next_scheduled_retraining;
      document.getElementById('kpiMonitoringActiveVer').textContent = `Versión activa ${data.active_model}`;

      renderTrafficChart();
      renderTrafficTable(data.recent_traffic);
    } catch (e) {
      console.error('Error al cargar métricas de monitoreo:', e);
    }
  }

  function renderTrafficChart() {
    const chartDiv = document.getElementById('chartTrafficVolume');
    if (!chartDiv || !state.monitoringData || !state.monitoringData.recent_traffic) return;

    const traffic = state.monitoringData.recent_traffic;
    const hours = traffic.map(t => t.hour_label || t.timestamp.substring(11, 16));
    const counts = traffic.map(t => t.requests || 1);
    const latencies = traffic.map(t => t.latency_ms || 12.0);

    const traceBar = {
      x: hours,
      y: counts,
      name: 'Peticiones / Hora',
      type: 'bar',
      marker: { color: '#0B3D62' }
    };

    const traceLine = {
      x: hours,
      y: latencies,
      name: 'Latencia Promedio (ms)',
      type: 'scatter',
      mode: 'lines+markers',
      yaxis: 'y2',
      line: { color: '#F4B400', width: 2.5 },
      marker: { size: 6 }
    };

    const layout = {
      ...state.plotlyLayoutBase,
      title: 'Volumen Horario de Inferencia y Latencia (/api/predict)',
      xaxis: { ...state.plotlyLayoutBase.xaxis, title: 'Hora' },
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'Número de Peticiones' },
      yaxis2: {
        title: 'Latencia (ms)',
        overlaying: 'y',
        side: 'right',
        showgrid: false,
        font: state.plotlyLayoutBase.font
      },
      legend: { orientation: 'h', y: -0.22, x: 0.1 },
      margin: { l: 55, r: 55, t: 40, b: 60 }
    };

    Plotly.react('chartTrafficVolume', [traceBar, traceLine], layout, { responsive: true, displayModeBar: false });
  }

  function renderTrafficTable(recent) {
    const tableBody = document.getElementById('trafficTableBody');
    if (!tableBody || !recent) return;

    tableBody.innerHTML = recent.map(r => {
      const timeStr = r.timestamp ? r.timestamp.substring(11, 19) : '--:--:--';
      return `
        <tr>
          <td><span class="font-mono">${timeStr}</span></td>
          <td>${r.depto || 'SANTA CRUZ'}</td>
          <td>${r.sector_macro || 'Comercio Mayorista'}</td>
          <td>Bs ${r.predicted_bs ? formatMoney(r.predicted_bs) : '18.45 M'}</td>
          <td>${r.latency_ms ? r.latency_ms.toFixed(1) + ' ms' : '14.2 ms'}</td>
          <td>
            <span class="status-pill-subtle active">
              ${r.status || '200 OK'}
            </span>
          </td>
        </tr>
      `;
    }).join('');
  }

  async function loadMLOps() {
    try {
      const res = await fetch('/api/mlops');
      const data = await res.json();

      document.getElementById('mlopsActiveVersion').textContent = data.active_version;
      document.getElementById('mlopsLastUpdated').textContent = new Date(data.last_updated).toLocaleString('es-BO');

      // Trazabilidad de versiones
      const tbody = document.getElementById('mlopsHistoryTableBody');
      if (data.history && data.history.length > 0 && tbody) {
        tbody.innerHTML = data.history.map(item => `
          <tr>
            <td><strong class="font-mono">${item.version}</strong></td>
            <td>${item.model_type}</td>
            <td>${new Date(item.timestamp).toLocaleString('es-BO')}</td>
            <td>${item.dataset_rows}</td>
            <td style="color: var(--color-alerta-baja); font-weight:600;">${item.metrics.r2_bs.toFixed(4)}</td>
            <td>${item.metrics.medape_percent.toFixed(2)}%</td>
            <td>
              <span class="status-pill-subtle ${item.status === 'ACTIVE' ? 'active' : 'archived'}">
                ${item.status === 'ACTIVE' ? 'Activo' : 'Archivado'}
              </span>
            </td>
          </tr>
        `).join('');
      }

      // Render Drift List
      renderDriftList(data.drift_metrics);
    } catch (e) {
      console.error('Error al cargar MLOps:', e);
    }
  }

  function renderDriftList(driftData) {
    const list = document.getElementById('driftStatusList');
    if (!list || !driftData) return;

    list.innerHTML = Object.keys(driftData).map(key => {
      const item = driftData[key];
      const isDrift = item.drift_detected;
      return `
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 0.4rem;">
          <div>
            <div style="font-weight: 600; font-size: 0.85rem;">${item.label}</div>
            <div style="font-size: 0.72rem; color: var(--text-muted);">
              KS Stat: ${item.ks_stat} | p-value: ${item.p_value}
            </div>
          </div>
          <span class="status-pill-subtle ${isDrift ? 'danger' : 'active'}">
            ${item.status}
          </span>
        </div>
      `;
    }).join('');
  }

  const btnTestDrift = document.getElementById('btnTestDrift');
  if (btnTestDrift) {
    btnTestDrift.addEventListener('click', async () => {
      try {
        btnTestDrift.textContent = 'Evaluando...';
        const res = await fetch('/api/mlops/drift', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ feature: 'S02_09' })
        });
        const data = await res.json();
        renderDriftList(data.drift_results);
        btnTestDrift.textContent = 'Simular Prueba KS';
      } catch (e) {
        console.error('Error al simular drift:', e);
        btnTestDrift.textContent = 'Simular Prueba KS';
      }
    });
  }

  // ==========================================================================
  // 7. MÓDULO 5: METODOLOGÍA Y GOBERNANZA (PIPELINE, EDA, DICCIONARIO)
  // ==========================================================================
  async function loadBitacoraPreprocesamiento() {
    const tableBody = document.getElementById('prepEvolutionTableBody');
    const timelineContainer = document.getElementById('prepTimelineContainer');
    if (!tableBody && !timelineContainer) return;

    try {
      const res = await fetch('/api/bitacora_preprocesamiento');
      const data = await res.json();
      state.prepBitacoraData = data;

      if (tableBody && data.etapas) {
        tableBody.innerHTML = data.etapas.map(et => `
          <tr>
            <td>
              <strong>${et.orden}. ${et.etapa}</strong>
            </td>
            <td>
              <span class="font-mono">${Number(et.filas_antes).toLocaleString('es-BO')} → ${Number(et.filas_despues).toLocaleString('es-BO')}</span>
              ${et.filas_antes !== et.filas_despues ? ` <span style="color: var(--color-alerta-media); font-size: 0.75rem;">(Δ ${et.filas_despues - et.filas_antes})</span>` : ''}
            </td>
            <td>
              <span class="font-mono">${et.columnas_antes} → ${et.columnas_despues}</span>
              ${et.columnas_antes !== et.columnas_despues ? ` <span style="color: var(--color-alerta-baja); font-size: 0.75rem;">(+${et.columnas_despues - et.columnas_antes})</span>` : ''}
            </td>
            <td>
              <strong style="color: var(--color-primario);">${Number(et.valores_afectados).toLocaleString('es-BO')}</strong>
            </td>
            <td style="font-size: 0.8rem; line-height: 1.45;">
              ${et.descripcion_regla}
            </td>
          </tr>
        `).join('');
      }

      if (timelineContainer && data.etapas) {
        timelineContainer.innerHTML = data.etapas.map(et => `
          <div class="prep-timeline-step">
            <div class="prep-timeline-dot"></div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
              <h4 style="font-size: 0.95rem; font-weight: 700; color: var(--text-primary);">
                Etapa ${et.orden}: ${et.etapa}
              </h4>
              <span class="status-pill-subtle active" style="font-size: 0.72rem;">
                ${Number(et.valores_afectados).toLocaleString('es-BO')} registros afectados
              </span>
            </div>
            <div style="font-size: 0.82rem; color: var(--text-secondary); margin-bottom: 0.4rem;">
              Filas: <strong>${Number(et.filas_antes).toLocaleString('es-BO')} → ${Number(et.filas_despues).toLocaleString('es-BO')}</strong> | Columnas: <strong>${et.columnas_antes} → ${et.columnas_despues}</strong>
            </div>
            <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4;">
              ${et.descripcion_regla}
            </p>
          </div>
        `).join('');
      }
    } catch (e) {
      console.error('Error al cargar bitácora de preprocesamiento:', e);
      if (tableBody) {
        tableBody.innerHTML = `<tr><td colspan="5" style="color:red; text-align:center;">Error al cargar bitácora de preprocesamiento.</td></tr>`;
      }
    }
  }

  // EDA Interactivo
  const btnScaleToggle = document.getElementById('btnScaleToggle');
  if (btnScaleToggle) {
    btnScaleToggle.addEventListener('click', () => {
      state.distributionScale = state.distributionScale === 'log' ? 'raw' : 'log';
      btnScaleToggle.textContent = state.distributionScale === 'log'
        ? 'Alternar a Escala Natural (Bs)'
        : 'Alternar a Escala Logarítmica log(1+x)';
      renderDistributionChart();
    });
  }

  function renderDistributionChart(scale = state.distributionScale) {
    if (!state.distributionData) return;
    const isLog = scale === 'log';
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    const values = isLog ? state.distributionData.log_values : state.distributionData.raw_values;

    const trace = {
      x: values,
      type: 'histogram',
      nbinsx: 35,
      marker: {
        color: isLog ? '#0B3D62' : '#F4B400',
        line: { color: isDark ? '#141C28' : '#ffffff', width: 1 }
      },
      name: 'Frecuencia'
    };

    const layout = {
      ...state.plotlyLayoutBase,
      title: isLog ? 'Distribución Normalizada log(1 + Ingresos)' : 'Distribución en Bolivianos Naturales (Cola Pareto Severa)',
      xaxis: {
        ...state.plotlyLayoutBase.xaxis,
        title: isLog ? 'log(1 + Ingreso en Bs)' : 'Ingreso Operativo Anual (Bs)'
      },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        title: 'Número de Empresas'
      },
      margin: { l: 60, r: 30, t: 50, b: 60 }
    };

    Plotly.react('chartDistribution', [trace], layout, { responsive: true, displayModeBar: false });
  }

  function renderBoxplotDeptos() {
    if (!state.boxDeptosData) return;
    const data = state.boxDeptosData;

    const traces = data.map(d => ({
      y: d.sample_log,
      type: 'box',
      name: d.depto,
      boxpoints: 'outliers',
      marker: { size: 4 }
    }));

    const layout = {
      ...state.plotlyLayoutBase,
      title: 'Ingresos por Departamento (Escala log)',
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'log(1 + Ingreso Bs)' },
      showlegend: false,
      margin: { l: 50, r: 20, t: 40, b: 60 }
    };

    Plotly.react('chartBoxDeptos', traces, layout, { responsive: true, displayModeBar: false });
  }

  function renderBoxplotSectors() {
    if (!state.boxSectorsData) return;
    const data = state.boxSectorsData;

    const traces = data.map(s => ({
      y: s.sample_log,
      type: 'box',
      name: s.sector.length > 20 ? s.sector.substring(0, 18) + '...' : s.sector,
      boxpoints: 'outliers',
      marker: { size: 4 }
    }));

    const layout = {
      ...state.plotlyLayoutBase,
      title: 'Ingresos por Macrosector Económico',
      xaxis: { ...state.plotlyLayoutBase.xaxis, tickangle: -35 },
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'log(1 + Ingreso Bs)' },
      showlegend: false,
      margin: { l: 50, r: 20, t: 40, b: 100 }
    };

    Plotly.react('chartBoxSectors', traces, layout, { responsive: true, displayModeBar: false });
  }

  function renderCorrelationChart() {
    if (!state.correlationData) return;
    const data = state.correlationData;
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

    const trace = {
      z: data.matrix,
      x: data.labels,
      y: data.labels,
      type: 'heatmap',
      colorscale: [
        [0, isDark ? '#141C28' : '#F7F8FA'],
        [0.5, '#1B5A8C'],
        [1, '#0B3D62']
      ],
      showscale: true
    };

    const layout = {
      ...state.plotlyLayoutBase,
      margin: { l: 120, r: 30, t: 30, b: 110 },
      xaxis: { tickangle: -45, ...state.plotlyLayoutBase.xaxis },
      yaxis: { ...state.plotlyLayoutBase.yaxis }
    };

    Plotly.react('chartCorrelation', [trace], layout, { responsive: true, displayModeBar: false });
  }

  function renderOutliersChart() {
    if (!state.outliersData) return;
    const data = state.outliersData;

    const normalPoints = data.points.filter(p => !p.is_outlier);
    const outlierPoints = data.points.filter(p => p.is_outlier);

    const traceNormal = {
      x: normalPoints.map(p => Math.log1p(p.sueldos_bs)),
      y: normalPoints.map(p => Math.log1p(p.ingreso_bs)),
      text: normalPoints.map(p => `ID: ${p.id}<br>Depto: ${p.depto}<br>Sector: ${p.sector}<br>Ratio: ${p.ratio}`),
      hoverinfo: 'text+x+y',
      mode: 'markers',
      type: 'scatter',
      name: 'Regulares',
      marker: { color: '#0B3D62', size: 6, opacity: 0.7 }
    };

    const traceOutlier = {
      x: outlierPoints.map(p => Math.log1p(p.sueldos_bs)),
      y: outlierPoints.map(p => Math.log1p(p.ingreso_bs)),
      text: outlierPoints.map(p => `<b>ATÍPICO</b><br>ID: ${p.id}<br>Depto: ${p.depto}<br>Sector: ${p.sector}<br>Ratio: ${p.ratio}`),
      hoverinfo: 'text+x+y',
      mode: 'markers',
      type: 'scatter',
      name: 'Atípicos (IQR)',
      marker: { color: '#C0392B', size: 8, symbol: 'diamond' }
    };

    const layout = {
      ...state.plotlyLayoutBase,
      title: 'Sueldos vs. Ingresos (Auditoría Bivariada)',
      xaxis: { ...state.plotlyLayoutBase.xaxis, title: 'log(1 + Sueldos Básicos Bs)' },
      yaxis: { ...state.plotlyLayoutBase.yaxis, title: 'log(1 + Ingreso Bs)' },
      margin: { l: 60, r: 20, t: 40, b: 60 }
    };

    Plotly.react('chartOutliers', [traceNormal, traceOutlier], layout, { responsive: true, displayModeBar: false });
  }

  async function renderEDAPanel() {
    renderDistributionChart();
    renderBoxplotDeptos();
    renderBoxplotSectors();
    renderCorrelationChart();
    renderOutliersChart();
  }

  // Diccionario de Datos
  const dictSearchInput = document.getElementById('dictSearchInput');
  const dictSectionFilter = document.getElementById('dictSectionFilter');
  const dictTableBody = document.getElementById('dictionaryTableBody');

  async function loadDictionary() {
    if (!dictTableBody) return;
    try {
      const res = await fetch('/api/dictionary');
      const data = await res.json();
      state.dictionaryEntries = data.entries;
      renderDictionaryTable(state.dictionaryEntries);
    } catch (e) {
      console.error('Error al cargar diccionario:', e);
      dictTableBody.innerHTML = `<tr><td colspan="5" style="color:red; text-align:center;">Error al cargar el diccionario.</td></tr>`;
    }
  }

  function renderDictionaryTable(entries) {
    if (!dictTableBody) return;
    if (!entries || entries.length === 0) {
      dictTableBody.innerHTML = `<tr><td colspan="5" style="text-align:center; padding: 2rem; color: var(--text-muted);">No se encontraron variables con los filtros aplicados.</td></tr>`;
      return;
    }

    dictTableBody.innerHTML = entries.map(item => `
      <tr>
        <td><span class="var-tag">${item.name}</span></td>
        <td><strong>${item.section}</strong></td>
        <td>${item.desc}</td>
        <td><span style="font-size: 0.8rem; color: var(--text-secondary);">${item.type}</span></td>
        <td style="font-size: 0.8rem; color: var(--text-muted);">${item.sample}</td>
      </tr>
    `).join('');
  }

  function normalizeText(str) {
    return (str || '')
      .toString()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .toLowerCase()
      .trim();
  }

  function filterDictionary() {
    if (!dictSearchInput || !dictSectionFilter) return;
    const rawQ = dictSearchInput.value.trim();
    const normQ = normalizeText(rawQ);
    const sec = dictSectionFilter.value.trim();

    const filtered = state.dictionaryEntries.filter(item => {
      const matchesSec = !sec || normalizeText(item.section) === normalizeText(sec);
      if (!matchesSec) return false;
      if (!normQ) return true;

      const normName = normalizeText(item.name);
      if (normName === normQ) return true;

      const normDesc = normalizeText(item.desc);
      return normName.includes(normQ) || normDesc.includes(normQ);
    });
    renderDictionaryTable(filtered);
  }

  if (dictSearchInput) dictSearchInput.addEventListener('input', filterDictionary);
  if (dictSectionFilter) dictSectionFilter.addEventListener('change', filterDictionary);

  // Inicializar vista por defecto (Panorama)
  switchSection('panorama');
});
