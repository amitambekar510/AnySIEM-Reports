# Interview Flow

Ask in small batches. After each batch, restate what you understood in one or
two lines and let the user correct you.

## Stage 0: Menu

Read `catalog/templates.yaml`. Present each available template with its name and
one-line description. Ask: "Which report would you like to build?"

## Stage 1: Context

1. Organization name and the audience (internal leadership, client, auditor, regulator).
2. SOC delivery model: in-house, managed provider, or hybrid. Operating hours.
3. Reporting period (monthly, quarterly, annual, or custom) and audit period.
4. Document classification label and document ID convention.
5. Template mode or populated mode? Exact numbers or diplomatic wording?

## Stage 2: SIEM discovery

Follow `core/siem-discovery.md`. Do not skip this stage.

## Stage 3: Frameworks

Show the framework list from `core/compliance-library.md`. Ask which apply:
regulator, sector, audit type, and any contractual requirement. Map only those.

## Stage 4: Section by section

For each section in the template's `sections.md`:

1. Tell the user the section name and its purpose in one line.
2. Ask only the questions in `questions.md` that belong to it.
3. Offer data you already know from the SIEM profile.
4. Draft the section text, then ask for approval or edits.

Skip conditional sections that do not apply, and say why.

## Stage 5: Extras

Ask: "Is there anything else you want in this report, such as a dashboard
summary, a risk statement, a custom table, or a regulator-specific appendix?"
Add what they request.

## Stage 6: Review

Show the final outline: section titles and page-level flow. Ask for approval.

## Stage 7: Build

Generate the PDF per `core/pdf-output-rules.md`. Share it, then ask whether any
section needs changes.
