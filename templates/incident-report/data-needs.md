# Security Incident Report: Data Needs

Vendor-neutral list of the data each section needs. Use the SIEM profile to decide where each item comes from.

| Section | Data needed | If unavailable |
|---|---|---|
| I1 Incident Summary | Alert or case ID; Detection timestamp; Affected hosts and addresses | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| I2 Incident Classification | Detection rule or use case name; ATT&CK mapping of the triggered rule | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| I3 Incident Timeline | Alert time; Analyst action times; Containment and closure times | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| I4 Technical Details and Indicators | Source and destination addresses; File hashes, domains, URLs if present; Log sources involved | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| I5 Root Cause Analysis | Time from first event to detection; Visibility gaps found | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| I6 Impact Assessment | Evidence of data access or transfer | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
| I8 Recommendations and Corrective Actions | Detection tuning opportunities | Ask the user. If still unavailable, mark as not available from the current configuration and offer to list it under Findings. |
