import os

base_head = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Source+Sans+Pro:wght@400;600;700&family=Noto+Serif+Hebrew:wght@400;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/assets/css/styles.css" />
  <script defer src="/assets/js/main.js"></script>
  {extra_meta}
  <title>{title}</title>
</head>
<body data-page="{page}">
  <header class="header" role="banner">
    <div class="page header-inner">
      <a class="brand" href="/">
        <strong>Lubavitch Heritage</strong>
        <small>Historic archive & restoration project</small>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="site-navigation">Menu</button>
      <nav id="site-navigation" role="navigation">
        <ul class="nav-list">
          <li><a href="/">Home</a></li>
          <li><a href="/history/">History</a></li>
          <li><a href="/sacred-sites/">Sacred Sites</a></li>
          <li><a href="/restoration/">Restoration</a></li>
          <li><a href="/gallery/">Gallery</a></li>
          <li><a href="/news/">News</a></li>
          <li><a href="/visit/">Visit</a></li>
          <li><a href="/archive/">Archive</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <main class="page">
'''

base_footer = '''  </main>
  <footer class="footer">
    <div class="page footer-inner">
      <div class="footer-grid">
        <div>
          <h3>Lubavitch Heritage Restoration</h3>
          <p>A respectful historical archive for Lubavitch / Lyubavichi and the ongoing work to preserve its sacred Jewish sites.</p>
        </div>
        <div>
          <h3>Quick links</h3>
          <a href="/history/">History</a><br />
          <a href="/restoration/">Restoration</a><br />
          <a href="/gallery/">Gallery</a><br />
          <a href="/contact/">Contact</a>
        </div>
        <div>
          <h3>Note</h3>
          <p>This website is an independent historical and informational project. Historical details should be verified with official representatives before citation or publication.</p>
        </div>
      </div>
      <div class="footer-note">© Lubavitch Historical Archive Project</div>
    </div>
  </footer>
</body>
</html>
'''

pages = [
    {
        'path': 'index.html',
        'page': 'home',
        'title': 'Lubavitch Heritage Restoration Project | Chabad History in Lyubavichi',
        'meta': '<meta name="description" content="A respectful digital archive and restoration chronicle for the historic village of Lubavitch, its sacred sites and ongoing preservation work." />',
        'content': '''
    <section class="hero" aria-label="Lubavitch hero image">
      <div class="hero-content">
        <p class="hero-tags"><span class="hero-tag">Archive</span><span class="hero-tag">Restoration</span><span class="hero-tag">Chabad History</span></p>
        <h1>Lubavitch: Where Chabad History Lives</h1>
        <p>Preserving the sacred legacy of Lubavitch through memory, restoration, and living connection.</p>
        <div class="hero-buttons">
          <a class="btn" href="/history/">Explore the History</a>
          <a class="btn-secondary" href="/restoration/">Follow the Restoration</a>
          <a class="btn-secondary" href="/contact/">Share Materials</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="section-title"><h2>Why Lubavitch Matters</h2></div>
      <div class="grid grid-3">
        <article class="card"><h3 class="card-strong">The Home of Chabad-Lubavitch</h3><p>Lubavitch is the village that gave a name to a worldwide movement, rooted in Torah, prayer, and community life.</p></article>
        <article class="card"><h3 class="card-strong">The Ohel of the Rebbeim</h3><p>The Ohel remains one of the central destinations for visitors honoring the Tzemach Tzedek and the Rebbe Maharash.</p></article>
        <article class="card"><h3 class="card-strong">Tomchei Temimim and Torah Life</h3><p>The village is linked with the yeshiva tradition and the historic life of Chabad students and teachers.</p></article>
        <article class="card"><h3 class="card-strong">A Living Restoration Project</h3><p>Restoration in Lubavitch is ongoing, careful, and rooted in memory rather than spectacle.</p></article>
      </div>
    </section>
    <section class="section">
      <div class="section-title"><h2>The Restoration Continues</h2></div>
      <div class="grid grid-3">
        <article class="card"><h3 class="card-strong">Cemetery Preservation</h3><p>Historic matzeivos are documented, cleaned, and protected with respect.</p></article>
        <article class="card"><h3 class="card-strong">Ohel Maintenance</h3><p>Care for the resting places of the Rebbeim includes structures, ground preservation, and visitor access.</p></article>
        <article class="card"><h3 class="card-strong">Historical Buildings</h3><p>Historic sites associated with prayer and study are being recorded and restored.</p></article>
      </div>
    </section>
    <section class="section">
      <div class="section-title"><h2>Latest Updates</h2><p class="section-intro">News and archive notes from the ongoing Lubavitch restoration work.</p></div>
      <div id="latest-updates" class="grid grid-3">Loading news...</div>
    </section>
    <section class="section">
      <div class="section-title"><h2>Before &amp; After</h2><p class="section-intro">A structure for before and after visual study that can receive new photographs as the project advances.</p></div>
      <div class="grid grid-2">
        <article class="image-card"><img src="/images/gallery/ohel-renovation-2024.svg" alt="Before and after restoration view" loading="lazy"><div class="image-card-body"><p>Before / After photography can be added to show the careful progression of restoration.</p></div></article>
        <article class="image-card"><img src="/images/gallery/cemetery-restoration.svg" alt="Cemetery restoration photo" loading="lazy"><div class="image-card-body"><p>Photo pairs help illustrate the preservation of stones, paths, and historic grounds.</p></div></article>
      </div>
    </section>
    <section class="section cta-panel">
      <h2>Help Preserve the Archive</h2>
      <p>If you have photographs, documents, maps, family stories, or memories connected to Lubavitch, we invite you to share them. Every image and testimony helps preserve this history for future generations.</p>
      <a class="btn" href="/contact/">Contact the Project</a>
    </section>
'''
    },
    {
        'path': os.path.join('history', 'index.html'),
        'page': 'history',
        'title': 'History of Lubavitch | The Village Behind Chabad-Lubavitch',
        'meta': '<meta name="description" content="The history of Lubavitch, its connection to Chabad-Lubavitch, the Rebbeim, and the ongoing work to restore this historic village." />',
        'content': '''
    <section class="section">
      <div class="section-title"><h1>The Village Behind the Name</h1></div>
      <p class="section-intro">Before Lubavitch became a global name, it was a real village — a place of Torah, prayer, leadership, and Chassidic life.</p>
    </section>
    <section class="section grid grid-2">
      <article class="card"><h3 class="card-strong">The Village</h3><p>Lubavitch is a historic shtetl in Russia that gave its name to the Chabad-Lubavitch movement and became a symbol of Jewish spiritual life.</p></article>
      <article class="card"><h3 class="card-strong">The Rebbeim</h3><p>The village is associated with the Lubavitcher Rebbeim, including the Tzemach Tzedek and the Rebbe Maharash, whose Ohel remains a point of pilgrimage.</p></article>
      <article class="card"><h3 class="card-strong">Torah and Chassidic Life</h3><p>Tomchei Temimim and related institutions helped shape the Chassidic study and prayer life that defined Lubavitch.</p></article>
      <article class="card"><h3 class="card-strong">Destruction, Silence, and Return</h3><p>In the 20th century, many Jewish sites were damaged or neglected. Since the fall of the Soviet regime, memory and restoration work has gradually returned.</p></article>
      <article class="card"><h3 class="card-strong">Lubavitch Today</h3><p>Today the village is once again a place of remembrance, restoration, and careful documentation of its heritage.</p></article>
    </section>
    <section class="section">
      <div class="section-title"><h2>Timeline</h2><p class="section-intro">The history of Lubavitch is presented with the care of a museum chronicle.</p></div>
      <div id="history-timeline" class="timeline"></div>
    </section>
'''
    },
    {
        'path': os.path.join('rabbi-gavriel-gordon', 'index.html'),
        'page': 'rabbi-gavriel-gordon',
        'title': 'Rabbi Gavriel Gordon | Preservation Work in Lubavitch',
        'meta': '<meta name="description" content="Information about Rabbi Gavriel Gordon and his role in the preservation and restoration of Lubavitch sacred sites." />',
        'content': '''
    <section class="section">
      <div class="section-title"><h1>Rabbi Gavriel Gordon</h1></div>
      <p class="section-intro">Serving Lubavitch through preservation, restoration, and living connection.</p>
      <p>Rabbi Gavriel Gordon is referenced in Chabad and Jewish heritage sources as the local Chabad representative in Lubavitch and as a central figure involved in the preservation, maintenance, and restoration of the village’s sacred Jewish sites.</p>
      <p>His work includes caring for the Ohel of the Rebbeim, supporting the restoration of historic areas, helping document discoveries at the cemetery, receiving visitors and groups, and maintaining the connection between the global Jewish community and the village from which the Lubavitch name emerged.</p>
    </section>
    <section class="section">
      <div class="section-title"><h2>Areas of Work</h2></div>
      <div class="grid grid-3">
        <article class="card"><h3 class="card-strong">Sacred Site Preservation</h3><p>Supporting the care and maintenance of historic sites in Lubavitch.</p></article>
        <article class="card"><h3 class="card-strong">Cemetery Restoration</h3><p>Documenting and preserving the cemetery’s historic stones and grounds.</p></article>
        <article class="card"><h3 class="card-strong">Ohel Maintenance</h3><p>Maintaining the Ohel of the Rebbeim and preparing it for respectful visitation.</p></article>
        <article class="card"><h3 class="card-strong">Historical Documentation</h3><p>Collecting photographs, notes, and records that help tell the village’s story.</p></article>
        <article class="card"><h3 class="card-strong">Visitor Coordination</h3><p>Helping visitors and groups engage with the village in a respectful way.</p></article>
        <article class="card"><h3 class="card-strong">Photo and Archive Development</h3><p>Building a living archive for the project’s images and historical materials.</p></article>
      </div>
    </section>
    <section class="section cta-panel">
      <h2>A Living Responsibility</h2>
      <p>The work in Lubavitch is not only about preserving buildings and stones. It is about restoring access, dignity, memory, and continuity to one of the most meaningful places in Chabad history.</p>
      <div class="note-block">All biographical and historical details should be verified with official project representatives before publication.</div>
    </section>
'''
    },
    {
        'path': os.path.join('sacred-sites', 'index.html'),
        'page': 'sacred-sites',
        'title': 'Lubavitch Sacred Sites | Historic and Holy Places',
        'meta': '<meta name="description" content="A catalog of Lubavitch sacred sites, including the Ohel of the Rebbeim, cemetery, Tomchei Temimim site, and other historic places." />',
        'content': '''
    <section class="section">
      <div class="section-title"><h1>Sacred Sites of Lubavitch</h1></div>
      <p class="section-intro">A respectful catalog of the historic places and living sites that remain at the center of Lubavitch heritage.</p>
    </section>
    <section class="section">
      <div id="sites-list" class="sites-grid"></div>
    </section>
'''
    },
    {
        'path': os.path.join('restoration', 'index.html'),
        'page': 'restoration',
        'title': 'Lubavitch Restoration Project | Ohel, Cemetery and Historic Sites',
        'meta': '<meta name="description" content="Documenting the ongoing restoration of Lubavitch sacred sites, including cemetery work, Ohel renovation, and archive development." />',
        'content': '''
    <section class="section">
      <div class="section-title"><h1>Restoration in Progress</h1></div>
      <p class="section-intro">Documenting the ongoing work to preserve, restore, and honor the sacred Jewish sites of Lubavitch.</p>
    </section>
    <section class="section">
      <div class="section-title"><h2>Restoration Timeline</h2></div>
      <div id="restoration-timeline" class="timeline"></div>
    </section>
    <section class="section">
      <div class="section-title"><h2>Project Areas</h2></div>
      <div class="project-grid grid grid-3">
        <article class="card"><h3 class="card-strong">Cemetery Restoration</h3><p>Preserving burial grounds and memorial stones with care.</p></article>
        <article class="card"><h3 class="card-strong">Ohel Renovation</h3><p>Maintaining the Ohel of the Rebbeim as a dignified place of memory.</p></article>
        <article class="card"><h3 class="card-strong">Historical Buildings</h3><p>Documenting and restoring structures connected to Torah life.</p></article>
        <article class="card"><h3 class="card-strong">Visitor Access</h3><p>Creating pathways and guidance for respectful visits.</p></article>
        <article class="card"><h3 class="card-strong">Matzeivah Documentation</h3><p>Recording gravestones, fragments, and inscriptions for future study.</p></article>
        <article class="card"><h3 class="card-strong">Photo Archive</h3><p>Collecting images that show restoration progress and the historic landscape.</p></article>
      </div>
    </section>
    <section class="section grid grid-2">
      <article class="image-card"><img src="/images/gallery/ohel-renovation-2024.svg" alt="Ohel renovation example" loading="lazy"><div class="image-card-body"><p>Before / after imagery for the Ohel can be added here as the archive grows.</p></div></article>
      <article class="image-card"><img src="/images/gallery/cemetery-restoration.svg" alt="Cemetery restoration example" loading="lazy"><div class="image-card-body"><p>Visual documentation supports each restoration phase in a respectful way.</p></div></article>
    </section>
    <section class="section">
      <div class="section-title"><h2>About the Project</h2></div>
      <div class="grid grid-2">
        <article class="card">
          <h3 class="card-strong">Local Leadership</h3>
          <p>The restoration work is led on the ground by the local Chabad emissary in Lubavitch, who is responsible for day-to-day care of the Ohel, the cemetery, and all sacred sites. His work includes receiving visitors and pilgrimage groups, coordinating restoration phases, maintaining the Akeda Shul, and managing the ongoing archive and documentation effort.</p>
        </article>
        <article class="card">
          <h3 class="card-strong">Partners &amp; Sponsors</h3>
          <p>The project operates in partnership with Geder Avos, the organization responsible for the cemetery restoration and burial database. Major restoration phases have been made possible through the generous support of Yosef and Penina Batsheva Popack and donors from the broader Chabad community worldwide.</p>
        </article>
      </div>
    </section>
    <section class="section cta-panel">
      <h2>Current Needs</h2>
      <p>The project continues to require documentation, careful restoration, photography, archival materials, historical research, and support from people connected to Lubavitch around the world.</p>
      <a class="btn" href="/contact/">Get Involved</a>
    </section>
'''
    },
    {
        'path': os.path.join('gallery', 'index.html'),
        'page': 'gallery',
        'title': 'Lubavitch Photo Gallery | Ohel, Cemetery and Restoration Images',
        'meta': '<meta name="description" content="A photo gallery documenting the Ohel, cemetery, restoration work, historic buildings, and archival materials from Lubavitch." />',
        'content': '''
    <section class="section">
      <div class="section-title"><h1>Gallery</h1></div>
      <p class="section-intro">A visual archive of Lubavitch, the sacred sites, the restoration work, and the historical landscape.</p>
    </section>
    <section class="section">
      <div id="gallery-filters" class="filter-toolbar"></div>
      <div id="gallery-grid" class="gallery-grid"></div>
    </section>
'''
    },
    {
        'path': os.path.join('news', 'index.html'),
        'page': 'news',
        'title': 'Lubavitch News & Updates | Historical Archive Notes',
        'meta': '<meta name="description" content="News and updates from the Lubavitch historical archive project, including restoration reports and discovery notes." />',
        'content': '''
    <section class="section">
      <div class="section-title"><h1>News / Updates</h1></div>
      <p class="section-intro">A chronicle of project updates, historical notes, and archive discoveries from Lubavitch.</p>
    </section>
    <section class="section">
      <div class="filter-toolbar">
        <input id="news-search" type="search" placeholder="Search news" aria-label="Search news" />
        <select id="news-category" aria-label="Filter by category"></select>
      </div>
      <div id="news-list" class="news-grid"></div>
    </section>
'''
    },
    {
        'path': os.path.join('news', 'welcome-to-lubavitch-archive', 'index.html'),
        'page': 'news-detail',
        'title': 'Welcome to the Lubavitch Historical Archive Project',
        'meta': '<meta name="description" content="An announcement introducing the Lubavitch Historical Archive Project and its work preserving Lubavitch heritage." />',
        'content': '''
    <section class="section">
      <div id="news-detail"></div>
    </section>
'''
    },
    {
        'path': os.path.join('visit', 'index.html'),
        'page': 'visit',
        'title': 'Visit Lubavitch | Historical and Sacred Sites of Chabad',
        'meta': '<meta name="description" content="Practical and respectful information for visitors to Lubavitch, its Ohel, cemetery, and historic sites." />',
        'content': '''
    <section class="section">
      <div class="section-title"><h1>Visit Lubavitch</h1></div>
      <p class="section-intro">Visitors come to Lubavitch to pray, learn, connect with Chabad history, visit the Ohel of the Rebbeim, and see the places connected to the village’s spiritual legacy.</p>
    </section>
    <section class="section grid grid-2">
      <article class="card"><h3 class="card-strong">Planning a Visit</h3><p>Visits should be planned with respect for the sacred sites and the local restoration effort.</p></article>
      <article class="card"><h3 class="card-strong">What Visitors May See</h3><p>The Ohel of the Rebbeim, the historic cemetery, restored areas, and the village landscape help tell the story of Lubavitch.</p></article>
    </section>
    <section class="section">
      <div class="section-title"><h2>Respectful Conduct</h2></div>
      <ul class="list-plain">
        <li>Dress respectfully.</li>
        <li>Maintain quiet near sacred places.</li>
        <li>Do not move stones or artifacts.</li>
        <li>Do not photograph people without permission.</li>
        <li>Coordinate group visits in advance.</li>
        <li>Follow local project guidance.</li>
      </ul>
    </section>
    <section class="section">
      <div class="section-title"><h2>Group Visits</h2></div>
      <p class="section-intro">For groups, schools, yeshivos, communities, and historians, visits should be coordinated in advance to honor the site and ensure safe access.</p>
    </section>
    <section class="section cta-panel">
      <h2>Contact About a Visit</h2>
      <p>Please use the contact page to express interest in visiting Lubavitch and to ask about the best way to plan a respectful trip.</p>
      <a class="btn" href="/contact/">Contact About a Visit</a>
    </section>
'''
    },
    {
        'path': os.path.join('archive', 'index.html'),
        'page': 'archive',
        'title': 'Lubavitch Historical Archive | Photos, Documents and Stories',
        'meta': '<meta name="description" content="A curated archive of photographs, documents, maps, family stories, and research notes connected to Lubavitch." />',
        'content': '''
    <section class="section">
      <div class="section-title"><h1>Archive</h1></div>
      <p class="section-intro">The archive is designed to gather photographs, documents, maps, family stories, research notes, and visual records connected to Lubavitch.</p>
      <p>Some materials may be fragmentary. Some may require verification. Together, they help preserve the memory of a place whose influence reached far beyond its physical size.</p>
    </section>
    <section class="section">
      <div class="section-title"><h2>Archive Collections</h2></div>
      <div id="archive-list" class="archive-grid"></div>
    </section>
'''
    },
    {
        'path': os.path.join('contact', 'index.html'),
        'page': 'contact',
        'title': 'Contact Lubavitch Archive Project | Share Materials or Support',
        'meta': '<meta name="description" content="Contact form for sharing photographs, documents, family stories, or project support related to Lubavitch restoration and archive work." />',
        'content': '''
    <section class="section">
      <div class="section-title"><h1>Contact / Get Involved</h1></div>
      <p class="section-intro">If you have photographs, documents, stories, maps, or memories connected to Lubavitch, we invite you to share them. Every fragment matters.</p>
    </section>
    <section class="section grid grid-2">
      <article class="card"><h3 class="card-strong">How to Reach Us</h3><p>Use this form to tell us about archive material, a possible visit, or support for restoration work. Personal contact details are collected respectfully.</p></article>
      <article class="card"><h3 class="card-strong">What We Seek</h3><p>Photographs, documents, family stories, maps, oral memories, and research notes that help preserve Lubavitch history.</p></article>
    </section>
    <section class="section">
      <form class="contact-form" action="mailto:project@lubavitch-archive.org" method="post" enctype="text/plain">
        <label>Full Name<input type="text" name="name" required /></label>
        <label>Email<input type="email" name="email" required /></label>
        <label>Country<input type="text" name="country" /></label>
        <label>Organization<input type="text" name="organization" /></label>
        <label>Reason for Contact<select name="reason">
          <option value="visit">I want to visit Lubavitch</option>
          <option value="photographs">I have historical photographs</option>
          <option value="documents">I have documents or family stories</option>
          <option value="support">I want to support the restoration</option>
          <option value="institution">I represent a community or institution</option>
          <option value="research">I want to help with research</option>
          <option value="other">Other</option>
        </select></label>
        <label>Message<textarea name="message" rows="6"></textarea></label>
        <div class="form-actions"><button class="btn" type="submit">Send a Message</button></div>
      </form>
      <div class="note-block">This is a placeholder contact form. Real upload handling and backend integration can be added later with Formspree, Netlify Forms, or another platform.</div>
    </section>
'''
    }
]

site_pages = [
    {
        'slug': 'ohel-rebbeim',
        'title': 'The Ohel of the Rebbeim',
        'image': '/images/sites/ohel-rebbeim.svg',
        'description': 'The Ohel in Lubavitch is associated with the resting places of the Tzemach Tzedek and the Rebbe Maharash. It is one of the central destinations for visitors to Lubavitch.',
        'significance': 'A place of prayer, memory, and connection to the Rebbeim of Chabad.',
        'status': 'Restored and maintained'
    },
    {
        'slug': 'historic-cemetery',
        'title': 'Historic Cemetery',
        'image': '/images/sites/cemetery-restoration.svg',
        'description': 'The cemetery of Lubavitch contains historic matzeivos and remains a major focus of preservation, research, cleaning, uncovering, documentation, and restoration.',
        'significance': 'Historic gravestones and burial grounds are central to the village\'s memory.',
        'status': 'Preserved and documented'
    },
    {
        'slug': 'rebbetzins-ohel',
        'title': 'Rebbetzins’ Ohel',
        'image': '/images/sites/rebbetzins-ohel.svg',
        'description': 'A sacred area associated with the Rebbetzins of Chabad, restored and respectfully marked.',
        'significance': 'Honoring the female leaders and families who supported Chabad life.',
        'status': 'Maintained'
    },
    {
        'slug': 'tomchei-temimim',
        'title': 'Tomchei Temimim Yeshiva Site',
        'image': '/images/sites/tomchei-temimim.svg',
        'description': 'The site connected to the historic yeshiva Tomchei Temimim, which played a central role in Chabad history.',
        'significance': 'A place linked with Torah study and the spiritual life of Chabad students.',
        'status': 'Documented'
    },
    {
        'slug': 'historic-beis-midrash',
        'title': 'Historic Beis Midrash / Zal',
        'image': '/images/sites/historic-zal.svg',
        'description': 'The historic study hall area connected with Torah learning and Chassidic life in Lubavitch.',
        'significance': 'A center of prayer, learning, and community study.',
        'status': 'Preserved'
    },
    {
        'slug': 'rebbeims-courtyard',
        'title': 'Rebbeim’s Courtyard / Chatzer',
        'image': '/images/sites/rebbeims-courtyard.svg',
        'description': 'The historical courtyard area connected to the life and leadership of the Rebbeim.',
        'significance': 'A living space that helped shape the leadership of Chabad.',
        'status': 'Recorded'
    },
    {
        'slug': 'old-streets',
        'title': 'Old Streets of Lubavitch',
        'image': '/images/sites/old-streets.svg',
        'description': 'The physical landscape of the village — roads, homes, paths, and views — helps visitors understand the historic setting.',
        'significance': 'The village fabric preserves the context of daily Chassidic life.',
        'status': 'Visible'
    }
]

for page in pages:
    folder = os.path.dirname(page['path'])
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    content = base_head.format(title=page['title'], extra_meta=page['meta'], page=page['page'])
    content += page['content']
    content += base_footer
    with open(page['path'], 'w', encoding='utf-8') as f:
        f.write(content)

for site in site_pages:
    folder = os.path.join('sites', site['slug'])
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, 'index.html')
    content = base_head.format(title=f"{site['title']} | Lubavitch Sacred Site", extra_meta=f'<meta name="description" content="{site["description"]}" />', page='sacred-sites')
    content += f'''    <section class="section">
      <div class="section-title"><h1>{site['title']}</h1></div>
      <div class="image-card"><img src="{site['image']}" alt="{site['title']}" loading="lazy"></div>
      <div class="card"><p>{site['description']}</p><p><strong>Historical significance:</strong> {site['significance']}</p><p><strong>Restoration status:</strong> {site['status']}</p></div>
      <div class="page-note">This page is part of the Lubavitch archive project. Details should be verified before formal publication.</div>
    </section>
'''
    content += base_footer
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Site pages generated.')
