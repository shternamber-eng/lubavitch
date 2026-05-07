/* ── LANGUAGE TOGGLE ──────────────────────────────── */
(function () {
  var lang = localStorage.getItem('lang') || 'en';
  document.documentElement.dataset.lang = lang;

  function setLang(l) {
    lang = l;
    localStorage.setItem('lang', l);
    document.documentElement.dataset.lang = l;
    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      btn.classList.toggle('active', btn.dataset.lang === l);
    });
  }

  document.addEventListener('click', function (e) {
    if (e.target.classList.contains('lang-btn')) {
      setLang(e.target.dataset.lang);
    }
  });

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });
  });
})();

/* ── UTILITIES ────────────────────────────────────── */
const state = {};

function qs(selector, scope = document) {
  return scope.querySelector(selector);
}

function qsa(selector, scope = document) {
  return Array.from(scope.querySelectorAll(selector));
}

async function fetchJSON(path) {
  try {
    const res = await fetch(path);
    return res.ok ? await res.json() : null;
  } catch {
    return null;
  }
}

/* ── NAV ──────────────────────────────────────────── */
function setNavActive() {
  const page = document.body.dataset.page;
  if (!page) return;
  qsa('.navbar-inner a').forEach((link) => {
    const href = link.getAttribute('href') || '';
    if (href.includes(page)) link.classList.add('active-link');
  });
}

function toggleMenu() {
  const button = qs('.nav-toggle');
  const nav = qs('.navbar-inner');
  if (!button || !nav) return;
  button.addEventListener('click', () => {
    nav.classList.toggle('open');
    button.setAttribute('aria-expanded', nav.classList.contains('open'));
  });
}

/* ── RENDER: NEWS PREVIEW (home page) ────────────── */
function renderPreviewCards(items, targetId) {
  const container = qs(targetId);
  if (!container || !items) return;
  container.innerHTML = items.slice(0, 3).map((item) => `
    <article class="news-card">
      <img src="${item.coverImage}" alt="${item.title}" loading="lazy" />
      <div class="card-content">
        <div class="news-meta">
          <span>${item.date}</span>
          <span>${item.category}</span>
        </div>
        <h3>${item.title}</h3>
        <p>${item.excerpt}</p>
        <a class="btn" href="/news/${item.slug}/">Read more</a>
      </div>
    </article>`).join('');
}

/* ── RENDER: SACRED SITES ─────────────────────────── */
function renderSites(cards) {
  const container = qs('#sites-list');
  if (!container || !cards) return;
  container.innerHTML = cards.map((item) => `
    <article class="site-card">
      <img src="${item.image}" alt="${item.title}" loading="lazy" />
      <div class="card-content">
        <div class="site-meta">
          <span>${item.category}</span>
          <span>${item.status}</span>
        </div>
        <h3>${item.title}</h3>
        <p>${item.description}</p>
        <a class="btn" href="/sites/${item.slug}/">View details</a>
      </div>
    </article>`).join('');
}

/* ── RENDER: ARCHIVE ──────────────────────────────── */
function renderArchive(items) {
  const container = qs('#archive-list');
  if (!container || !items) return;
  container.innerHTML = items.map((item) => `
    <article class="archive-card">
      <img src="${item.image}" alt="${item.title}" loading="lazy" />
      <div class="card-content">
        <div class="archive-meta">
          <span>${item.type}</span>
          <span>${item.date}</span>
        </div>
        <h3>${item.title}</h3>
        <p>${item.description}</p>
        <small>${item.credit}</small>
      </div>
    </article>`).join('');
}

/* ── RENDER: RESTORATION TIMELINE ────────────────── */
function renderRestoration(items) {
  const container = qs('#restoration-timeline');
  if (!container || !items) return;
  container.innerHTML = `<div class="timeline">${items.map((item) => `
    <div class="timeline-item">
      <time>${item.date}</time>
      <h3>${item.title}</h3>
      <p>${item.description}</p>
      <small>${item.source}</small>
      <span class="status-badge">${item.status}</span>
    </div>`).join('')}</div>`;
}

/* ── RENDER: GALLERY ──────────────────────────────── */
function createLightbox() {
  const overlay = qs('.lightbox-overlay');
  if (!overlay) return;
  qs('.lightbox-close', overlay)?.addEventListener('click', () => overlay.classList.remove('active'));
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) overlay.classList.remove('active');
  });
}

function showLightbox(item) {
  const overlay = qs('.lightbox-overlay');
  if (!overlay) return;
  qs('.lightbox h3', overlay).textContent = item.title;
  qs('.lightbox img', overlay).src = item.image;
  qs('.lightbox img', overlay).alt = item.alt || item.title;
  qs('.lightbox p', overlay).textContent = item.caption;
  qs('.lightbox small', overlay).textContent = `${item.date} · ${item.location} · ${item.credit}`;
  overlay.classList.add('active');
}

function renderGallery(items) {
  const container = qs('#gallery-grid');
  const filterBar = qs('#gallery-filters');
  if (!container || !items || !filterBar) return;

  const categories = ['All', ...new Set(items.map((i) => i.category))];
  filterBar.innerHTML = categories.map((cat) =>
    `<button type="button" class="filter-button${cat === 'All' ? ' active' : ''}" data-category="${cat}">${cat}</button>`
  ).join('');

  function updateGrid(cat = 'All') {
    const sel = cat === 'All' ? items : items.filter((i) => i.category === cat);
    container.innerHTML = sel.map((item) => `
      <article class="gallery-item" data-id="${item.id}" tabindex="0">
        <img src="${item.image}" alt="${item.alt}" loading="lazy" />
        <div class="gallery-info">
          <h3>${item.title}</h3>
          <p>${item.date} · ${item.location}</p>
        </div>
      </article>`).join('');

    qsa('.gallery-item').forEach((card) => {
      const open = () => {
        const found = items.find((i) => i.id === card.dataset.id);
        if (found) showLightbox(found);
      };
      card.addEventListener('click', open);
      card.addEventListener('keydown', (e) => { if (e.key === 'Enter') open(); });
    });
  }

  filterBar.addEventListener('click', (e) => {
    const btn = e.target.closest('button');
    if (!btn) return;
    qsa('.filter-button').forEach((b) => b.classList.remove('active'));
    btn.classList.add('active');
    updateGrid(btn.dataset.category);
  });

  updateGrid();
}

/* ── RENDER: NEWS LIST ────────────────────────────── */
function renderNewsList(items) {
  const container = qs('#news-list');
  const searchInput = qs('#news-search');
  const categorySelect = qs('#news-category');
  if (!container || !items) return;

  const categories = ['All', ...new Set(items.map((i) => i.category))];
  if (categorySelect) {
    categorySelect.innerHTML = categories.map((cat) =>
      `<option value="${cat}">${cat}</option>`).join('');
  }

  function updateList() {
    const query = (searchInput?.value || '').toLowerCase();
    const category = categorySelect?.value || 'All';
    const filtered = items.filter((item) => {
      const matchCat = category === 'All' || item.category === category;
      const matchQ = item.title.toLowerCase().includes(query) || item.excerpt.toLowerCase().includes(query);
      return matchCat && matchQ;
    });
    container.innerHTML = filtered.map((item) => `
      <article class="news-card">
        <img src="${item.coverImage}" alt="${item.title}" loading="lazy" />
        <div class="card-content">
          <div class="news-meta">
            <span>${item.date}</span>
            <span>${item.category}</span>
          </div>
          <h3>${item.title}</h3>
          <p>${item.excerpt}</p>
          <a class="btn" href="/news/${item.slug}/">Read more</a>
        </div>
      </article>`).join('');
  }

  searchInput?.addEventListener('input', updateList);
  categorySelect?.addEventListener('change', updateList);
  updateList();
}

/* ── RENDER: NEWS DETAIL ──────────────────────────── */
function renderNewsDetail(items) {
  const slug = location.pathname.split('/').filter(Boolean).pop();
  const item = items?.find((e) => e.slug === slug);
  if (!item) return;
  const container = qs('#news-detail');
  if (!container) return;
  container.innerHTML = `
    <article class="news-card">
      <img src="${item.coverImage}" alt="${item.title}" loading="lazy" />
      <div class="card-content">
        <div class="news-meta">
          <span>${item.date}</span>
          <span>${item.category}</span>
          <span>${item.author}</span>
        </div>
        <h1>${item.title}</h1>
        <p>${item.excerpt}</p>
        <div>${item.body}</div>
        <div class="page-note"><strong>Source note:</strong> ${item.sources}</div>
      </div>
    </article>`;
}

/* ── RENDER: HISTORY TIMELINE ─────────────────────── */
function renderHistoryTimeline() {
  const container = qs('#history-timeline');
  if (!container) return;
  container.innerHTML = `
    <div class="timeline">
      <div class="timeline-item"><time>c. 1813</time><h3>Chabad Court Moves to Lubavitch</h3><p>The Mitteler Rebbe establishes Lubavitch as the seat of Chabad, giving the movement its enduring name.</p></div>
      <div class="timeline-item"><time>1813 – 1866</time><h3>The Tzemach Tzedek</h3><p>Rabbi Menachem Mendel Schneerson leads Chabad from Lubavitch, writing thousands of responsa and building the movement's institutions.</p></div>
      <div class="timeline-item"><time>1897</time><h3>Tomchei Temimim Founded</h3><p>The Rebbe Rashab establishes the first yeshiva combining Talmud and Chassidus study, setting the model for all Chabad education.</p></div>
      <div class="timeline-item"><time>1915 – 1916</time><h3>The Court Departs</h3><p>World War I forces the Rebbe Rashab to relocate the court from Lubavitch to Rostov-on-Don, ending 102 years of Chabad leadership in the village.</p></div>
      <div class="timeline-item"><time>August 1941</time><h3>Nazi Occupation</h3><p>German forces occupy Lubavitch. On November 4, 1941, 483 Jews of the village are murdered.</p></div>
      <div class="timeline-item"><time>1989</time><h3>Restoration Begins</h3><p>With the opening of the Soviet Union, the Lubavitcher Rebbe directs and funds the first modern renovation of the Ohel. A permanent Chabad presence is re-established in the village.</p></div>
      <div class="timeline-item"><time>2000s – today</time><h3>Ongoing Restoration</h3><p>Rabbi Gavriel Gordon and the Geder Avos organization systematically restore the cemetery, rebuild the shul, and document the village's history.</p></div>
    </div>`;
}

/* ── INIT ─────────────────────────────────────────── */
function init() {
  setNavActive();
  toggleMenu();
  createLightbox();

  const page = document.body.dataset.page;
  if (!page) return;

  if (page === 'history') {
    renderHistoryTimeline();
  }

  const promises = [
    fetchJSON('/data/news.json'),
    fetchJSON('/data/gallery.json'),
    fetchJSON('/data/restoration.json'),
    fetchJSON('/data/sacredSites.json'),
    fetchJSON('/data/archive.json'),
  ];

  Promise.all(promises).then(([news, gallery, restoration, sites, archive]) => {
    state.news = news || [];
    state.gallery = gallery || [];
    state.restoration = restoration || [];
    state.sites = sites || [];
    state.archive = archive || [];

    if (page === 'home') renderPreviewCards(state.news, '#latest-updates');
    if (page === 'sacred-sites') renderSites(state.sites);
    if (page === 'restoration') renderRestoration(state.restoration);
    if (page === 'gallery') renderGallery(state.gallery);
    if (page === 'news') renderNewsList(state.news);
    if (page === 'news-detail') renderNewsDetail(state.news);
    if (page === 'archive') renderArchive(state.archive);
  });
}

window.addEventListener('DOMContentLoaded', init);
