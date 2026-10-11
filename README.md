# Once Upon a Timeline

A static literature library and installable PWA with 158 works and 1896 story cards.

[Open the library](https://ascendesshady.github.io/English-Literature/)

Painting preview: 18 of 158 books have reviewed painted illustrations (216 cards). Remaining books use their existing symbolic drawings while their paintings are prepared or corrected. The complete illustration rollout and final storytelling review remain pending.

Read each story through twelve narrated cards, explore the cast and quotations, and save favourites and reading progress in your browser. Every story has an **Author** tab with a concise biography, sources and a licensed historical portrait where available. Joint authorship and unknown authors are identified explicitly; portrait credits and reuse terms are included. Author profiles and portraits are available offline alongside the stories. Use **Install app** in the top navigation on Chrome. Wait for the offline-ready message before reading without a connection. Existing installed readers can choose **Update and reopen** to receive a release; their saved progress is preserved.

This repository contains only the website, story-card data, paintings and app icons. Source documents, Python build tools, research files and image-generation prompts are retained in the author's local workspace. Paintings are WebP; app icons are PNG/SVG. No account, build step, API key or backend is required.

Open `index.html` locally to read. Installation and service-worker caching require the HTTPS site. GitHub Pages can serve these files directly from the repository root.

Choose **Listen** inside any story for gentle, local neural narration. Cards turn automatically when their audio finishes. Pause/resume, stop, replay, voice, pace and Auto turn controls are provided. First use downloads the pinned Kokoro model (about 92 MB) plus the optional browser speech runtime (about 23 MB); no story text is sent to a speech server. Once prepared, the model and runtime work offline in the same browser. The model is fetched from Hugging Face and retained on the device, rather than stored in this repository. Neural narration uses the hosted/installed library; a local file preview links to that library. Software and voice licence notices accompany the runtime assets.
