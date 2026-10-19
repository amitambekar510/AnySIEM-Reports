# SIEM Health and Coverage Report: Data Needs

Vendor-neutral list of the data each section needs. Use the SIEM profile to decide where each item comes from.

| Section | Data needed | If unavailable |
|---|---|---|
| H1 Executive Summary | Availability for the period; Number of sources onboarded vs expected; Count of unresolved gaps | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| H2 Platform Health | Component or node status; Availability figures; CPU, memory, storage and queue indicators; Platform version and update status | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| H3 Log Source Inventory and Coverage | Onboarded source list with category; Last-seen time per source; Parser or integration used per source | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| H4 Ingestion Quality | Daily volume; Event rate per source; Parse failure counts; Ingest-to-index delay; Sources with no data in the period; Time drift indicators | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| H5 Retention, Storage and Integrity | Retention configuration; Storage usage and growth; Integrity or immutability features in use; Backup status | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| H6 Collector, Forwarder and Agent Health | Collector or agent list and status; Version per collector or agent; Backlog or buffer indicators; Error counts | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| H7 Access, Configuration and Change Control | User and role inventory; Authentication settings; Admin audit log summary; Configuration change history | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| H8 Coverage Gaps and Risk Assessment | Missing source categories; Sources with partial logging; Detection use cases blocked by missing data | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
