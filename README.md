# Once Upon a Timeline

A static literature library and installable PWA built in HTML, CSS and JavaScript. Includes 98 works across eight eras, exactly 12 scenes per work (1176 total), expressive character artwork, lively storytelling, recall prompts, 98 annotated quotations, saved favourites and reading progress.

## Open locally

Open `index.html` in a browser. No installation, build, API key or backend is needed. Fonts load from Google Fonts when online, with Georgia and Arial as offline fallbacks. All illustrations are original inline SVG artwork. Content and functionality work offline.

## Publish on GitHub Pages

1. Keep the website files in the repository root, including `manifest.json`, `sw.js`, `pwa.js`, `illustrations.js`, the complete `assets` folder and `literature by codex.docx`. The local `website-github-ready.zip` also contains these files in the correct arrangement.
2. In the repository, select **Settings → Pages → Deploy from a branch**.
3. Select the branch containing these files and the **root** folder, then save.

All URLs are relative, so the site also works in a repository subdirectory. The repository is [AscendesShady/English-Literature](https://github.com/AscendesShady/English-Literature). GitHub Pages must be enabled separately if it is not already configured. See the [official GitHub Pages publishing guide](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Content and editing

- The original three Word files remain unchanged. 25 distinct works are adapted; the duplicate Paradise Lost is merged, and the April opening-line note appears within The Waste Land.
- There are 73 additions: the original Odyssey, Antigone and Frankenstein, 50 further canonical works, and 20 new additions: Twelfth Night, The Merchant of Venice, As You Like It, Lycidas, Elegy Written in a Country Churchyard, I Wandered Lonely as a Cloud, Christabel, To a Skylark, Ode on a Grecian Urn, She Walks in Beauty, Persuasion, A Christmas Carol, Ulysses, My Last Duchess, Dover Beach, The Mayor of Casterbridge, Jude the Obscure, The Time Machine, The Windhover and Animal Farm. All 73 have full copies in the 147-page `literature by codex.docx`.
- Every work has twelve scenes. All 1176 card paragraphs and all 98 library hooks have been individually rewritten for the October 10 narration edition. Openings establish place, people and stakes; later cards connect choices to consequences. Suspense comes from each work rather than repeated commands or generic questions. Poems and collections follow their images, arguments and separate voices without invented continuous plots. Scene keys, order, illustrations and saved positions remain compatible.
- Every work has a short quotation, its speaker or textual context, an original memory connection and a linked reference. Quotation wording follows the linked edition. Contemporary works use academic quotation references where full primary texts are unavailable.
- `tools/build_content.py` assembles the original catalogue, the `additions_*.py` modules, `expand_originals.py`, `twelve_scenes.py` and `quotations.py`, then applies `narrative_rewrite.py`. Edit the individually authored paragraphs in `tools/narrative_cards.txt`: each `@id|hook` header has exactly twelve paragraphs. Missing or duplicate works and incorrect paragraph counts fail the build. Run the builder with Python to regenerate `stories.js` and `content/catalog.json`. The website itself requires no Python.
- Reading references remain attached to every work, including online references beside the original-document provenance. These paraphrases are learning adaptations with spoilers, not quotations. The narration review used the existing catalogue and targeted online checks, including [the 1818 Frankenstein text](https://www.gutenberg.org/cache/epub/41445/pg41445-images.html), [Macbeth](https://www.gutenberg.org/files/1533/1533-h/1533-h.htm), [The Duchess of Malfi](https://www.gutenberg.org/files/2232/2232-h/2232-h.htm) and [Coleridge's selected poems](https://dev.gutenberg.org/cache/epub/11101/pg11101-images.html). This was not a fresh line-by-line audit of all 98 primary texts. Existing attributed quotations are unchanged.
- `tools/build_document.py` generates the companion document with python-docx.
- Era divisions are learning aids rather than strict literary-history boundaries. Ordering follows first publication, with approximate composition or performance dates where necessary. Beowulf uses its manuscript-era anchor. A date range is displayed when needed.
- Storyboards use concise original paraphrases. They contain spoilers. Non-narrative poetry is presented through thematic landmarks. Editorial notes record ambiguities and corrections to the supplied notes.
- The palette translates the supplied historical and environmental colors into court, spring, ocean, autumn, night, Gothic, industrial and Igbo-setting palettes. `illustrations.js` gives recurring characters consistent costumes, hair, keepsakes and roles; facial expressions and poses respond to each scene. Animals, birds, the Cyclops, spirits and personified natural forces have distinct forms. Gentle blinking, gesturing, leaf movement and lighting respect reduced-motion preferences. These are symbolic storybook illustrations rather than historical portraits.

## Controls and storage

Click an era, search a title/author/character, and open a story. Next/Previous buttons, scene dots, left/right keys and horizontal swipes on the picture turn pages. At the final scene, Next opens recall. After recall, Explore memorable quotes opens the fourth panel. Escape closes the reader. Tab panels support arrow keys, Home and End. Press `/` to focus search.

The heart saves a work to My shelf. Reading positions, saved works and remembered status are stored only in this browser's localStorage. Both older five/seven-scene positions migrate to matching scenes in the twelve-scene boards; new positions also retain stable scene keys. Favourites and remembered status are preserved. Storage-denied environments remain usable for the current session. Sources & notes contains a two-click reset. The site respects reduced motion and works at mobile widths. Existing scene URLs still use their numeric position within the expanded storyboard.

## Install on a phone and read offline

1. Publish with GitHub Pages and open the resulting **HTTPS** address on the phone. A `file://` preview cannot register a service worker or install this app.
2. On Android Chrome, use **Install the library** when it appears, or Chrome's menu → **Install app / Add to Home screen**. On iPhone, use Safari → Share → Add to Home Screen.
3. Wait for **All 98 stories, illustrations and quotes are ready offline!** before leaving the connection. The manifest opens the installed app in standalone mode. The service worker precaches the HTML, scripts, styles, icons, full story catalogue and companion Word document; illustrations are local SVG code. Linked literary reference websites need a connection. Fonts have offline Georgia/Arial fallbacks.

`manifest.json` uses relative URLs and scope so repository subdirectories work. Icons include 192px, 512px, a separate safely padded maskable icon, and an Apple touch icon. `assets/app-icon.svg` is their source; `tools/build_icons.cjs` rasterises it with Sharp.

When deploying future changes, change the `v4-20261010-narration` release identifier in `sw.js`. The next service worker installs a complete new cache, waits until the reader selects **Update and reopen**, then activates. Cache names include the registration scope, and cleanup leaves other apps' caches intact. Saved reading data lives separately in localStorage and survives updates. Browser site-data deletion removes offline files and saved progress.

## Verification

`tools/check_site.cjs` performs browser interaction checks for all 98 stories and 1176 scenes, filters, searches, persistence, recall, direct links and mobile layouts. `tools/check_expansion.cjs` checks all quotation panels, four-tab navigation, progress migration and mobile quote layouts. `tools/check_extras.cjs` checks focus, touch and storage edge cases. `tools/check_pwa.cjs` serves a temporary localhost site in a repository-style subdirectory and checks the actual Chrome manifest/installability response, service-worker registration, offline reloads, all 98 quote panels offline, cached Word download, update/reload, cache isolation and saved-data preservation. Its Chrome profile is private to QA. These tests do not claim an installation on a physical phone.

`tools/verify_quotations.py` compares 73 Gutenberg excerpts against linked text editions; the other 25 use poetry, university, author or Gutenberg Australia references. QA images, source comparison reports and document renders are kept in `qa/` and are not required for hosting.
