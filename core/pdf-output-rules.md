# PDF Output Rules

The deliverable is **one PDF file**. You decide which tool or library to use,
based on what your environment supports.

## Required

- Page size: ask the user (A4 or US Letter). Default to A4.
- Embedded fonts, selectable text, and a bookmark outline that follows the
  section headings.
- Cover page, document control table, and a table of contents.
- Header and footer on every page after the cover (classification, page number).
- Theme colors from the template's `theme.yaml`.
- Tables must not split awkwardly. Repeat table header rows across pages.
- Placeholders (template mode) must be visually distinct, for example in
  brackets with a light highlight.

## Branding (see `core/branding.yaml`)

- **Watermark:** the project name, diagonal, very light (opacity 8 percent or
  lower), so text stays readable.
- **Footer:** the attribution line, plus page number.
- Both are optional. If the user asks to remove them, remove them.

## Quality check before delivery

1. Render the pages to images, if your environment allows it.
2. Look for cut-off text, overflowing tables, low contrast, and blank pages.
3. Fix problems and re-render.
4. Report any limits honestly, such as "charts were drawn as tables".
