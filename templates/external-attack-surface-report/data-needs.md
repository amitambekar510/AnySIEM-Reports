# External Attack Surface Report: Data Needs

Vendor-neutral list of the data each section needs. Use the SIEM profile to decide where each item comes from.

| Section | Data needed | If unavailable |
|---|---|---|
| EA2 Asset Discovery Summary | Discovery results if available | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| EA3 Exposed Services | Perimeter traffic and scan-attempt data | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| EA4 Certificates and DNS Hygiene | DNS and certificate telemetry if available | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| EA6 Risk Prioritization | Attack attempts against exposed services | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
