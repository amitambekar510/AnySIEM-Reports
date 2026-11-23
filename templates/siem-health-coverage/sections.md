# SIEM Health and Coverage Report: Section Blueprint

Blueprint for a platform health and monitoring coverage report. Written for any SIEM; the AI maps the user's platform data during the interview.

## Section index

| ID | Section | Include |
|---|---|---|
| H0 | Cover and Document Control | Always |
| H1 | Executive Summary | Always |
| H2 | Platform Health | Always |
| H3 | Log Source Inventory and Coverage | Always |
| H4 | Ingestion Quality | Always |
| H5 | Retention, Storage and Integrity | Always |
| H6 | Collector, Forwarder and Agent Health | Always |
| H7 | Access, Configuration and Change Control | Always |
| H8 | Coverage Gaps and Risk Assessment | Always |
| H9 | Recommendations and Remediation Plan | Always |
| H10 | Sign-Off and Acknowledgement | Always |

## H0: Cover and Document Control

**Purpose:** Identify the report, period, and owner.

**Content blocks**

- Cover
- Document control table
- Revision history

**Inputs from the user**

- Document ID format
- Author, reviewer, approver roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## H1: Executive Summary

**Purpose:** Give a plain-language view of platform health and monitoring coverage.

**Content blocks**

- Overall health statement
- Coverage statement
- Top risks and actions

**Inputs from the user**

- Disclosure level
- Messages leadership must see

**Data from the SIEM (vendor-neutral)**

- Availability for the period
- Number of sources onboarded vs expected
- Count of unresolved gaps

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, NIST CSF

## H2: Platform Health

**Purpose:** Show that the monitoring platform itself is reliable.

**Content blocks**

- Component status table
- Availability and performance
- Capacity indicators
- Upgrade and patch status of platform components

**Inputs from the user**

- Known outages and causes
- Planned maintenance

**Data from the SIEM (vendor-neutral)**

- Component or node status
- Availability figures
- CPU, memory, storage and queue indicators
- Platform version and update status

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, NSE/BSE Tech Audit

## H3: Log Source Inventory and Coverage

**Purpose:** Show what is monitored, what should be, and the difference.

**Content blocks**

- Inventory by category (network, endpoint, identity, server, application, cloud)
- Expected vs onboarded sources
- Coverage of critical assets
- Coverage by site or business unit
- AI platform and model-hosting log sources (when AI systems are in scope)

**Inputs from the user**

- Authoritative asset list or CMDB extract
- Which assets are critical
- Out-of-scope assets and reasons

**Data from the SIEM (vendor-neutral)**

- Onboarded source list with category
- Last-seen time per source
- Parser or integration used per source

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, ISO/IEC 27090

## H4: Ingestion Quality

**Purpose:** Show that data arrives completely, on time, and in usable form.

**Content blocks**

- Daily volume and event rate trend
- Parsing and normalization success
- Ingestion latency
- Silent or degraded sources
- Dropped or duplicate events
- Time synchronization status

**Inputs from the user**

- Latency expectations
- Time source used

**Data from the SIEM (vendor-neutral)**

- Daily volume
- Event rate per source
- Parse failure counts
- Ingest-to-index delay
- Sources with no data in the period
- Time drift indicators

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001, RBI IT/Cyber

## H5: Retention, Storage and Integrity

**Purpose:** Evidence that data is kept as long as required and protected.

**Content blocks**

- Retention tiers and periods
- Storage capacity and forecast
- Integrity and access controls on stored logs
- Backup and recovery of platform configuration

**Inputs from the user**

- Required retention periods
- Storage location (for residency statements)

**Data from the SIEM (vendor-neutral)**

- Retention configuration
- Storage usage and growth
- Integrity or immutability features in use
- Backup status

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, DPDP Act 2023, ISO/IEC 27001, RBI IT/Cyber, NSE/BSE Tech Audit

## H6: Collector, Forwarder and Agent Health

**Purpose:** Show the data collection layer is healthy and current.

**Content blocks**

- Collector and agent inventory
- Version currency
- Backlog and error counts
- Connectivity issues

**Inputs from the user**

- Approved versions
- Known connectivity limits

**Data from the SIEM (vendor-neutral)**

- Collector or agent list and status
- Version per collector or agent
- Backlog or buffer indicators
- Error counts

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## H7: Access, Configuration and Change Control

**Purpose:** Show the platform is administered under control.

**Content blocks**

- Role-based access summary
- Authentication strength (such as MFA)
- Administrative activity review
- Configuration and rule change record

**Inputs from the user**

- Access review date and outcome
- Change approval process

**Data from the SIEM (vendor-neutral)**

- User and role inventory
- Authentication settings
- Admin audit log summary
- Configuration change history

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, SEBI CSCRF 2024, NIST CSF

## H8: Coverage Gaps and Risk Assessment

**Purpose:** Name the gaps and what they mean for detection.

**Content blocks**

- Gap register (gap, affected assets, detection impact, owner, target date)
- Risk rating per gap

**Inputs from the user**

- Risk scale
- Owners

**Data from the SIEM (vendor-neutral)**

- Missing source categories
- Sources with partial logging
- Detection use cases blocked by missing data

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, NIST CSF, MITRE ATT&CK

**Writing note:** State gaps plainly. A reported gap is evidence of a working review process.

## H9: Recommendations and Remediation Plan

**Purpose:** Convert gaps into tracked actions.

**Content blocks**

- Action table (action, owner, priority, due date)

**Inputs from the user**

- Agreed owners and dates

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## H10: Sign-Off and Acknowledgement

**Purpose:** Record review.

**Content blocks**

- Team-level sign-off
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
