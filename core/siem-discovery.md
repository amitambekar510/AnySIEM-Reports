# SIEM Discovery Procedure

Goal: understand the user's SIEM well enough to map its data to each report
section, without assuming anything.

## Step 1: Ask

Ask for: product name and version, deployment (on-premises, cloud, hybrid),
single or multi-tenant, and which modules are enabled.

## Step 2: Research

Search the internet for the product's **current** capabilities. Prefer official
vendor documentation and release notes. Collect:

- Supported log source types and collection methods
- Detection content: rule types, correlation, anomaly detection, threat
  intelligence integration, ATT&CK mapping support
- Dashboards and reporting features, and export options (PDF, CSV, API)
- Case or incident management features
- Data retention and storage tiers
- Health and ingestion monitoring features
- Access control, authentication, and audit logging features

Record the source and date for each finding. If sources conflict, say so.

## Step 3: Build the profile

Create a SIEM profile using the schema below. Keep it in the conversation. Do
not write it into this repository.

```yaml
siem_profile:
  product: ""
  version: ""
  deployment: ""        # on-premises | cloud | hybrid
  tenancy: ""           # single | multi
  sources_checked:      # official URLs and the date you checked them
    - url: ""
      checked_on: ""
  log_collection: []
  detection_features: []
  threat_intel_integration: ""
  attack_mapping: ""    # supported | partial | none | unknown
  dashboards: []
  export_options: []
  case_management: ""
  retention: ""
  health_monitoring: ""
  access_control: []
  confirmed_by_user: false
  gaps_to_ask_user: []
```

## Step 4: Confirm and fill gaps

Show the user a short summary of what you found. Ask them to confirm or correct
it. For every item you could not find, ask the user directly. Add their answers
to the profile.

## Step 5: Map to the template

Use the template's `data-needs.md` to decide, for each section, which SIEM
feature supplies the data. If none does, apply the fallback rule in
`AI_INSTRUCTIONS.md`, section 6.
