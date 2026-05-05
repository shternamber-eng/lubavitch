# Lubavitch Heritage Restoration Project

A static informational website for Lubavitch / Lyubavichi and the restoration work associated with Rabbi Gavriel Gordon.

## Project structure

- `index.html` — Home page
- `history/index.html` — History of Lubavitch
- `rabbi-gavriel-gordon/index.html` — Rabbi Gavriel Gordon page
- `sacred-sites/index.html` — Sacred sites catalog
- `restoration/index.html` — Restoration timeline and project overview
- `gallery/index.html` — Photo gallery with filters and lightbox
- `news/index.html` — News list
- `news/welcome-to-lubavitch-archive/index.html` — Sample news article
- `visit/index.html` — Visitor information
- `archive/index.html` — Archive section
- `contact/index.html` — Contact / get involved page
- `sites/*/index.html` — Sacred site detail placeholder pages
- `assets/css/styles.css` — Global styles
- `assets/js/main.js` — Shared frontend logic and data rendering
- `data/*.json` — Content data for news, gallery, restoration, sites, archive, and navigation
- `images/` — Placeholder image assets

## Run locally

This site uses JSON content loaded by JavaScript, so it should be served by a local HTTP server.

### Option 1: Python

```sh
cd "c:\Users\19298\OneDrive\Documents\GitHub\lubavitch"
python -m http.server 8000
```

Then open `http://localhost:8000/`.

### Option 2: Visual Studio Code Live Server

Install the Live Server extension and open the workspace, then click <kbd>Go Live</kbd>.

## How to add new content

### Add a news update

1. Open `data/news.json`.
2. Add a new object with fields:
   - `id`
   - `slug`
   - `title`
   - `date`
   - `category`
   - `author`
   - `coverImage`
   - `excerpt`
   - `body`
   - `gallery` (optional)
   - `sources`
3. Create a matching detail page if you want a separate static route, or reuse the sample detail page structure.

### Add a new gallery image

1. Open `data/gallery.json`.
2. Add a new object with fields:
   - `id`
   - `title`
   - `image`
   - `category`
   - `date`
   - `location`
   - `caption`
   - `description`
   - `credit`
   - `alt`
3. Add the image file to `images/gallery/` and reference it with an absolute path, for example `/images/gallery/new-photo.svg`.

### Edit restoration timeline

1. Open `data/restoration.json`.
2. Add or update objects with fields:
   - `id`
   - `year`
   - `date`
   - `title`
   - `category`
   - `status`
   - `description`
   - `images`
   - `source`
   - `notes`

### Replace placeholder images

1. Place new image files into the appropriate `images/` subfolder.
2. Update the image paths in the JSON data files or page templates.
3. Use descriptive filenames, for example `ohel-rebbeim-2026.jpg`.

## Deployment

The site is ready for static hosting on Cloudflare Pages, Vercel, Netlify, or any static web host.

- Deploy the entire repository root.
- Ensure the host supports directory-based routes.
- If a host uses rewrite rules, point the root to `index.html` and preserve subfolders as static paths.

## Notes

- This website is designed as a respectful historical archive and restoration chronicle.
- Facts should be verified before final publication.
- No direct personal contact data is published on the site beyond the placeholder contact form.
