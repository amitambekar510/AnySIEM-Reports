# SOC Operations Report: Data Needs

Vendor-neutral list of the data each section needs. Use the SIEM profile to decide where each item comes from.

| Section | Data needed | If unavailable |
|---|---|---|
| M1 Executive Summary | Total events ingested for the period; Number of onboarded log sources; Platform availability for the period; Alerts triaged and incidents escalated; Detection and response timing as measured; Detection rule trigger counts and tuning status | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M3 Scope, Infrastructure and Reporting Framework | Log source inventory by category; Collector or forwarder list and status; Component and agent versions | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M4 Platform Health and Data Ingestion | Platform health indicators; Daily event volume; Per-source status, event rate, last-seen time; Retention configuration; Time synchronization status | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M5 Alert and Incident Summary | Alert counts by severity; Alert status; Incident or case list with category, severity, status | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M6 Incident Management and Threat Intelligence | Incident counts by type and priority; IOC match counts; Top external talkers; Platform user and role inventory; Authentication settings | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M7 Detection Strategy and Coverage | Count of active detection rules by type; Rules mapped to ATT&CK tactics and techniques; Custom rule list | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M8 Vulnerability and Patch Posture | Vulnerability scan data forwarded to the SIEM (if any) | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M9 Findings, Recommendations and Action Items | Source health gaps; Detection gaps; Unavailable data items from this report | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M10 Service Level Compliance | Acknowledgement and response timestamps; Platform availability | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M11 Regulatory and Framework Compliance Summary | Evidence extracts such as retention and monitoring reports | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| M12A AI System Security Addendum | Logs from AI platforms and model access; Unusual query or data-change events | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
