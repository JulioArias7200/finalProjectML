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
  // ESTADO GLOBAL DE LA APLICACIÓN Y SISTEMA DE PERSISTENCIA JSON
  // ==========================================================================
  const STORAGE_KEY = 'dashboard_session_state_v1';

  const SessionStateManager = {
    loadState() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw ? JSON.parse(raw) : null;
      } catch (e) {
        console.warn('Error al leer sesión de localStorage:', e);
        return null;
      }
    },

    saveState(partial) {
      try {
        const current = this.loadState() || {
          active_section: 'panorama',
          active_subtabs: {
            'modelo_validez': 'mv-diagnostico',
            'monitoreo': 'mon-trafico',
            'gobernanza': 'gob-pipeline'
          },
          simulator: null,
          drift: null,
          filters: {
            risk_search: '',
            risk_level: '',
            risk_depto: '',
            analysis_search: '',
            analysis_phase: ''
          },
          chart_toggles: {
            heatmap_metric: 'count',
            distribution_scale: 'log'
          }
        };

        const updated = {
          ...current,
          ...partial,
          active_subtabs: {
            ...current.active_subtabs,
            ...(partial.active_subtabs || {})
          },
          filters: {
            ...current.filters,
            ...(partial.filters || {})
          },
          chart_toggles: {
            ...current.chart_toggles,
            ...(partial.chart_toggles || {})
          }
        };

        localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
        return updated;
      } catch (e) {
        console.warn('Error al guardar sesión en localStorage:', e);
      }
    },

    updateHash(section, subtab) {
      try {
        if (!section) return;
        const targetHash = subtab ? `#${section}/${subtab}` : `#${section}`;
        if (window.location.hash !== targetHash) {
          history.replaceState(null, '', targetHash);
        }
      } catch (e) {
        // Ignorar restricciones en entornos aislados
      }
    },

    parseHash() {
      try {
        const hash = (window.location.hash || '').replace(/^#\/?/, '').trim();
        if (!hash) return null;
        const parts = hash.split('/');
        return {
          section: parts[0] || null,
          subtab: parts[1] || null
        };
      } catch (e) {
        return null;
      }
    },

    clearState() {
      try {
        localStorage.removeItem(STORAGE_KEY);
      } catch (e) {}
    }
  };

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
    comparativaBaselineData: null,
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
    chartComparativaMedape: {
      endpoint: '/api/comparativa_baseline',
      stateProp: 'comparativaBaselineData',
      render: () => renderComparativaMedapeChart()
    },
    chartComparativaR2: {
      endpoint: '/api/comparativa_baseline',
      stateProp: 'comparativaBaselineData',
      render: () => renderComparativaR2Chart()
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

  // Obtención compartida con deduplicación: una sola petición en vuelo por
  // endpoint y caché de sesión. Evita dobles fetch (y el parpadeo asociado)
  // cuando varios consumidores —tabla y gráfico— piden el mismo recurso.
  window.fetchShared = function(url, force = false) {
    const key = url.split('?')[0];
    const cache = state._endpointCache || (state._endpointCache = {});
    const inflight = state._inflight || (state._inflight = {});
    if (!force && cache[key]) return Promise.resolve(cache[key]);
    if (!force && inflight[key]) return inflight[key];
    const p = fetch(url).then(async (res) => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json();
    }).then((data) => {
      cache[key] = data;
      return data;
    });
    inflight[key] = p;
    const done = () => { delete inflight[key]; };
    p.then(done, done);
    return p;
  };

  window.reloadChart = async function(chartId, force = true) {
    const cfg = chartsRegistry[chartId];
    if (!cfg) return;

    if (chartsLoading[chartId]) return;
    chartsLoading[chartId] = true;

    const loadingEl = document.getElementById(`loading-${chartId}`);
    const errorEl = document.getElementById(`error-${chartId}`);
    const btn = document.querySelector(`.chart-refresh-btn[data-chart="${chartId}"]`);

    const needsFetch = force || !state[cfg.stateProp];
    // ¿Habrá petición de red real? Solo entonces se muestra el overlay: con
    // datos en caché (o uniéndose a una petición en vuelo) el gráfico se
    // redibuja sin parpadeo visible.
    const cache = state._endpointCache || (state._endpointCache = {});
    const inflight = state._inflight || (state._inflight = {});
    const willFetch = needsFetch && !cache[cfg.endpoint] && !inflight[cfg.endpoint];

    if (willFetch && loadingEl) loadingEl.style.display = 'flex';
    if (errorEl) errorEl.style.display = 'none';
    if (btn) btn.classList.add('spinning');

    try {
      if (needsFetch) {
        const url = force ? `${cfg.endpoint}?_t=${Date.now()}` : cfg.endpoint;
        state[cfg.stateProp] = await fetchShared(url, force);
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
    },
    'bitacora_analisis': {
      title: 'Bitácora de Análisis del Proyecto',
      sub: 'Trazabilidad integral, auditoría de calidad de datos, benchmark y MLOps'
    }
  };

  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.getAttribute('data-section');
      switchSection(target, null, true);
    });
  });

  function switchSubtab(parentPanel, subtabTarget, saveState = true) {
    if (!parentPanel || !subtabTarget) return;

    const sectionId = parentPanel.id.replace('panel-', '');

    // Actualizar botones del subnav en este panel
    parentPanel.querySelectorAll('.subnav-tab-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-subtab') === subtabTarget);
    });

    // Ocultar todos los subtab-contents y mostrar el seleccionado
    parentPanel.querySelectorAll('[id^="subtab-content-"]').forEach(content => {
      if (content.id === `subtab-content-${subtabTarget}`) {
        content.style.display = 'block';
      } else {
        content.style.display = 'none';
      }
    });

    if (saveState) {
      SessionStateManager.saveState({
        active_subtabs: { [sectionId]: subtabTarget }
      });
      SessionStateManager.updateHash(sectionId, subtabTarget);
    }

    // Refrescar tamaño de gráficos Plotly
    setTimeout(() => window.dispatchEvent(new Event('resize')), 100);

    // Carga diferida según subtab
    if (subtabTarget === 'mv-cv') {
      Promise.all([
        reloadChart('chartCvFolds', false),
        reloadChart('chartCvStability', false),
        reloadChart('chartCvBoxplot', false),
        reloadChart('chartCvVsTest', false)
      ]);
    } else if (subtabTarget === 'mv-comparativa') {
      loadComparativaBaseline();
    } else if (subtabTarget === 'gob-eda') {
      Promise.all([
        reloadChart('chartDistribution', false),
        reloadChart('chartBoxDeptos', false),
        reloadChart('chartBoxSectors', false),
        reloadChart('chartCorrelation', false),
        reloadChart('chartOutliers', false)
      ]);
    } else if (subtabTarget === 'gob-pipeline') {
      loadBitacoraPreprocesamiento();
      loadDatasetMetadata();
      loadDatasetLineage();
    } else if (subtabTarget === 'gob-diccionario' && state.dictionaryEntries.length === 0) {
      loadDictionary();
    }
  }

  function switchSection(sectionId, targetSubtab = null, saveState = true) {
    state.activeSection = sectionId;

    navBtns.forEach(b => b.classList.toggle('active', b.getAttribute('data-section') === sectionId));
    panels.forEach(p => p.classList.toggle('active', p.id === `panel-${sectionId}`));

    const meta = titlesMap[sectionId] || { title: 'Dashboard', sub: '' };
    sectionTitle.textContent = meta.title;
    sectionSubtitle.textContent = meta.sub;

    const panel = document.getElementById(`panel-${sectionId}`);
    let activeSubtab = targetSubtab;

    if (panel) {
      const subnavBtns = panel.querySelectorAll('.subnav-tab-btn');
      if (subnavBtns.length > 0) {
        if (!activeSubtab) {
          const savedState = SessionStateManager.loadState();
          activeSubtab = savedState?.active_subtabs?.[sectionId] || subnavBtns[0].getAttribute('data-subtab');
        }
        switchSubtab(panel, activeSubtab, false);
      }
    }

    if (saveState) {
      SessionStateManager.saveState({
        active_section: sectionId,
        ...(activeSubtab ? { active_subtabs: { [sectionId]: activeSubtab } } : {})
      });
      SessionStateManager.updateHash(sectionId, activeSubtab);
    }

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
      Promise.all([
        loadBitacoraModelos(),
        reloadChart('chartRealVsPred', false),
        reloadChart('chartResidualsHist', false),
        reloadChart('chartModelsBarComparison', false),
        reloadChart('chartFeatureImportance', false)
      ]);
      if (activeSubtab === 'mv-cv') {
        Promise.all([
          reloadChart('chartCvFolds', false),
          reloadChart('chartCvStability', false),
          reloadChart('chartCvBoxplot', false),
          reloadChart('chartCvVsTest', false)
        ]);
      } else if (activeSubtab === 'mv-comparativa') {
        loadComparativaBaseline();
      }
    } else if (sectionId === 'monitoreo') {
      loadMLOps();
      Promise.all([
        loadMonitoring(),
        reloadChart('chartTrafficVolume', false)
      ]);
    } else if (sectionId === 'gobernanza') {
      loadBitacoraPreprocesamiento();
      loadDatasetMetadata();
      loadDatasetLineage();
      if (activeSubtab === 'gob-eda') {
        Promise.all([
          reloadChart('chartDistribution', false),
          reloadChart('chartBoxDeptos', false),
          reloadChart('chartBoxSectors', false),
          reloadChart('chartCorrelation', false),
          reloadChart('chartOutliers', false)
        ]);
      } else if (activeSubtab === 'gob-diccionario' && state.dictionaryEntries.length === 0) {
        loadDictionary();
      }
    } else if (sectionId === 'bitacora_analisis') {
      loadBitacoraAnalisis();
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
      switchSubtab(parentPanel, subtabTarget, true);
    });
  });

  // ==========================================================================
  // 3. MÓDULO 1: PANORAMA GENERAL & HEATMAP DEPTO X SECTOR
  // ==========================================================================
  async function loadKPIs() {
    try {
      const res = await fetch('/api/kpis');
      if (!res.ok) {
        console.warn('API /api/kpis respondió con código:', res.status);
        return;
      }
      const data = await res.json();
      if (!data || data.error) {
        console.warn('API /api/kpis retornó error:', data?.error, data?.detalle);
        return;
      }
      if (data.total_empresas !== undefined && document.getElementById('kpiTotalEmpresas')) {
        document.getElementById('kpiTotalEmpresas').textContent = Number(data.total_empresas).toLocaleString('es-BO');
      }
      if (data.ingreso_mediano !== undefined && document.getElementById('kpiIngresoMediano')) {
        document.getElementById('kpiIngresoMediano').textContent = `Bs ${(Number(data.ingreso_mediano) / 1e6).toFixed(2)} M`;
      }
      if (data.ingreso_promedio !== undefined && document.getElementById('kpiIngresoPromedio')) {
        document.getElementById('kpiIngresoPromedio').textContent = `Bs ${(Number(data.ingreso_promedio) / 1e6).toFixed(2)} M`;
      }
      if (data.num_departamentos !== undefined && document.getElementById('kpiDeptos')) {
        document.getElementById('kpiDeptos').textContent = `${data.num_departamentos} Deptos`;
      }
    } catch (e) {
      console.error('Error al cargar KPIs:', e);
    }
  }
  // Nota: los KPIs se cargan desde switchSection('panorama') al final de la
  // inicialización. Una llamada aquí provocaba una segunda petición
  // redundante a /api/kpis en cada carga de la página.

  const btnHeatmapMetricCount = document.getElementById('btnHeatmapMetricCount');
  const btnHeatmapMetricMedian = document.getElementById('btnHeatmapMetricMedian');
  const btnHeatmapMetricTotal = document.getElementById('btnHeatmapMetricTotal');

  function updateHeatmapMetricBtns(activeMetric, saveState = true) {
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

    if (saveState) {
      SessionStateManager.saveState({
        chart_toggles: { heatmap_metric: activeMetric }
      });
    }
  }

  if (btnHeatmapMetricCount) {
    btnHeatmapMetricCount.addEventListener('click', () => {
      updateHeatmapMetricBtns('count', true);
      renderHeatmapDeptoSector('count');
    });
  }
  if (btnHeatmapMetricMedian) {
    btnHeatmapMetricMedian.addEventListener('click', () => {
      updateHeatmapMetricBtns('median', true);
      renderHeatmapDeptoSector('median');
    });
  }
  if (btnHeatmapMetricTotal) {
    btnHeatmapMetricTotal.addEventListener('click', () => {
      updateHeatmapMetricBtns('total', true);
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

    SessionStateManager.saveState({
      filters: {
        risk_search: q,
        risk_level: riesgo,
        risk_depto: depto
      }
    });

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
            <span class="badge-riesgo ${riesgoClass}" title="Señal descriptiva de discrepancia frente a la estructura productiva; no constituye acusación individual">
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
            <button class="status-pill active" onclick="window.openCompanyModal(${emp.id})" style="cursor: pointer; padding: 0.25rem 0.65rem; font-size: 0.78rem;" title="Detalle individual sujeto a la política D04">
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
      if (res.status === 403) {
        const body = await res.json().catch(() => ({}));
        alert(body.detalle || 'El detalle individual está restringido por la política de acceso D04 (entrega pública agregada).');
        return;
      }
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
      const data = await window.fetchShared('/api/bitacora_modelos');
      state.bitacoraModelosData = data;

      // Actualizar número y barra de cobertura del intervalo conformal (D02)
      const covNum = document.getElementById('coverageEmpiricalNum');
      const covBar = document.getElementById('coverageEmpiricalBar');
      const covNota = document.getElementById('coverageEmpiricalNota');
      const cobertura = data.cobertura_ic_90_campeon || (data.modelos || []).find(m => m.campeon)?.test_metricas?.cobertura_ic_90;
      if (covNum && cobertura) {
        covNum.textContent = `${Number(cobertura).toFixed(1)}%`;
      }
      if (covBar && cobertura) {
        covBar.style.width = `${Math.min(100, Number(cobertura))}%`;
      }
      if (covNota && cobertura) {
        const dentro = Number(cobertura) >= 85 && Number(cobertura) <= 95;
        covNota.textContent = dentro
          ? `✓ Dentro de la tolerancia predefinida [85%, 95%] → intervalo etiquetable como 90% calibrado`
          : `⚠ Fuera de la tolerancia [85%, 95%] → NO etiquetar como intervalo 90% calibrado`;
        covNota.style.color = dentro ? 'var(--color-alerta-baja)' : 'var(--color-alerta-alta)';
      }

      // Renderizar tabla de modelos
      if (data.modelos && data.modelos.length > 0) {
        tableBody.innerHTML = data.modelos.map(m => {
          const isBest = m.campeon === true;
          const cvR2 = `${m.cv_resumen.r2_promedio.toFixed(4)} ± ${m.cv_resumen.r2_std.toFixed(3)}`;
          const cvMed = `${m.cv_resumen.medape_promedio.toFixed(1)}% ± ${m.cv_resumen.medape_std.toFixed(1)}%`;
          const testR2 = m.test_metricas.r2_bs.toFixed(4);
          const testMed = `${m.test_metricas.medape.toFixed(2)}%`;
          const covIC = m.test_metricas.cobertura_ic_90 != null ? `${m.test_metricas.cobertura_ic_90.toFixed(1)}%` : '--';

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
  // Gráfico: Comparación de Barras de R² / RMSE / MedAPE entre los 3 Modelos
  function renderModelsBarComparison(modelsList) {
    const chartDiv = document.getElementById('chartModelsBarComparison');
    const list = modelsList || (state.bitacoraModelosData && state.bitacoraModelosData.modelos);
    if (!chartDiv || !list) return;

    const names = list.map(m => String(m.modelo));
    const r2Vals = list.map(m => Number(m.test_metricas?.r2_bs || 0));
    const rmseLogVals = list.map(m => Number(m.test_metricas?.rmse_log || 0));
    const medapeVals = list.map(m => Number(m.test_metricas?.medape || 0));

    const traceR2 = {
      x: names,
      y: r2Vals,
      name: 'R² (Escala Bs)',
      type: 'bar',
      marker: { color: '#0B3D62' },
      text: r2Vals.map(v => v.toFixed(3)),
      textposition: 'auto',
      hovertemplate: 'R²(Bs): %{y:.3f}<extra></extra>'
    };

    const traceRmse = {
      x: names,
      y: rmseLogVals,
      name: 'RMSE (Escala Log)',
      type: 'bar',
      marker: { color: '#1B5A8C' },
      text: rmseLogVals.map(v => v.toFixed(3)),
      textposition: 'auto',
      hovertemplate: 'RMSE(log): %{y:.3f}<extra></extra>'
    };

    const traceMedape = {
      x: names,
      y: medapeVals,
      name: 'MedAPE (%)',
      type: 'bar',
      yaxis: 'y2',
      marker: { color: '#F4B400' },
      text: medapeVals.map(v => `${v.toFixed(1)}%`),
      textposition: 'auto',
      hovertemplate: 'MedAPE: %{y:.2f}%<extra></extra>'
    };

    const layout = {
      ...state.plotlyLayoutBase,
      barmode: 'group',
      title: 'Desempeño Comparativo de Modelos (Test Set)',
      xaxis: { ...state.plotlyLayoutBase.xaxis, type: 'category' },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        title: 'R² (Bs) / RMSE (log)',
        type: 'linear',
        range: [0, 1.0],
        dtick: 0.2,
        tickformat: '.2f'
      },
      yaxis2: {
        title: 'MedAPE (%)',
        type: 'linear',
        overlaying: 'y',
        side: 'right',
        range: [0, 100],
        dtick: 20,
        tickformat: '.0f',
        showgrid: false,
        zeroline: false
      },
      legend: { orientation: 'h', y: -0.22, x: 0.05 },
      margin: { l: 55, r: 55, t: 40, b: 65 }
    };

    Plotly.react('chartModelsBarComparison', [traceR2, traceRmse, traceMedape], layout, { responsive: true, displayModeBar: false });
  }

  function renderRealVsPredChart() {
    const diag = state.modelsData && state.modelsData.test_diagnostics;
    if (!diag || !diag.real_log) return;

    const realLog = diag.real_log.map(Number);
    const predLog = diag.pred_log.map(Number);

    const traceScatter = {
      x: realLog,
      y: predLog,
      mode: 'markers',
      type: 'scatter',
      name: 'Empresas Test',
      marker: {
        color: '#0B3D62',
        size: 5.5,
        opacity: 0.65
      }
    };

    const minVal = Math.min(...realLog);
    const maxVal = Math.max(...realLog);
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
      xaxis: {
        ...state.plotlyLayoutBase.xaxis,
        title: 'Valor Real log(1 + Bs)',
        type: 'linear',
        dtick: 1,
        tickformat: '.1f'
      },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        title: 'Valor Predicho log(1 + Bs)',
        type: 'linear',
        dtick: 1,
        tickformat: '.1f'
      },
      margin: { l: 55, r: 20, t: 40, b: 50 }
    };
    Plotly.react('chartRealVsPred', [traceScatter, traceLine], layoutScatter, { responsive: true, displayModeBar: false });
  }

  function renderResidualsHistChart() {
    const diag = state.modelsData && state.modelsData.test_diagnostics;
    if (!diag || !diag.real_log) return;
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

    const realLog = diag.real_log.map(Number);
    const predLog = diag.pred_log.map(Number);
    const residuals = (diag.residuals_log ? diag.residuals_log.map(Number) : realLog.map((r, i) => r - predLog[i]));

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
        title: 'Residuo log(y) - log(ŷ)',
        type: 'linear',
        dtick: 0.5,
        tickformat: '.1f'
      },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        title: 'Frecuencia (N° Empresas)',
        type: 'linear',
        tickformat: 'd'
      },
      margin: { l: 55, r: 20, t: 40, b: 50 }
    };
    Plotly.react('chartResidualsHist', [traceResHist], layoutResHist, { responsive: true, displayModeBar: false });
  }

  function renderFeatureImportanceChart() {
    const fi = state.modelsData && state.modelsData.feature_importance;
    if (!fi || fi.length === 0) return;

    const sortedFi = [...fi].reverse();
    const cleanNames = sortedFi.map(f => {
      let name = String(f.feature).replace('log_', '').replace('cat__', '');
      return name;
    });
    const xVals = sortedFi.map(f => Number(f.importance));

    const traceFi = {
      x: xVals,
      y: cleanNames,
      type: 'bar',
      orientation: 'h',
      marker: { color: '#0B3D62' },
      text: xVals.map(v => `${(v * 100).toFixed(1)}%`),
      textposition: 'auto',
      hovertemplate: '%{y}: %{x:.2%}<extra></extra>'
    };

    const maxImportance = Math.max(...xVals, 0.35);

    const layoutFi = {
      ...state.plotlyLayoutBase,
      title: 'Importancia Relativa de Predictores (Gini / MDI)',
      xaxis: {
        ...state.plotlyLayoutBase.xaxis,
        title: 'Peso Relativo de Importancia',
        type: 'linear',
        tickformat: '.0%',
        range: [0, maxImportance * 1.15]
      },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        type: 'category',
        automargin: true
      },
      margin: { l: 220, r: 35, t: 40, b: 50 }
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
    const cohortNote = cv.cohorte
      ? ` · CV sobre bloque de ajuste n=${cv.cohorte.n_entrenamiento_ajuste}`
      : '';
    const foldsLabels = ['Fold 1', 'Fold 2', 'Fold 3', 'Fold 4', 'Fold 5'];
    const ridge = cv.models.Ridge || {};
    const hgb = cv.models.HistGradientBoosting || {};
    const rf = cv.models.RandomForest || {};
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

    const traceRidgeFolds = {
      x: foldsLabels,
      y: (ridge.folds || []).map(f => Number(f.r2)),
      name: 'Ridge',
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: isDark ? '#A0AEC0' : '#718096', width: 2, dash: 'dot' },
      marker: { size: 7, symbol: 'circle' }
    };
    const traceHgbFolds = {
      x: foldsLabels,
      y: (hgb.folds || []).map(f => Number(f.r2)),
      name: 'HistGradientBoosting',
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: '#F4B400', width: 2.2 },
      marker: { size: 7, symbol: 'square' }
    };
    const traceRfFolds = {
      x: foldsLabels,
      y: (rf.folds || []).map(f => Number(f.r2)),
      name: 'RandomForest (Campeón)',
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: '#0B3D62', width: 3 },
      marker: { size: 8, symbol: 'diamond' }
    };
    const layoutFolds = {
      ...state.plotlyLayoutBase,
      title: `Evolución de R² por Pliegue (Stratified 5-Fold)${cohortNote}`,
      xaxis: { ...state.plotlyLayoutBase.xaxis, type: 'category', title: 'Pliegues de Validación' },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        title: 'R² (Escala Log)',
        type: 'linear',
        range: [0.45, 0.85],
        dtick: 0.05,
        tickformat: '.2f'
      },
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
    const means = [Number(ridge.cv_r2_mean || 0), Number(hgb.cv_r2_mean || 0), Number(rf.cv_r2_mean || 0)];
    const stds = [Number(ridge.cv_r2_std || 0), Number(hgb.cv_r2_std || 0), Number(rf.cv_r2_std || 0)];
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
      xaxis: { ...state.plotlyLayoutBase.xaxis, type: 'category' },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        title: 'CV R² (Log)',
        type: 'linear',
        range: [0, 0.95],
        dtick: 0.1,
        tickformat: '.2f'
      },
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
      y: (ridge.folds || []).map(f => Number(f.r2)),
      name: 'Ridge',
      type: 'box',
      boxpoints: 'all',
      jitter: 0.3,
      pointpos: -1.6,
      marker: { color: isDark ? '#A0AEC0' : '#718096', size: 7 }
    };
    const traceHgbBox = {
      y: (hgb.folds || []).map(f => Number(f.r2)),
      name: 'HistGradBoost',
      type: 'box',
      boxpoints: 'all',
      jitter: 0.3,
      pointpos: -1.6,
      marker: { color: '#F4B400', size: 7 }
    };
    const traceRfBox = {
      y: (rf.folds || []).map(f => Number(f.r2)),
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
      xaxis: { ...state.plotlyLayoutBase.xaxis, type: 'category' },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        title: 'R² de Pliegue',
        type: 'linear',
        range: [0.45, 0.85],
        dtick: 0.05,
        tickformat: '.2f'
      },
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
    const cvVals = [Number(ridge.cv_r2_mean || 0), Number(hgb.cv_r2_mean || 0), Number(rf.cv_r2_mean || 0)];
    const testVals = [Number(ridge.test_r2_log || 0), Number(hgb.test_r2_log || 0), Number(rf.test_r2_log || 0)];

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
      xaxis: { ...state.plotlyLayoutBase.xaxis, type: 'category' },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        title: 'R² (Escala Log)',
        type: 'linear',
        range: [0, 0.95],
        dtick: 0.1,
        tickformat: '.2f'
      },
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

  // ==========================================================================
  // CUADRO COMPARATIVO: DATOS SIN ENTRENAR VS MODELOS ML
  // ==========================================================================
  async function loadComparativaBaseline() {
    try {
      const res = await fetch('/api/comparativa_baseline');
      const data = await res.json();
      state.comparativaBaselineData = data;

      // Actualizar KPIs si existen
      if (data.kpis_mejora) {
        const kpiError = document.getElementById('comp-kpi-error-reduc');
        const kpiR2 = document.getElementById('comp-kpi-r2-bs');
        const kpiDuan = document.getElementById('comp-kpi-duan');
        const kpiFalsos = document.getElementById('comp-kpi-falsos-pos');

        if (kpiError) kpiError.textContent = `-${data.kpis_mejora.reduccion_medape_vs_mco_pct}%`;
        if (kpiR2) kpiR2.textContent = `+${data.kpis_mejora.ganancia_varianza_r2_bs_pct}%`;
        if (kpiDuan) kpiDuan.textContent = `Ŝ = ${data.kpis_mejora.factor_duan_smearing}`;
        if (kpiFalsos) kpiFalsos.textContent = `${data.kpis_mejora.tasa_falsos_positivos_actual_pct}%`;
      }

      // Renderizar tabla
      const tbody = document.getElementById('tabla-comparativa-baseline-body');
      if (tbody && data.tabla_comparativa) {
        tbody.innerHTML = data.tabla_comparativa.map(row => {
          let badgeClass = 'badge-secondary';
          if (row.estado_badge === 'primary') badgeClass = 'badge-primary';
          else if (row.estado_badge === 'success') badgeClass = 'badge-success';
          else if (row.estado_badge === 'warning') badgeClass = 'badge-warning';
          else if (row.estado_badge === 'danger') badgeClass = 'badge-danger';

          const isChampion = row.estado_badge === 'primary';
          const rowStyle = isChampion ? 'background: rgba(11, 61, 98, 0.08); font-weight: 500;' : '';

          return `
            <tr style="${rowStyle}">
              <td>
                <div style="font-weight: 600; color: var(--text-primary);">${row.enfoque}</div>
                <div style="font-size: 0.78rem; color: var(--text-secondary);">${row.descripcion}</div>
              </td>
              <td><span class="badge ${badgeClass}" style="font-size: 0.72rem;">${row.categoria}</span></td>
              <td style="font-weight: 600; color: ${row.medape_pct <= 40 ? 'var(--success)' : 'var(--danger)'};">
                ${row.medape_pct.toFixed(2)}%
              </td>
              <td style="font-weight: 600;">${row.r2_bs.toFixed(4)}</td>
              <td>${row.r2_log !== undefined ? row.r2_log.toFixed(4) : '--'}</td>
              <td><small>${row.sesgo_jensen}</small></td>
              <td><small>${row.cobertura_ic90}</small></td>
              <td style="color: ${parseFloat(row.tasa_falsos_positivos) <= 20 ? 'var(--success)' : 'var(--danger)'}; font-weight: 600;">
                ${row.tasa_falsos_positivos}
              </td>
              <td>
                <span class="badge ${badgeClass}">${row.estado_texto}</span>
                <div style="font-size: 0.72rem; color: var(--text-secondary); margin-top: 3px;">${row.impacto_empresa}</div>
              </td>
            </tr>
          `;
        }).join('');
      }

      // Renderizar gráficos Plotly
      renderComparativaMedapeChart();
      renderComparativaR2Chart();
    } catch (e) {
      console.error('Error al cargar comparativa baseline vs modelos:', e);
    }
  }

  function renderComparativaMedapeChart() {
    const el = document.getElementById('chartComparativaMedape');
    if (!el || !state.comparativaBaselineData) return;

    const data = state.comparativaBaselineData.graficos_datos;
    const baseTheme = getPlotlyThemeLayout();

    const colors = data.medape_vals.map(v => {
      if (v <= 40) return '#10B981'; // Verde meta cumplida
      if (v <= 75) return '#F59E0B'; // Naranja intermedio
      return '#EF4444'; // Rojo inaceptable
    });

    const traceBars = {
      x: data.modelos,
      y: data.medape_vals,
      type: 'bar',
      marker: {
        color: colors,
        line: { width: 1.5, color: colors }
      },
      text: data.medape_vals.map(v => `${v.toFixed(1)}%`),
      textposition: 'outside',
      cliponaxis: false,
      hoverinfo: 'x+y'
    };

    const layout = {
      ...baseTheme,
      margin: { t: 40, r: 25, b: 85, l: 55 },
      xaxis: {
        ...baseTheme.xaxis,
        tickangle: -20,
        tickfont: { size: 10 }
      },
      yaxis: {
        ...baseTheme.yaxis,
        title: 'MedAPE (%)',
        range: [0, 165]
      },
      shapes: [
        {
          type: 'line',
          x0: -0.5,
          x1: 5.5,
          y0: 40,
          y1: 40,
          line: {
            color: '#EF4444',
            width: 2.5,
            dash: 'dash'
          }
        }
      ],
      annotations: [
        {
          x: 4.8,
          y: 43,
          xref: 'x',
          yref: 'y',
          text: 'Meta Máx. MML: 40%',
          showarrow: false,
          font: { color: '#EF4444', size: 11, weight: 'bold' }
        }
      ]
    };

    Plotly.react('chartComparativaMedape', [traceBars], layout, { responsive: true, displayModeBar: false });
  }

  function renderComparativaR2Chart() {
    const el = document.getElementById('chartComparativaR2');
    if (!el || !state.comparativaBaselineData) return;

    const data = state.comparativaBaselineData.graficos_datos;
    const baseTheme = getPlotlyThemeLayout();

    const colors = data.r2_bs_vals.map(v => {
      if (v >= 0.70) return '#0B3D62'; // Primario campeón
      if (v >= 0.50) return '#3B82F6'; // Azul medio
      return '#94A3B8'; // Gris sin modelo
    });

    const traceBars = {
      x: data.modelos,
      y: data.r2_bs_vals,
      type: 'bar',
      marker: {
        color: colors,
        line: { width: 1.5, color: colors }
      },
      text: data.r2_bs_vals.map(v => v.toFixed(3)),
      textposition: 'outside',
      cliponaxis: false,
      hoverinfo: 'x+y'
    };

    const layout = {
      ...baseTheme,
      margin: { t: 40, r: 25, b: 85, l: 55 },
      xaxis: {
        ...baseTheme.xaxis,
        tickangle: -20,
        tickfont: { size: 10 }
      },
      yaxis: {
        ...baseTheme.yaxis,
        title: 'R² en Escala Monetaria (Bs)',
        range: [0, 0.9]
      },
      shapes: [
        {
          type: 'line',
          x0: -0.5,
          x1: 5.5,
          y0: 0.60,
          y1: 0.60,
          line: {
            color: '#10B981',
            width: 2.5,
            dash: 'dot'
          }
        }
      ],
      annotations: [
        {
          x: 4.8,
          y: 0.63,
          xref: 'x',
          yref: 'y',
          text: 'Meta Mín. MML: 0.60',
          showarrow: false,
          font: { color: '#10B981', size: 11, weight: 'bold' }
        }
      ]
    };

    Plotly.react('chartComparativaR2', [traceBars], layout, { responsive: true, displayModeBar: false });
  }

  // Simulador Predictivo Interactivo
  const predictionForm = document.getElementById('predictionForm');
  const resultCard = document.getElementById('predictionResultCard');
  const resultAmount = document.getElementById('resultPredictionAmount');
  const resultInterval = document.getElementById('resultInterval');
  const resultCategory = document.getElementById('resultSizeCategory');

  function saveSimulatorInputs(result = null) {
    const payload = {
      depto: document.getElementById('predDepto')?.value || 'La Paz',
      sector_macro: document.getElementById('predSector')?.value || 'Industria Manufacturera',
      personal: parseFloat(document.getElementById('predPersonal')?.value) || 0,
      sueldos: parseFloat(document.getElementById('predSueldos')?.value) || 0,
      remuneraciones: parseFloat(document.getElementById('predRemuneraciones')?.value) || 0,
      energia: parseFloat(document.getElementById('predEnergia')?.value) || 0,
      activos: parseFloat(document.getElementById('predActivos')?.value) || 0,
      inventarios: parseFloat(document.getElementById('predInventarios')?.value) || 0,
      total_valor_co: parseFloat(document.getElementById('predInsumosCompras')?.value) || 0,
      total_valor_uti: parseFloat(document.getElementById('predInsumosUtil')?.value) || 0,
      n_insumos: parseInt(document.getElementById('predNInsumos')?.value) || 0
    };

    const current = SessionStateManager.loadState()?.simulator;
    SessionStateManager.saveState({
      simulator: {
        payload: payload,
        result: result !== null ? result : (current?.result || null)
      }
    });
  }

  function restoreSimulatorState(savedSim) {
    if (!savedSim) return;
    if (savedSim.payload) {
      const p = savedSim.payload;
      const setVal = (id, val) => {
        const el = document.getElementById(id);
        if (el && val !== undefined && val !== null) el.value = val;
      };
      setVal('predDepto', p.depto);
      setVal('predSector', p.sector_macro);
      setVal('predPersonal', p.personal);
      setVal('predSueldos', p.sueldos);
      setVal('predRemuneraciones', p.remuneraciones);
      setVal('predEnergia', p.energia);
      setVal('predActivos', p.activos);
      setVal('predInventarios', p.inventarios);
      setVal('predInsumosCompras', p.total_valor_co);
      setVal('predInsumosUtil', p.total_valor_uti);
      setVal('predNInsumos', p.n_insumos);
    }
    if (savedSim.result && savedSim.result.success && resultCard) {
      resultCard.classList.add('has-result');
      if (resultAmount) resultAmount.textContent = savedSim.result.prediction_formatted;
      if (resultInterval) resultInterval.textContent = `${savedSim.result.interval_formatted} · ${savedSim.result.interval_label || ''}`;
      if (resultCategory) {
        resultCategory.textContent = savedSim.result.categoria_tamano;
        resultCategory.className = `size-category-badge ${savedSim.result.categoria_color}`;
      }
    }
  }

  if (predictionForm) {
    predictionForm.querySelectorAll('input, select').forEach(inp => {
      inp.addEventListener('input', () => saveSimulatorInputs());
      inp.addEventListener('change', () => saveSimulatorInputs());
    });

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
        n_insumos: parseInt(document.getElementById('predNInsumos').value) || 0
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
          resultInterval.textContent = `${data.interval_formatted} · ${data.interval_label || ''}`;

          resultCategory.textContent = data.categoria_tamano;
          resultCategory.className = `size-category-badge ${data.categoria_color}`;
          saveSimulatorInputs(data);
        } else if (res.status === 400) {
          resultAmount.textContent = 'Entrada inválida';
          resultInterval.textContent = data.detalle || 'Revise los valores ingresados.';
        } else if (res.status === 503) {
          resultAmount.textContent = 'Servicio en preparación';
          resultInterval.textContent = 'El paquete de modelo no está disponible temporalmente (503).';
        } else {
          resultAmount.textContent = 'Error';
          resultInterval.textContent = data.detalle || data.error || 'Error desconocido';
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

      // A10: sin tráfico real se muestra 'sin telemetría', nunca métricas simuladas
      const sinTelemetria = data.status === 'SIN TELEMETRÍA' || !Array.isArray(data.recent_traffic) || data.recent_traffic.length === 0;
      document.getElementById('kpiMonitoringTotalReqs').textContent = sinTelemetria ? 'Sin telemetría' : Number(data.total_requests).toLocaleString('es-BO');
      document.getElementById('kpiMonitoringLatency').textContent = sinTelemetria ? '—' : `${Number(data.avg_latency_ms).toFixed(1)} ms`;
      document.getElementById('kpiMonitoringLastDate').textContent = (data.last_retrained || '').substring(0, 10);
      document.getElementById('kpiMonitoringNextDate').textContent = data.next_scheduled_retraining || '—';
      document.getElementById('kpiMonitoringActiveVer').textContent = `Versión activa ${data.active_model || '—'}`;

      if (sinTelemetria) {
        try { Plotly.purge('chartTrafficVolume'); } catch (err) { /* contenedor aún sin gráfico */ }
      } else {
        renderTrafficChart();
        renderTrafficTable(data.recent_traffic);
      }
    } catch (e) {
      console.error('Error al cargar métricas de monitoreo:', e);
    }
  }

  function renderTrafficChart() {
    const chartDiv = document.getElementById('chartTrafficVolume');
    if (!chartDiv || !state.monitoringData || !state.monitoringData.recent_traffic) return;

    const traffic = state.monitoringData.recent_traffic;
    const hours = traffic.map(t => String(t.hour_label || (t.timestamp ? t.timestamp.substring(11, 16) : '--:--')));
    const counts = traffic.map(t => Number(t.requests || 1));
    const latencies = traffic.map(t => Number(t.latency_ms || 12.0));

    const traceBar = {
      x: hours,
      y: counts,
      name: 'Peticiones / Hora',
      type: 'bar',
      marker: { color: '#3B82F6', opacity: 0.85 }
    };

    const traceLine = {
      x: hours,
      y: latencies,
      name: 'Latencia Promedio (ms)',
      type: 'scatter',
      mode: 'lines+markers',
      yaxis: 'y2',
      line: { color: '#F4B400', width: 2.5 },
      marker: { size: 7, color: '#F4B400' }
    };

    const layout = {
      ...state.plotlyLayoutBase,
      title: 'Volumen Horario de Inferencia y Latencia (/api/predict)',
      xaxis: { ...state.plotlyLayoutBase.xaxis, type: 'category', title: 'Hora' },
      yaxis: {
        ...state.plotlyLayoutBase.yaxis,
        title: 'Número de Peticiones',
        type: 'linear',
        rangemode: 'tozero',
        dtick: 1,
        tickformat: 'd'
      },
      yaxis2: {
        title: 'Latencia (ms)',
        type: 'linear',
        overlaying: 'y',
        side: 'right',
        rangemode: 'tozero',
        dtick: 2,
        tickformat: '.1f',
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
          <td>${r.latency_ms ? Number(r.latency_ms).toFixed(1) + ' ms' : '14.2 ms'}</td>
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

      document.getElementById('mlopsActiveVersion').textContent = data.active_version || '—';
      document.getElementById('mlopsModelType').textContent = data.model_type || '—';
      document.getElementById('mlopsSmearingFactor').textContent = data.smearing_factor == null ? '—' : Number(data.smearing_factor).toFixed(4);
      document.getElementById('mlopsLastUpdated').textContent = data.last_updated ? new Date(data.last_updated).toLocaleString('es-BO') : '—';

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
      const savedState = SessionStateManager.loadState();
      if (savedState?.drift) {
        renderDriftList(savedState.drift);
      } else if (data.drift_demostracion) {
        renderDriftList(data.drift_demostracion);
      } else {
        renderDriftList(data.drift_metrics);
      }
    } catch (e) {
      console.error('Error al cargar MLOps:', e);
    }
  }

  function renderDriftList(driftData) {
    const list = document.getElementById('driftStatusList');
    if (!list || !driftData) return;

    const validKeys = Object.keys(driftData).filter(key => {
      const item = driftData[key];
      return !key.startsWith('__') && key !== 'ventana_horas' && item && typeof item === 'object' && (item.label || item.status || item.ks_stat !== undefined);
    });

    if (validKeys.length === 0) {
      list.innerHTML = `
        <div style="padding: 1.5rem; color: var(--text-muted); text-align: center; font-size: 0.85rem;">
          No hay datos de deriva disponibles. Haga clic en <strong>Simular Prueba KS</strong> para evaluar variables.
        </div>
      `;
      return;
    }

    list.innerHTML = validKeys.map(key => {
      const item = driftData[key];
      const isDrift = item.drift_detected || item.status === 'DRIFT DETECTADO';
      const isSinDatos = item.status === 'SIN DATOS';
      const label = item.label || key;
      const statusText = item.status || (isDrift ? 'DRIFT DETECTADO' : 'ESTABLE');
      const badgeClass = isDrift ? 'danger' : isSinDatos ? 'archived' : 'active';
      const ksInfo = item.ks_stat !== undefined && item.p_value !== undefined
        ? `KS Stat: ${item.ks_stat} | p-value: ${item.p_value}`
        : item.n_produccion !== undefined
          ? `Muestras en producción: ${item.n_produccion} (requiere ≥ 30)`
          : 'Monitoreo de distribución';

      return `
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding: 0.55rem 0;">
          <div>
            <div style="font-weight: 600; font-size: 0.85rem; color: var(--text-primary);">${label}</div>
            <div style="font-size: 0.72rem; color: var(--text-muted);">
              ${ksInfo}
            </div>
          </div>
          <span class="status-pill-subtle ${badgeClass}">
            ${statusText}
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
          body: JSON.stringify({ feature: 'S02_09', modo: 'simulado' })
        });
        const data = await res.json();
        renderDriftList(data.drift_results);
        SessionStateManager.saveState({ drift: data.drift_results });
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

  // --------------------------------------------------------------------------
  // CARGA DE METADATOS CRIPTOGRÁFICOS DE LOS ARCHIVOS DEL CORPUS
  // --------------------------------------------------------------------------
  async function loadDatasetMetadata() {
    const container = document.getElementById('metadataCardsContainer');
    if (!container) return;

    try {
      const res = await fetch('/api/dataset/metadata');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      state.datasetMetadata = data;

      const datasets = data.datasets || {};
      const prim = datasets.primary;
      const sec = datasets.secondary;
      const proc = datasets.processed;

      if (!prim || !sec || !proc) return;

      container.innerHTML = `
        <!-- CARD 1: DATASET PRIMARIO -->
        <div class="metadata-file-card card-primary">
          <div>
            <div class="meta-header-row">
              <span class="status-pill-subtle" style="background: rgba(2, 132, 199, 0.12); color: #0284C7; font-weight: 700;">
                📘 DATASET PRIMARIO
              </span>
              <span class="status-pill-subtle active" style="font-size: 0.72rem;">${prim.quality_status}</span>
            </div>
            <div class="meta-file-title">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>
              Base Maestra General
            </div>
            <div class="meta-filename-code">${prim.filename}</div>

            <table class="meta-metrics-table">
              <tr><td class="meta-label">Registros:</td><td class="meta-val">${Number(prim.rows).toLocaleString('es-BO')} empresas</td></tr>
              <tr><td class="meta-label">Columnas:</td><td class="meta-val">${prim.columns} variables censales</td></tr>
              <tr><td class="meta-label">Tamaño en Disco:</td><td class="meta-val">${prim.size_human}</td></tr>
              <tr><td class="meta-label">Clave Relacional:</td><td class="meta-val"><strong style="color: #0284C7;">${prim.key}</strong></td></tr>
            </table>

            <div class="meta-hash-container">
              <span class="meta-hash-text" title="${prim.sha256}">SHA-256: ${prim.sha256.substring(0, 16)}...</span>
              <button class="btn-copy-hash" data-hash="${prim.sha256}" title="Copiar hash SHA-256">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                Copiar
              </button>
            </div>

            <div class="meta-quality-note note-optimo">
              <strong>Nota de Integridad:</strong> ${prim.quality_note}
            </div>
          </div>

          <button class="btn-inspect-schema" data-target="primary">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            Ver Esquema de Variables (167)
          </button>
        </div>

        <!-- CARD 2: DATASET SECUNDARIO -->
        <div class="metadata-file-card card-secondary">
          <div>
            <div class="meta-header-row">
              <span class="status-pill-subtle" style="background: rgba(234, 88, 12, 0.12); color: #EA580C; font-weight: 700;">
                📙 DATASET SECUNDARIO
              </span>
              <span class="status-pill-subtle" style="background: rgba(234, 88, 12, 0.15); color: #EA580C; font-size: 0.72rem; font-weight: 600;">${sec.quality_status}</span>
            </div>
            <div class="meta-file-title">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#EA580C" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
              Insumos y Materias Primas
            </div>
            <div class="meta-filename-code">${sec.filename}</div>

            <table class="meta-metrics-table">
              <tr><td class="meta-label">Registros Físicos:</td><td class="meta-val">${Number(sec.rows_physical).toLocaleString('es-BO')} líneas</td></tr>
              <tr><td class="meta-label">Registros Válidos:</td><td class="meta-val">${Number(sec.rows_valid).toLocaleString('es-BO')} útiles</td></tr>
              <tr><td class="meta-label">Columnas:</td><td class="meta-val">${sec.columns} campos de insumo</td></tr>
              <tr><td class="meta-label">Tamaño en Disco:</td><td class="meta-val">${sec.size_human}</td></tr>
              <tr><td class="meta-label">Clave Relacional:</td><td class="meta-val"><strong style="color: #EA580C;">${sec.key}</strong></td></tr>
            </table>

            <div class="meta-hash-container">
              <span class="meta-hash-text" title="${sec.sha256}">SHA-256: ${sec.sha256.substring(0, 16)}...</span>
              <button class="btn-copy-hash" data-hash="${sec.sha256}" title="Copiar hash SHA-256">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                Copiar
              </button>
            </div>

            <div class="meta-quality-note note-saneado">
              <strong>Alerta de Saneamiento:</strong> ${sec.quality_note}
            </div>
          </div>

          <button class="btn-inspect-schema" data-target="secondary">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            Ver Esquema de Insumos (8)
          </button>
        </div>

        <!-- CARD 3: DATASET PROCESADO -->
        <div class="metadata-file-card card-processed">
          <div>
            <div class="meta-header-row">
              <span class="status-pill-subtle" style="background: rgba(16, 185, 129, 0.12); color: #10B981; font-weight: 700;">
                📗 DATASET PROCESADO
              </span>
              <span class="status-pill-subtle active" style="font-size: 0.72rem;">${proc.quality_status}</span>
            </div>
            <div class="meta-file-title">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              Matriz Consolidada Inmutable
            </div>
            <div class="meta-filename-code">${proc.filename}</div>

            <table class="meta-metrics-table">
              <tr><td class="meta-label">Registros Finales:</td><td class="meta-val">${Number(proc.rows).toLocaleString('es-BO')} empresas</td></tr>
              <tr><td class="meta-label">Columnas Totales:</td><td class="meta-val">${proc.columns} predictores & target</td></tr>
              <tr><td class="meta-label">Tamaño en Disco:</td><td class="meta-val">${proc.size_human}</td></tr>
              <tr><td class="meta-label">Clave Relacional:</td><td class="meta-val"><strong style="color: #10B981;">${proc.key}</strong></td></tr>
            </table>

            <div class="meta-hash-container">
              <span class="meta-hash-text" title="${proc.sha256}">SHA-256: ${proc.sha256.substring(0, 16)}...</span>
              <button class="btn-copy-hash" data-hash="${proc.sha256}" title="Copiar hash SHA-256">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                Copiar
              </button>
            </div>

            <div class="meta-quality-note note-certificado">
              <strong>Gobernanza:</strong> ${proc.quality_note}
            </div>
          </div>

          <button class="btn-inspect-schema" data-target="processed">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            Ver Esquema Consolidado (184)
          </button>
        </div>
      `;

      // Eventos de botones Copiar Hash
      container.querySelectorAll('.btn-copy-hash').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
          const hashVal = btn.getAttribute('data-hash');
          if (navigator.clipboard && hashVal) {
            navigator.clipboard.writeText(hashVal).then(() => {
              const prevHTML = btn.innerHTML;
              btn.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> ¡Copiado!`;
              btn.style.color = '#10B981';
              btn.style.borderColor = '#10B981';
              setTimeout(() => {
                btn.innerHTML = prevHTML;
                btn.style.color = '';
                btn.style.borderColor = '';
              }, 2000);
            });
          }
        });
      });

      // Eventos de Ver Esquema
      container.querySelectorAll('.btn-inspect-schema').forEach(btn => {
        btn.addEventListener('click', () => {
          const targetKey = btn.getAttribute('data-target');
          openSchemaModal(targetKey, datasets[targetKey]);
        });
      });

    } catch (e) {
      console.error('Error al cargar metadatos de datasets:', e);
      if (container) {
        container.innerHTML = `<div style="color: red; padding: 1.5rem; text-align: center; grid-column: 1 / -1;">Error al cargar metadatos de los archivos fuente.</div>`;
      }
    }
  }

  function openSchemaModal(targetKey, fileData) {
    const modal = document.getElementById('modalDatasetSchema');
    const modalTitle = document.getElementById('modalSchemaTitle');
    const modalBody = document.getElementById('modalSchemaBody');
    if (!modal || !modalTitle || !modalBody || !fileData) return;

    modalTitle.textContent = `Esquema de Variables: ${fileData.filename} (${fileData.role})`;

    const sampleCols = fileData.sample_columns || [];
    let colsHtml = `
      <div style="margin-bottom: 1rem; font-size: 0.88rem; color: var(--text-secondary);">
        Archivo con <strong>${fileData.columns} columnas</strong> y <strong>${Number(fileData.rows).toLocaleString('es-BO')} registros</strong>.
        Clave: <strong style="color: var(--primary);">${fileData.key}</strong>.
      </div>
      <div class="custom-table-container">
        <table class="custom-table" style="font-size: 0.82rem;">
          <thead>
            <tr>
              <th style="width: 50px;">#</th>
              <th>Nombre de Columna</th>
              <th>Rol / Naturaleza</th>
              <th>Descripción Metodológica</th>
            </tr>
          </thead>
          <tbody>
    `;

    sampleCols.forEach((col, idx) => {
      let desc = 'Variable censal del módulo anual EAIMCS.';
      let rol = 'Predictor';
      if (col === 'ID') { desc = 'Identificador único inmutable de la empresa.'; rol = 'Llave Primaria'; }
      else if (col === 'target' || col === 'S00_01_A') { desc = 'Ingreso Operativo Anual declarado (Variable Objetivo).'; rol = 'Target'; }
      else if (col.startsWith('log1p_')) { desc = 'Transformación estabilizadora ln(1+x).'; rol = 'Predictor log1p'; }
      else if (col === 'depto') { desc = 'Departamento geográfico de operación.'; rol = 'Categórica'; }
      else if (col === 'sector_macro') { desc = 'Macrosector de actividad normalizado según CAEB.'; rol = 'Categórica'; }
      else if (col === 'n_insumos') { desc = 'Diversidad total de materias primas reportadas.'; rol = 'Ingeniería N:1'; }
      else if (col.startsWith('total_valor_')) { desc = 'Consumo / compra monetaria agregada de materias primas.'; rol = 'Ingeniería N:1'; }

      colsHtml += `
        <tr>
          <td style="font-family: monospace; color: var(--text-muted);">${idx + 1}</td>
          <td><code style="font-weight: 700; color: var(--primary);">${col}</code></td>
          <td><span class="status-pill-subtle" style="font-size: 0.72rem;">${rol}</span></td>
          <td style="color: var(--text-secondary);">${desc}</td>
        </tr>
      `;
    });

    if (fileData.columns > sampleCols.length) {
      colsHtml += `
        <tr>
          <td colspan="4" style="text-align: center; color: var(--text-muted); padding: 0.75rem; font-style: italic;">
            ... y ${fileData.columns - sampleCols.length} variables adicionales catalogadas en el diccionario completo de datos.
          </td>
        </tr>
      `;
    }

    colsHtml += `
          </tbody>
        </table>
      </div>
    `;

    modalBody.innerHTML = colsHtml;
    modal.style.display = 'flex';
  }

  // Cerrar modal
  const modalSchemaCloseBtn = document.getElementById('modalSchemaCloseBtn');
  const modalDismissBtn = document.getElementById('modalSchemaDismissBtn');
  const modalElem = document.getElementById('modalDatasetSchema');
  if (modalSchemaCloseBtn) modalSchemaCloseBtn.addEventListener('click', () => { modalElem.style.display = 'none'; });
  if (modalDismissBtn) modalDismissBtn.addEventListener('click', () => { modalElem.style.display = 'none'; });
  if (modalElem) {
    modalElem.addEventListener('click', (e) => {
      if (e.target === modalElem) modalElem.style.display = 'none';
    });
  }

  // --------------------------------------------------------------------------
  // CARGA DE ARQUITECTURA EMPRESARIAL INTERACTIVA Y DIAGRAMA SANKEY
  // --------------------------------------------------------------------------
  async function loadDatasetLineage() {
    const archContainer = document.getElementById('archDiagramWrapper');
    const sankeyContainer = document.getElementById('chartDataLineageSankey');
    if (!archContainer && !sankeyContainer) return;

    try {
      const res = await fetch('/api/dataset/lineage');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      state.datasetLineage = data;

      // 1. Renderizar Arquitectura Empresarial Interactiva con Hero Icons
      if (archContainer) {
        archContainer.innerHTML = `
          <div class="arch-layout">
            <!-- ZONA 1: ALMACENAMIENTO CRUDO INE -->
            <div class="arch-perimeter perimeter-raw">
              <span class="arch-perimeter-badge badge-raw-zone">INE RAW STORAGE</span>

              <div class="arch-node-card" data-step="1" id="archNodeDP">
                <div class="arch-hero-icon" style="background: rgba(2, 132, 199, 0.12); color: #0284C7;">
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>
                </div>
                <div class="arch-node-title">DATASET PRIMARIO</div>
                <div class="arch-node-subtitle">
                  <strong>3,153 empresas</strong> (167 cols)<br/>
                  <span style="color: #0284C7; font-weight: 600;">Clave: ID (1:1 Base)</span>
                </div>
              </div>

              <div class="arch-node-card" data-step="1" id="archNodeDS">
                <div class="arch-hero-icon" style="background: rgba(234, 88, 12, 0.12); color: #EA580C;">
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                </div>
                <div class="arch-node-title">DATASET SECUNDARIO</div>
                <div class="arch-node-subtitle">
                  <strong>6,428 líneas</strong> (8 cols)<br/>
                  <span style="color: #EA580C; font-weight: 600;">Clave: ID (N:1 Crudo)</span>
                </div>
              </div>
            </div>

            <!-- ZONA 2: MOTOR DE INTEGRACIÓN Y GOBERNANZA -->
            <div class="arch-perimeter perimeter-engine">
              <span class="arch-perimeter-badge badge-engine-zone">DATA INTEGRATION & GOVERNANCE</span>

              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.85rem;">
                <!-- Saneamiento -->
                <div class="arch-node-card" data-step="2">
                  <div class="arch-hero-icon" style="background: rgba(220, 38, 38, 0.12); color: #DC2626;">
                    <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon></svg>
                  </div>
                  <div class="arch-node-title">SANEAMIENTO</div>
                  <div class="arch-node-subtitle">
                    Exclusión fila 6,429 vacía<br/>
                    <strong style="color: #DC2626;">6,427 útiles</strong> | Negativos a NaN
                  </div>
                </div>

                <!-- Agregación N:1 -->
                <div class="arch-node-card" data-step="3">
                  <div class="arch-hero-icon" style="background: rgba(79, 70, 229, 0.12); color: #4F46E5;">
                    <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                  </div>
                  <div class="arch-node-title">AGREGACIÓN N:1</div>
                  <div class="arch-node-subtitle">
                    Colapso a nivel ID<br/>
                    <strong style="color: #4F46E5;">1,614 empresas fabriles</strong>
                  </div>
                </div>
              </div>

              <!-- Grid de Operaciones Nucleares -->
              <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.65rem; margin-top: 0.5rem;">
                <div class="arch-node-card" data-step="4">
                  <div style="color: #2563EB; font-weight: 700; margin-bottom: 0.25rem;">🔗 Cruce</div>
                  <div style="font-size: 0.72rem; color: var(--text-secondary);">Left Join 3,153</div>
                </div>
                <div class="arch-node-card" data-step="5">
                  <div style="color: #DC2626; font-weight: 700; margin-bottom: 0.25rem;">🛡️ Blindaje</div>
                  <div style="font-size: 0.72rem; color: var(--text-secondary);">-19 vars fuga</div>
                </div>
                <div class="arch-node-card" data-step="6">
                  <div style="color: #16A34A; font-weight: 700; margin-bottom: 0.25rem;">⚡ log1p</div>
                  <div style="font-size: 0.72rem; color: var(--text-secondary);">Homocedasticidad</div>
                </div>
                <div class="arch-node-card" data-step="7">
                  <div style="color: #7C3AED; font-weight: 700; margin-bottom: 0.25rem;">✂️ Muestreo</div>
                  <div style="font-size: 0.72rem; color: var(--text-secondary);">60 / 20 / 20</div>
                </div>
              </div>

              <!-- Bloque Final Procesado -->
              <div class="arch-node-card" data-step="8" style="background: var(--bg-surface); border: 2px solid #10B981; padding: 0.75rem;">
                <div style="display: flex; align-items: center; justify-content: center; gap: 0.5rem;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                  <strong style="color: #10B981; font-size: 0.85rem;">DATASET PROCESADO INMUTABLE (3,153 × 184 cols)</strong>
                </div>
              </div>
            </div>

            <!-- ZONA 3: CONSUMIDORES Y AUDITORÍA -->
            <div class="arch-perimeter perimeter-consumers">
              <span class="arch-perimeter-badge badge-consumers-zone">CONSUMERS</span>

              <div class="arch-node-card" style="cursor: default;">
                <div class="arch-hero-icon" style="background: rgba(249, 115, 22, 0.12); color: #F97316;">
                  <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg>
                </div>
                <div class="arch-node-title" style="font-size: 0.82rem;">API GATEWAY</div>
                <div class="arch-node-subtitle" style="font-family: monospace; font-size: 0.68rem;">/api/lineage</div>
              </div>

              <div class="arch-node-card" style="cursor: default;">
                <div class="arch-hero-icon" style="background: rgba(30, 41, 59, 0.08); color: var(--text-primary);">
                  <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                </div>
                <div class="arch-node-title" style="font-size: 0.82rem;">DASHBOARD</div>
                <div class="arch-node-subtitle">5 Módulos Web<br/><span style="color: #10B981; font-weight: 600;">Inferencia 90%</span></div>
              </div>
            </div>
          </div>
        `;

        // Eventos de clic en nodos de arquitectura para abrir el inspector
        const inspector = document.getElementById('archInspectorPanel');
        archContainer.querySelectorAll('.arch-node-card[data-step]').forEach(card => {
          card.addEventListener('click', () => {
            const stepNum = parseInt(card.getAttribute('data-step'), 10);
            archContainer.querySelectorAll('.arch-node-card').forEach(c => c.classList.remove('active'));
            card.classList.add('active');

            const op = data.operations.find(o => o.step === stepNum);
            if (op && inspector) {
              inspector.style.display = 'block';
              inspector.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.65rem;">
                  <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span class="status-pill-subtle ${op.badge_class}" style="font-weight: 700;">Etapa ${op.step}: ${op.badge}</span>
                    <h4 style="margin: 0; font-size: 1.05rem; font-weight: 700; color: var(--text-primary);">${op.title}</h4>
                  </div>
                  <button id="closeInspectorBtn" style="background: none; border: none; font-size: 1.25rem; cursor: pointer; color: var(--text-muted);">&times;</button>
                </div>
                <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 0.5rem; line-height: 1.45;">
                  <strong>Resumen Operativo:</strong> ${op.summary}
                </p>
                <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 0.75rem; line-height: 1.45;">
                  <strong>Trazabilidad y Calidad:</strong> ${op.details}
                </p>
                <div style="background: var(--bg-surface-elevated); padding: 0.6rem 0.85rem; border-radius: 6px; border: 1px solid var(--border-color); font-family: monospace; font-size: 0.78rem; color: var(--primary);">
                  <strong>Regla de Código / Pipeline:</strong> ${op.rules}
                </div>
              `;

              const closeBtn = document.getElementById('closeInspectorBtn');
              if (closeBtn) closeBtn.addEventListener('click', () => {
                inspector.style.display = 'none';
                card.classList.remove('active');
              });

              inspector.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
          });
        });
      }

      // 2. Renderizar Diagrama Sankey con Plotly.js
      if (sankeyContainer && data.sankey && window.Plotly) {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        const sankeyNodes = data.sankey.nodes;
        const sankeyLinks = data.sankey.links;

        const nodeLabels = sankeyNodes.map(n => n.name);
        const nodeColors = sankeyNodes.map(n => n.color);

        const linkSources = sankeyLinks.map(l => l.source);
        const linkTargets = sankeyLinks.map(l => l.target);
        const linkValues = sankeyLinks.map(l => l.value);
        const linkLabels = sankeyLinks.map(l => l.label);

        const trace = {
          type: "sankey",
          orientation: "h",
          node: {
            pad: 15,
            thickness: 22,
            line: { color: isDark ? "#0F172A" : "#FFFFFF", width: 1 },
            label: nodeLabels,
            color: nodeColors
          },
          link: {
            source: linkSources,
            target: linkTargets,
            value: linkValues,
            label: linkLabels,
            color: linkSources.map(s => {
              const baseColor = nodeColors[s] || "#64748B";
              return baseColor.startsWith('#')
                ? baseColor + '40'
                : 'rgba(100, 116, 139, 0.25)';
            })
          }
        };

        const layout = {
          margin: { l: 20, r: 20, t: 25, b: 25 },
          font: {
            family: "Inter, -apple-system, sans-serif",
            size: 11,
            color: isDark ? "#E2E8F0" : "#1E293B"
          },
          paper_bgcolor: "transparent",
          plot_bgcolor: "transparent"
        };

        Plotly.newPlot(sankeyContainer, [trace], layout, { responsive: true, displayModeBar: false });
      }

    } catch (e) {
      console.error('Error al cargar linaje de dataset:', e);
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
      SessionStateManager.saveState({
        chart_toggles: { distribution_scale: state.distributionScale }
      });
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
      name: d.status === 'suppressed'
        ? `<${d.min_n ?? 5} ▲`
        : `${d.depto.length > 14 ? d.depto.substring(0, 13) + '…' : d.depto} (N=${d.count})`,
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
      // Etiqueta con N y marca de suprimido D05; el nombre completo viaja en hover/texto
      name: s.status === 'suppressed'
        ? `<${s.min_n ?? 5} ▲`
        : `${s.sector.length > 16 ? s.sector.substring(0, 15) + '…' : s.sector} (N=${s.count})`,
      fullSectorName: s.sector,
      customdata: [s.sector, s.status === 'suppressed' ? `N<${s.min_n ?? 5} (suprimido)` : s.count],
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

  // ==========================================================================
  // MÓDULO 6: BITÁCORA DE ANÁLISIS INTEGRAL DEL PROYECTO
  // ==========================================================================
  let analysisLogData = null;

  async function loadBitacoraAnalisis() {
    const timelineContainer = document.getElementById('analysisLogTimelineContainer');
    const qualityBody = document.getElementById('qualityMatrixTableBody');
    const rawViewer = document.getElementById('analysisRawJsonViewer');

    try {
      if (!analysisLogData) {
        const res = await fetch('/api/bitacora_analisis');
        analysisLogData = await res.json();
      }

      // 1. Poblar Metadatos & Resumen
      const meta = analysisLogData.metadatos_auditoria || {};
      const resumen = analysisLogData.resumen_ejecutivo || {};

      const runBadge = document.getElementById('logRunIdBadge');
      const preBadge = document.getElementById('logPreRunIdBadge');
      const genDate = document.getElementById('logGeneratedDate');

      if (runBadge) runBadge.textContent = meta.run_id || '—';
      if (preBadge) preBadge.textContent = meta.preprocessing_run_id || '—';
      if (genDate) genDate.textContent = meta.fecha_generacion ? new Date(meta.fecha_generacion).toLocaleString('es-BO') : '—';

      const elUniverso = document.getElementById('bitKpiUniverso');
      const elModelo = document.getElementById('bitKpiModelo');
      const elDuan = document.getElementById('bitKpiDuan');
      const elConformal = document.getElementById('bitKpiConformal');

      if (elUniverso) elUniverso.textContent = Number(resumen.universo_analizado || 3153).toLocaleString('es-BO');
      if (elModelo) elModelo.textContent = resumen.modelo_campeon ? resumen.modelo_campeon.split(' ')[0] : 'Random Forest';
      if (elDuan) elDuan.textContent = Number(resumen.smearing_factor_duan || 1.04035).toFixed(5);
      if (elConformal) elConformal.textContent = `${Number(resumen.cobertura_conformal_pct || 90.33).toFixed(2)}%`;

      // 2. Renderizar Hitos
      renderAnalysisTimeline(analysisLogData.hitos_analisis || []);

      // 3. Renderizar Matriz de Calidad MML
      renderQualityMatrix(analysisLogData.matriz_control_calidad || []);

      // 4. Renderizar JSON Raw
      if (rawViewer) {
        rawViewer.textContent = JSON.stringify(analysisLogData, null, 2);
      }
    } catch (err) {
      console.error('Error al cargar la bitácora de análisis:', err);
      if (timelineContainer) {
        timelineContainer.innerHTML = `<div class="card" style="text-align:center; color: var(--color-alerta-alta); padding: 2rem;">Error al cargar la bitácora de análisis del proyecto.</div>`;
      }
    }
  }

  function renderAnalysisTimeline(hitos) {
    const container = document.getElementById('analysisLogTimelineContainer');
    if (!container) return;

    if (!hitos || hitos.length === 0) {
      container.innerHTML = `<div class="card" style="text-align:center; padding: 2rem; color: var(--text-muted);">No se encontraron hitos metodológicos con el filtro seleccionado.</div>`;
      return;
    }

    container.innerHTML = hitos.map(h => {
      const badgeClass = `audit-badge-${h.color_badge || 'indigo'}`;
      const findings = (h.hallazgos_estadisticos || []).map(f => `<li>${f}</li>`).join('');
      const formula = h.formula_matematica ? `<div class="audit-formula-box"><strong>Fórmula Matemática:</strong> <code>${h.formula_matematica}</code></div>` : '';
      const decision = h.decisiones_ingenieria ? `<div class="chart-rationale-box" style="margin-top:0.75rem;"><strong>Decisión de Ingeniería:</strong> ${h.decisiones_ingenieria}</div>` : '';

      return `
        <div class="audit-timeline-card">
          <div class="audit-card-header">
            <div class="audit-card-title">
              <span style="color: var(--primary); font-family: monospace;">[${h.id}]</span>
              <span>${h.fase}</span>
            </div>
            <span class="audit-badge ${badgeClass}">${h.estado}</span>
          </div>
          <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.5rem;">
            <span>Responsable: <strong>${h.responsable}</strong></span> · <span>Fecha: ${h.fecha}</span>
          </div>
          <p style="font-size: 0.9rem; color: var(--text-primary); margin-bottom: 0.5rem;">
            ${h.descripcion}
          </p>
          ${findings ? `<ul class="audit-findings-list">${findings}</ul>` : ''}
          ${formula}
          ${decision}
        </div>
      `;
    }).join('');
  }

  function renderQualityMatrix(matriz) {
    const tbody = document.getElementById('qualityMatrixTableBody');
    if (!tbody) return;

    if (!matriz || matriz.length === 0) {
      tbody.innerHTML = `<tr><td colspan="6" style="text-align:center; padding: 2rem; color: var(--text-muted);">No hay registros en la matriz de calidad.</td></tr>`;
      return;
    }

    tbody.innerHTML = matriz.map(m => `
      <tr>
        <td><strong>${m.criterio}</strong></td>
        <td><span class="var-tag">${m.categoria}</span></td>
        <td style="font-size: 0.85rem; color: var(--text-secondary);">${m.meta_esperada}</td>
        <td><strong style="color: var(--color-primario);">${m.valor_obtenido}</strong></td>
        <td><span class="badge-riesgo badge-riesgo-bajo">${m.estado}</span></td>
        <td style="font-size: 0.8rem; font-family: monospace; color: var(--text-muted);">${m.evidencia}</td>
      </tr>
    `).join('');
  }

  // Filtrado de la Línea de Tiempo de Hitos
  const analysisSearchInput = document.getElementById('analysisLogSearchInput');
  const analysisPhaseFilter = document.getElementById('analysisLogPhaseFilter');

  function filterAnalysisTimeline() {
    if (!analysisLogData || !analysisLogData.hitos_analisis) return;
    const q = (analysisSearchInput ? analysisSearchInput.value : '').toLowerCase().trim();
    const phase = (analysisPhaseFilter ? analysisPhaseFilter.value : '').toLowerCase().trim();

    SessionStateManager.saveState({
      filters: {
        analysis_search: q,
        analysis_phase: phase
      }
    });

    const filtered = analysisLogData.hitos_analisis.filter(h => {
      const matchPhase = !phase || (h.fase || '').toLowerCase().includes(phase);
      if (!matchPhase) return false;
      if (!q) return true;

      const fullText = `${h.id} ${h.fase} ${h.descripcion} ${(h.hallazgos_estadisticos || []).join(' ')} ${h.decisiones_ingenieria || ''}`.toLowerCase();
      return fullText.includes(q);
    });

    renderAnalysisTimeline(filtered);
  }

  if (analysisSearchInput) analysisSearchInput.addEventListener('input', filterAnalysisTimeline);
  if (analysisPhaseFilter) analysisPhaseFilter.addEventListener('change', filterAnalysisTimeline);

  // Copiar JSON al portapapeles
  const btnCopyAnalysisJson = document.getElementById('btnCopyAnalysisJson');
  if (btnCopyAnalysisJson) {
    btnCopyAnalysisJson.addEventListener('click', () => {
      if (!analysisLogData) return;
      navigator.clipboard.writeText(JSON.stringify(analysisLogData, null, 2))
        .then(() => {
          const originalText = btnCopyAnalysisJson.textContent;
          btnCopyAnalysisJson.textContent = '¡Copiado!';
          setTimeout(() => btnCopyAnalysisJson.textContent = originalText, 1500);
        })
        .catch(() => alert('No se pudo copiar el JSON'));
    });
  }

  // Exportar JSON
  const btnExportAnalysisLogJson = document.getElementById('btnExportAnalysisLogJson');
  if (btnExportAnalysisLogJson) {
    btnExportAnalysisLogJson.addEventListener('click', () => {
      if (!analysisLogData) return;
      const blob = new Blob([JSON.stringify(analysisLogData, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `bitacora_analisis_${analysisLogData.metadatos_auditoria?.run_id || 'proyecto'}.json`;
      a.click();
      URL.revokeObjectURL(url);
    });
  }

  // Exportar Matriz MML en CSV
  const btnExportQualityMatrixCsv = document.getElementById('btnExportQualityMatrixCsv');
  if (btnExportQualityMatrixCsv) {
    btnExportQualityMatrixCsv.addEventListener('click', () => {
      if (!analysisLogData || !analysisLogData.matriz_control_calidad) return;
      const headers = ['Criterio', 'Categoria', 'Meta Esperada', 'Valor Obtenido', 'Estado', 'Evidencia'];
      const rows = analysisLogData.matriz_control_calidad.map(m => [
        `"${m.criterio.replace(/"/g, '""')}"`,
        `"${m.categoria.replace(/"/g, '""')}"`,
        `"${m.meta_esperada.replace(/"/g, '""')}"`,
        `"${m.valor_obtenido.replace(/"/g, '""')}"`,
        `"${m.estado.replace(/"/g, '""')}"`,
        `"${m.evidencia.replace(/"/g, '""')}"`
      ]);
      const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `matriz_calidad_mml_${analysisLogData.metadatos_auditoria?.run_id || 'proyecto'}.csv`;
      a.click();
      URL.revokeObjectURL(url);
    });
  }

  // ==========================================================================
  // RESTAURACIÓN DE SESIÓN Y ENLACES DIRECTOS (HASH ROUTING)
  // ==========================================================================
  function restoreSessionState() {
    const saved = SessionStateManager.loadState() || {};
    const hash = SessionStateManager.parseHash();

    // 1. Restaurar Filtros
    if (saved.filters) {
      if (riskSearchInput && saved.filters.risk_search) riskSearchInput.value = saved.filters.risk_search;
      if (riskFilterSelect && saved.filters.risk_level) riskFilterSelect.value = saved.filters.risk_level;
      if (riskDeptoFilter && saved.filters.risk_depto) riskDeptoFilter.value = saved.filters.risk_depto;
      if (analysisSearchInput && saved.filters.analysis_search) analysisSearchInput.value = saved.filters.analysis_search;
      if (analysisPhaseFilter && saved.filters.analysis_phase) analysisPhaseFilter.value = saved.filters.analysis_phase;
    }

    // 2. Restaurar Simulador
    if (saved.simulator) {
      restoreSimulatorState(saved.simulator);
    }

    // 3. Restaurar Toggles de Gráficos
    if (saved.chart_toggles) {
      if (saved.chart_toggles.heatmap_metric) {
        state.heatmapMetric = saved.chart_toggles.heatmap_metric;
        updateHeatmapMetricBtns(state.heatmapMetric, false);
      }
      if (saved.chart_toggles.distribution_scale) {
        state.distributionScale = saved.chart_toggles.distribution_scale;
        if (btnScaleToggle) {
          btnScaleToggle.textContent = state.distributionScale === 'log'
            ? 'Alternar a Escala Natural (Bs)'
            : 'Alternar a Escala Logarítmica log(1+x)';
        }
      }
    }

    // 4. Determinar sección y subtab inicial (URL Hash prevalece sobre localStorage)
    const targetSection = hash?.section || saved.active_section || 'panorama';
    const targetSubtab = hash?.subtab || saved?.active_subtabs?.[targetSection] || null;

    switchSection(targetSection, targetSubtab, true);
  }

  // Sincronizar navegación cuando el usuario usa atrás/adelante en el navegador
  window.addEventListener('hashchange', () => {
    const hash = SessionStateManager.parseHash();
    if (hash && hash.section) {
      if (hash.section !== state.activeSection || (hash.subtab && hash.subtab !== SessionStateManager.loadState()?.active_subtabs?.[hash.section])) {
        switchSection(hash.section, hash.subtab, false);
      }
    }
  });

  // Inicializar restaurando estado persistido
  restoreSessionState();
});
