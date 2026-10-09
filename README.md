# Once Upon a Timeline

A static literature library built in HTML, CSS and JavaScript. Includes 78 works across eight eras, 545 illustrated scenes, character guides, recall prompts, 78 annotated quotations, saved favourites and reading progress.

## Open locally

Open `index.html` in a browser. No installation, build, API key or backend is needed. Fonts load from Google Fonts when online, with Georgia and Arial as offline fallbacks. All illustrations are original inline SVG artwork. Content and functionality work offline.

## Publish on GitHub Pages

1. Upload `index.html`, `styles.css`, `app.js`, `stories.js`, the `assets` folder and `literature by codex.docx` to a repository. Keep them in the same arrangement.
2. In the repository, select **Settings → Pages → Deploy from a branch**.
3. Select the branch containing these files and the **root** folder, then save.

All URLs are relative, so the site also works in a repository subdirectory. Publishing is left for you as requested. No remote repository has been created. See the [official GitHub Pages publishing guide](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Content and editing

- The original three Word files remain unchanged. 25 distinct works are adapted; the duplicate Paradise Lost is merged, and the April opening-line note appears within The Waste Land.
- There are 53 additions: The Odyssey, Antigone and Frankenstein, plus 50 further works spanning More, Shakespeare, Donne, Webster, Bunyan, Defoe, Swift, Fielding, Sterne, Blake, Wordsworth, Coleridge, Percy Shelley, Keats, Byron, Rossetti, Austen, the Brontës, Dickens, George Eliot, Wilde, Stevenson, Stoker, Joyce, Woolf, Lawrence, T. S. Eliot and Yeats. All 53 additions have copies in the 54-page `literature by codex.docx`.
- New works have seven scenes. Two supplementary scenes enrich each original storyboard, keeping its original scenes and stable story ID. All stories now have seven scenes except the six-scene To His Coy Mistress.
- Every work has a short quotation, its speaker or textual context, an original memory connection and a linked reference. Quotation wording follows the linked edition. Contemporary works use academic quotation references where full primary texts are unavailable.
- `tools/build_content.py` assembles the original catalogue, three `additions_*.py` files, `expand_originals.py` and `quotations.py`. Run it with Python to regenerate `stories.js` and `content/catalog.json`. The website itself requires no Python.
- `tools/build_document.py` generates the companion document with python-docx.
- Era divisions are learning aids rather than strict literary-history boundaries. Ordering follows first publication, with approximate composition or performance dates where necessary. Beowulf uses its manuscript-era anchor. A date range is displayed when needed.
- Storyboards use concise original paraphrases. They contain spoilers. Non-narrative poetry is presented through thematic landmarks. Editorial notes record ambiguities and corrections to the supplied notes.
- The palette translates the supplied historical color names to hexadecimal colors. Original SVG scenes combine era colors with natural setting imagery. Characters are symbolic illustrations rather than historical portraits.

## Controls and storage

Click an era, search a title/author/character, and open a story. Next/Previous buttons, scene dots, left/right keys and horizontal swipes on the picture turn pages. At the final scene, Next opens recall. After recall, Explore memorable quotes opens the fourth panel. Escape closes the reader. Tab panels support arrow keys, Home and End. Press `/` to focus search.

The heart saves a work to My shelf. Reading positions, saved works and remembered status are stored only in this browser's localStorage. Existing positions migrate once to the matching original scene within the expanded storyboard; favourites and remembered status are preserved. Storage-denied environments remain usable for the current session. Sources & notes contains a two-click reset. The site respects reduced motion and works at mobile widths. Existing scene URLs still use their numeric position within the expanded storyboard.

## Verification

`tools/check_site.cjs` performs browser interaction checks for all 78 stories and 545 scenes, filters, searches, persistence, recall, direct links and mobile layouts. `tools/check_expansion.cjs` checks all quotation panels, four-tab navigation, progress migration and mobile quote layouts. `tools/check_extras.cjs` checks focus, touch and storage edge cases. `tools/verify_quotations.py` compares 64 Gutenberg excerpts against their linked text editions; the 14 other excerpts were checked against their linked references. QA images, source comparison reports and document renders are kept in `qa/` and are not required for hosting.
