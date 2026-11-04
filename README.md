# CV Editor

A free CV and cover letter editor that runs entirely in your browser. Pick a design, fill in your details, drag things into place, and save it as a PDF. Nothing is uploaded anywhere: your CV never leaves your computer.

![The editor with the Solid sidebar design](docs/editor.png)

## Use it

**Online:** open the GitHub Pages link for this repository (see *Publishing* below).

**Offline:** download `index.html` and open it in Chrome, Edge or Firefox. It's one self-contained file, with no installation and no internet needed.

Then:

1. Choose **Start from the example** or **Start blank**.
2. Edit on the left. The preview on the right updates as you type.
3. Click **Save as PDF / Print** and choose **Save as PDF** as the printer.

## Features

- **Six designs:** Blueprint, Solid sidebar, Banner, Timeline, Minimal and Classic. Each works with a left sidebar, a right sidebar or one column, three font styles and any colour.
- **Drag and drop** sections, jobs and bullet points in the preview, including between columns and pages. Click anything in the preview to jump to it in the editor.
- **Matching cover letter:** the same header, design and colours as your CV.
- **Versions:** keep one CV per job application, with duplicate, rename and delete.
- **Checks:** finds common mistakes such as missing contact details, leftover example text, missing or inconsistent dates, long bullets, empty sections and content that doesn't fit the page.
- **Keyword checker:** paste a job posting to see which of its key terms are already in your CV and which are missing, and how the posting uses each one.
- **Top image:** a certification badge, logo or photo, with crop, zoom and shape options, or a text box such as "Exam scheduled".
- **One or two pages**, and **Compact / Normal / Roomy** density to make things fit.
- **Hide without deleting:** leave a section or job off one version and keep it for the next.
- **Copy as text** for job portals that ask you to paste your CV.
- **Undo** (Ctrl+Z) for edits, moves and deletions.

![All six designs](docs/designs.png)

## Your data

- Everything is stored in your own browser's local storage. Nothing is sent to a server.
- Because of that, your versions exist **only in the browser you used**. Clearing browser data, or switching computer or browser, means they're not there.
- Use **Backup** to download all versions in one file, and **Backup → Restore** to bring them back. **Save file** saves the current version only.
- Don't commit your own CV or backup files to a public repository. The included `.gitignore` excludes `.json` files for that reason.

## Printing tips

- **Chrome / Edge:** choose *Save as PDF*, set margins to *None* or *Default*, and keep *Background graphics* on.
- **Firefox:** under *More settings*, tick *Print backgrounds* and untick *Print headers and footers*.
- **Safari:** choose *PDF → Save as PDF* in the print dialog.

Links (email, phone, LinkedIn) stay clickable in the PDF.

## Publishing with GitHub Pages

1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Under *Build and deployment*, choose **Deploy from a branch**, then pick the `main` branch and the `/ (root)` folder, and save.
4. After a minute or two, the editor is live at `https://<your-username>.github.io/<repository-name>/`.

## Development

The page is built from a few source files into a single `index.html`:

```
src/template.html   the editor: layout, styles and code
src/keywords.js     the keyword checker
src/fonts/          the embedded fonts (WOFF) and their licence
build.py            combines the above into index.html
```

After changing anything in `src/`, rebuild with:

```
python build.py
```

No packages are needed, just Python 3.

## Credits

The embedded fonts are subsets of open-source fonts, licensed under the [SIL Open Font License 1.1](src/fonts/OFL.txt). They are renamed inside the files (CV Serif, CV Sans, CV Head), as the licence asks for modified versions.

- **Lora**: Copyright 2011 The Lora Project Authors, with Reserved Font Name "Lora".
- **Carlito**: Copyright 2010–2013 tyPoland Łukasz Dziedzic, with Reserved Font Name "Carlito".
- **Poppins**: Copyright 2020 The Poppins Project Authors.
