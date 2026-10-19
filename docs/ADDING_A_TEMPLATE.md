# Adding a Template

1. Create `templates/<template-id>/` with these files:
   - `template.yaml` (id, name, version, description, theme)
   - `sections.md` (section blueprint)
   - `questions.md` (what the AI must ask)
   - `data-needs.md` (vendor-neutral data per section)
   - `compliance-map.md` (indicative framework mapping)
   - `theme.yaml` (colors)
2. Design a new palette (a hue not yet used, with strong contrast for white text on the primary color). Record it in `docs/COLOR_PALETTES.md` and add `theme.yaml`.
3. Add one entry to `catalog/templates.yaml`.
4. Rules: no SIEM product names, no real client data, US English.
5. Update the README template table.
