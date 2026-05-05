const state = {};

function qs(selector, scope = document) {
  return scope.querySelector(selector);
}

function qsa(selector, scope = document) {
  return Array.from(scope.querySelectorAll(selector));
}

async function fetchJSON(path) {
  try {
    const response = await fetch(path);
    return response.ok ? await response.json() : null;
  } catch (error) {
    return null;
  }
}

function setNavActive() {
  const page = document.body.dataset.page;
  if (!page) return;
  qsa('.nav-list a').forEach((link) => {
    const href = link.getAttribute('href');
    if (href && href.includes(page)) {
      link.classList.add('active-link');
    }
  });
}

function toggleMenu() {
  const button = qs('.nav-toggle');
  const nav = qs('.nav-list');
  if (!button || !nav) return;
  button.addEventListener('click', () => {
    nav.classList.toggle('open');
    button.setAttribute('aria-expanded', nav.classList.contains('open'));
  });
}

function renderPreviewCards(items, targetId) {
  const container = qs(targetId);
  if (!container || !items) return;
  container.innerHTML = items.slice(0, 3).map((item) => {
    return `
      <article class="news-card">
        <img src="${item.coverImage}" alt="${item.title}" loading="lazy">
        <div class="card-content">
          <div class="news-meta"><span>${item.date}</span><span>${item.category}</span></div>
          <h3>${item.title}</h3>
          <p>${item.excerpt}</p>
          <a class="btn" href="/news/${item.slug}/">Read more</a>
        </div>
      </article>`;
  }).join('');
}

function renderSectionCards(items, targetId) {
  const container = qs(targetId);
  if (!container || !items) return;
  container.innerHTML = items.map((item) => {
    return `
      <article class="card">
        <h3 class="card-strong">${item.title}</h3>
        <p>${item.text}</p>
      </article>`;
  }).join('');
}

function renderSites(cards) {
  const container = qs('#sites-list');
  if (!container || !cards) return;
  container.innerHTML = cards.map((item) => `
    <article class="site-card">
      <img src="${item.image}" alt="${item.title}" loading="lazy">
      <div class="card-content">
        <div class="site-meta"><span>${item.category}</span><span>${item.status}</span></div>
        <h3>${item.title}</h3>
        <p>${item.description}</p>
        <a class="btn" href="/sites/${item.slug}/">View details</a>
      </div>
    </article>
  `).join('');
}

function renderArchive(items) {
  const container = qs('#archive-list');
  if (!container || !items) return;
  container.innerHTML = items.map((item) => `
    <article class="archive-card">
      <img src="${item.image}" alt="${item.title}" loading="lazy">
      <div class="card-content">
        <div class="archive-meta"><span>${item.type}</span><span>${item.date}</span></div>
        <h3>${item.title}</h3>
        <p>${item.description}</p>
        <small>${item.credit}</small>
      </div>
    </article>`).join('');
}

function renderRestoration(items) {
  const container = qs('#restoration-timeline');
  if (!container || !items) return;
  container.innerHTML = items.map((item) => `
    <div class="timeline-item">
      <div class="timeline-card">
        <time>${item.date}</time>
        <h3>${item.title}</h3>
        <p>${item.description}</p>
        <small>${item.source}</small>
        <div class="status-badge">${item.status}</div>
      </div>
    </div>
  `).join('');
}

function createLightbox() {
  const overlay = qs('.lightbox-overlay');
  if (!overlay) return;
  const closeBtn = qs('.lightbox-close', overlay);
  closeBtn?.addEventListener('click', () => overlay.classList.remove('active'));
  overlay.addEventListener('click', (event) => {
    if (event.target === overlay) {
      overlay.classList.remove('active');
    }
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
  const categories = ["All", ...new Set(items.map((item) => item.category))];
  filterBar.innerHTML = categories.map((category) => `
    <button type="button" class="filter-button${category === 'All' ? ' active' : ''}" data-category="${category}">${category}</button>
  `).join('');

  function updateGrid(category = 'All') {
    const selection = category === 'All' ? items : items.filter((item) => item.category === category);
    container.innerHTML = selection.map((item) => `
      <article class="gallery-item" data-id="${item.id}" tabindex="0" aria-label="View ${item.title}">
        <img src="${item.image}" alt="${item.alt}" loading="lazy">
        <div class="gallery-info">
          <h3>${item.title}</h3>
          <p>${item.date} · ${item.location}</p>
        </div>
      </article>
    `).join('');
    qsa('.gallery-item').forEach((card) => {
      card.addEventListener('click', () => {
        const found = items.find((item) => item.id === card.dataset.id);
        if (found) showLightbox(found);
      });
      card.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
          const found = items.find((item) => item.id === card.dataset.id);
          if (found) showLightbox(found);
        }
      });
    });
  }

  filterBar.addEventListener('click', (event) => {
    const button = event.target.closest('button');
    if (!button) return;
    qsa('.filter-button').forEach((btn) => btn.classList.remove('active'));
    button.classList.add('active');
    updateGrid(button.dataset.category);
  });

  updateGrid();
}

function renderNewsList(items) {
  const container = qs('#news-list');
  const searchInput = qs('#news-search');
  const categorySelect = qs('#news-category');
  if (!container || !items) return;
  const categories = ["All", ...new Set(items.map((item) => item.category))];
  if (categorySelect) {
    categorySelect.innerHTML = categories.map((category) => `<option value="${category}">${category}</option>`).join('');
  }

  function updateList() {
    const query = searchInput?.value.toLowerCase() || '';
    const category = categorySelect?.value || 'All';
    const filtered = items.filter((item) => {
      const matchesCategory = category === 'All' || item.category === category;
      const matchesSearch = item.title.toLowerCase().includes(query) || item.excerpt.toLowerCase().includes(query);
      return matchesCategory && matchesSearch;
    });

    container.innerHTML = filtered.map((item) => `
      <article class="news-card">
        <img src="${item.coverImage}" alt="${item.title}" loading="lazy">
        <div class="card-content">
          <div class="news-meta"><span>${item.date}</span><span>${item.category}</span></div>
          <h3>${item.title}</h3>
          <p>${item.excerpt}</p>
          <a class="btn" href="/news/${item.slug}/">Read more</a>
        </div>
      </article>
    `).join('');
  }

  searchInput?.addEventListener('input', updateList);
  categorySelect?.addEventListener('change', updateList);
  updateList();
}

function renderNewsDetail(items) {
  const slug = location.pathname.split('/').filter(Boolean).pop();
  const item = items?.find((entry) => entry.slug === slug);
  if (!item) return;
  const container = qs('#news-detail');
  if (!container) return;
  container.innerHTML = `
    <article class="news-card">
      <img src="${item.coverImage}" alt="${item.title}" loading="lazy">
      <div class="card-content">
        <div class="news-meta"><span>${item.date}</span><span>${item.category}</span><span>${item.author}</span></div>
        <h1>${item.title}</h1>
        <p>${item.excerpt}</p>
        <div>${item.body}</div>
        <div class="page-note"><strong>Source note:</strong> ${item.sources}</div>
      </div>
    </article>`;
  if (item.gallery && item.gallery.length) {
    const gallery = document.createElement('div');
    gallery.className = 'gallery-grid';
    gallery.innerHTML = item.gallery.map((image) => `
      <article class="gallery-item" data-id="${image.id}">
        <img src="${image.image}" alt="${image.alt}" loading="lazy">
        <div class="gallery-info">
          <h3>${image.title}</h3>
          <p>${image.date} · ${image.location}</p>
        </div>
      </article>
    `).join('');
    container.appendChild(gallery);
    qsa('.gallery-item', gallery).forEach((card) => {
      card.addEventListener('click', () => {
        const found = item.gallery.find((image) => image.id === card.dataset.id);
        if (found) showLightbox(found);
      });
    });
  }
}

function init() {
  setNavActive();
  toggleMenu();
  createLightbox();
  const page = document.body.dataset.page;
  if (!page) return;
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

    if (page === 'home') {
      renderPreviewCards(state.news, '#latest-updates');
    }
    if (page === 'history') {
      const intro = qs('#history-timeline');
      if (intro) {
        intro.innerHTML = `
          <div class="timeline-item"><time>c. 1813</time><h3>Early Chabad connection</h3><p>Lubavitch is first documented as a center of Chabad life and leadership.</p></div>
          <div class="timeline-item"><time>19th century</time><h3>Growth as a Chassidic center</h3><p>The village supported Torah study, Chassidic prayer, and the yeshiva tradition.</p></div>
          <div class="timeline-item"><time>Late 19th century</time><h3>Tomchei Temimim</h3><p>The Tomchei Temimim yeshiva is associated with the life of Chabad students and teachers.</p></div>
          <div class="timeline-item"><time>20th century</time><h3>Destruction, silence, and return</h3><p>Historical sites were disrupted by wartime and later Soviet neglect; memory endured through scholarship and return visits.</p></div>
          <div class="timeline-item"><time>Late 20th century</time><h3>Preservation begins</h3><p>Visitors and local representatives began documenting and restoring the historic sites.</p></div>
          <div class="timeline-item"><time>2000s–today</time><h3>Living restoration</h3><p>Ongoing restoration, documentation, and memory work honors the village and its heritage.</p></div>`;
      }
    }
    if (page === 'sacred-sites') {
      renderSites(state.sites);
    }
    if (page === 'restoration') {
      renderRestoration(state.restoration);
    }
    if (page === 'gallery') {
      renderGallery(state.gallery);
    }
    if (page === 'news') {
      renderNewsList(state.news);
    }
    if (page === 'news-detail') {
      renderNewsDetail(state.news);
    }
    if (page === 'archive') {
      renderArchive(state.archive);
    }
  });
}

window.addEventListener('DOMContentLoaded', init);
