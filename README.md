# Once Upon a Timeline

A static literature library and installable PWA with 158 works and 1896 story cards.

[Open the library](https://ascendesshady.github.io/English-Literature/)

Painting preview: 60 of 158 books have reviewed painted illustrations (720 cards). Remaining books use their existing symbolic drawings while their paintings are prepared or corrected. The complete illustration rollout and final storytelling review remain pending.

Read each story through twelve narrated cards, explore the cast and quotations, and save favourites and reading progress in your browser. Every story has an **Author** tab with a concise biography, sources and a licensed historical portrait where available. Joint authorship and unknown authors are identified explicitly; portrait credits and reuse terms are included. Author profiles and portraits are available offline alongside the stories. Use **Install app** in the top navigation on Chrome. Wait for the offline-ready message before reading without a connection. Existing installed readers can choose **Update and reopen** to receive a release; their saved progress is preserved.

This repository contains only the website, story-card data, paintings and app icons. Source documents, Python build tools, research files and image-generation prompts are retained in the author's local workspace. Paintings are WebP; app icons are PNG/SVG. No account, build step, API key or backend is required.

Paintings use compressed WebP at their original dimensions, with one sheet serving all twelve cards of a book. Packaging enforces a 100 MB website budget and excludes voice models and finished audio recordings. The speech runtime is downloaded only when narration is requested; ordinary reading does not fetch it.

Open `index.html` locally to read. Installation and service-worker caching require the HTTPS site. GitHub Pages can serve these files directly from the repository root.

Choose **Listen** inside any story for gentle, local neural narration. Cards turn automatically when their audio finishes. Pause/resume, stop, replay, voice, pace and Auto turn controls are provided. First use downloads the pinned Kokoro model (about 92 MB) plus the optional browser speech runtime (about 23 MB); no story text is sent to a speech server. Once prepared, the model and runtime work offline in the same browser. The model is fetched from Hugging Face and retained on the device, rather than stored in this repository. Neural narration uses the hosted/installed library; a local file preview links to that library. Software and voice licence notices accompany the runtime assets.

Use **Audio ↓** at the top, **Download narration** beside the installation options, or **Download story** inside a reader to prepare finished narration ahead of time. Choose one story or the full library, with all available voices and paces or just your selected version. Progress, saved size, a storage estimate, pause/resume and an estimate of remaining time are shown. Completed audio persists across reloads and app updates and is keyed to the exact card text, voice and pace. Cached cards play without loading the neural model or synthesising again. The first preparation still runs locally and may take substantial time; keep the app open. Finished WAV audio for the full library is approximately 1 GB for one voice/pace. Clearing browser site data removes it. Normal on-demand listening also saves each completed card automatically.

The default **All voices and paces** option prepares both voices at all four paces: eight versions, 15,168 recordings for the full library (roughly 9 GB), or 96 recordings for one story. You can choose **Selected voice and pace only** for a smaller preparation. Each card's eight versions are prepared together, starting with your current listening voice and pace. Existing completed versions are reused and the whole queue is resumable. These recordings are prepared in each reader's browser; they are not pre-generated server downloads. Saved recordings have no speech-generation delay, with normal device audio startup still applying.
