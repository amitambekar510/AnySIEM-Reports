# SOC Operations Report: Section Blueprint

Blueprint for a periodic SOC operations report. Duration and audit period are set during the interview.

## Section index

| ID | Section | Include |
|---|---|---|
| M0 | Cover and Document Control | Always |
| M1 | Executive Summary | Always |
| M2 | Communication and Escalation Contacts | Always |
| M3 | Scope, Infrastructure and Reporting Framework | Always |
| M4 | Platform Health and Data Ingestion | Always |
| M5 | Alert and Incident Summary | Always |
| M6 | Incident Management and Threat Intelligence | Always |
| M7 | Detection Strategy and Coverage | Always |
| M8 | Vulnerability and Patch Posture | Always. If out of scope, show the scope statement and responsibility table only. |
| M9 | Findings, Recommendations and Action Items | Always |
| M10 | Service Level Compliance | Always |
| M11 | Regulatory and Framework Compliance Summary | Always |
| M12 | Advisory Notes and Security Awareness | Always |
| M12A | AI System Security Addendum | When the organization develops or uses AI systems that the SOC monitors |
| M13 | Sign-Off and Acknowledgement | Always |

## M0: Cover and Document Control

**Purpose:** Identify the document, its version, owner, and distribution.

**Content blocks**

- Cover page with period, audience, and classification
- Document control table (ID, version, author, reviewer, approver, issue date)
- Revision history
- Reference to the previous period report

**Inputs from the user**

- Document ID convention
- Author, reviewer, approver roles
- Previous report reference

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## M1: Executive Summary

**Purpose:** Give leadership a clear view of SOC activity and posture for the period.

**Content blocks**

- Purpose and importance of the report
- Confidentiality and data privacy statement
- Key highlights
- Period-at-a-glance scorecard
- Detection rule performance summary

**Inputs from the user**

- Disclosure level (exact or diplomatic)
- Key messages the user wants leadership to see

**Data from the SIEM (vendor-neutral)**

- Total events ingested for the period
- Number of onboarded log sources
- Platform availability for the period
- Alerts triaged and incidents escalated
- Detection and response timing as measured
- Detection rule trigger counts and tuning status

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, NIST CSF

**Writing note:** State timing metrics honestly. If detection time depends on log delivery latency, say so.

## M2: Communication and Escalation Contacts

**Purpose:** Show who talks to whom, and how incidents are escalated.

**Content blocks**

- Client-side contacts by role
- SOC contacts by role
- Escalation path

**Inputs from the user**

- Role titles (use roles, not personal names, if the user prefers)
- Escalation levels and timing

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, ISO/IEC 27001

## M3: Scope, Infrastructure and Reporting Framework

**Purpose:** Define what the SOC monitors and how.

**Content blocks**

- Collector or forwarder inventory
- Service scope summary
- Infrastructure coverage by category
- Component and agent versions

**Inputs from the user**

- Services in scope and out of scope
- Environments and locations covered

**Data from the SIEM (vendor-neutral)**

- Log source inventory by category
- Collector or forwarder list and status
- Component and agent versions

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001, SEBI CSCRF 2024

## M4: Platform Health and Data Ingestion

**Purpose:** Evidence that monitoring data was collected completely and reliably.

**Content blocks**

- Platform health overview
- Daily ingestion volume
- Log source health table (status, event rate, last seen)
- Retention settings (hot, warm, archive)
- Time synchronization statement

**Inputs from the user**

- Required retention periods
- Known outages or gaps and their causes

**Data from the SIEM (vendor-neutral)**

- Platform health indicators
- Daily event volume
- Per-source status, event rate, last-seen time
- Retention configuration
- Time synchronization status

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001, RBI IT/Cyber, NSE/BSE Tech Audit

## M5: Alert and Incident Summary

**Purpose:** Summarize alert load and incident handling for the period.

**Content blocks**

- Alerts by severity (opened and closed)
- Alert volume chart
- Incidents handled with classification and status

**Inputs from the user**

- Severity scheme and definitions
- Incident reference format

**Data from the SIEM (vendor-neutral)**

- Alert counts by severity
- Alert status
- Incident or case list with category, severity, status

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, NIST CSF, ISO/IEC 27001

## M6: Incident Management and Threat Intelligence

**Purpose:** Describe how incidents and threat intelligence were managed.

**Content blocks**

- Incident management summary by type and priority
- Incident response lifecycle
- Threat intelligence and IOC management (generic wording if the user prefers)
- Malicious IP and top-talker intelligence with required client action
- Regulatory and statutory reporting summary
- Escalation matrix
- Dashboard access control and MFA status

**Inputs from the user**

- Threat intelligence source types (open, community, commercial). Names stay private unless the user shares them
- Required client action wording
- Reporting obligations that applied this period
- User and role counts for the monitoring platform

**Data from the SIEM (vendor-neutral)**

- Incident counts by type and priority
- IOC match counts
- Top external talkers
- Platform user and role inventory
- Authentication settings

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, DPDP Act 2023, SEBI CSCRF 2024, ISO/IEC 27001, MITRE ATT&CK, NPCI/UPI

**Writing note:** Keep regulatory statements generic unless the user supplies verified figures.

## M7: Detection Strategy and Coverage

**Purpose:** Show what the SOC can and cannot detect.

**Content blocks**

- Default detection content
- Custom, client-specific use cases
- ATT&CK coverage view with honest gaps
- AI system detection coverage (when AI systems are in scope)

**Inputs from the user**

- Links or references to rule documentation
- Planned detection improvements

**Data from the SIEM (vendor-neutral)**

- Count of active detection rules by type
- Rules mapped to ATT&CK tactics and techniques
- Custom rule list

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF, ISO/IEC 27001, ISO/IEC 27090

**Writing note:** Explain that coverage reflects the number of mapped rules, not a guarantee of detection.

## M8: Vulnerability and Patch Posture

**Purpose:** State vulnerability management scope and results.

**Include when:** Always. If out of scope, show the scope statement and responsibility table only.

**Content blocks**

- Scope statement
- Responsibility boundary table
- Findings (if in scope)
- Conditions to activate this section (if out of scope)

**Inputs from the user**

- Is vulnerability management in scope?
- Responsibility owner for scanning and patching

**Data from the SIEM (vendor-neutral)**

- Vulnerability scan data forwarded to the SIEM (if any)

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, NSE/BSE Tech Audit

## M9: Findings, Recommendations and Action Items

**Purpose:** Turn observations into tracked actions.

**Content blocks**

- Findings table (observation, recommendation, owner, priority)
- Feedback invitation for tuning and whitelisting

**Inputs from the user**

- Findings and owners
- Remediation targets

**Data from the SIEM (vendor-neutral)**

- Source health gaps
- Detection gaps
- Unavailable data items from this report

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## M10: Service Level Compliance

**Purpose:** Report SLA performance.

**Content blocks**

- SLA table (metric, target, result)

**Inputs from the user**

- SLA metrics and targets
- Result per metric, or a generic statement in diplomatic mode

**Data from the SIEM (vendor-neutral)**

- Acknowledgement and response timestamps
- Platform availability

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, SEBI CSCRF 2024

## M11: Regulatory and Framework Compliance Summary

**Purpose:** Show control-by-control evidence against the frameworks the user selected.

**Content blocks**

- Control domain table (reference, domain, status, evidence)

**Inputs from the user**

- Selected frameworks
- Evidence references

**Data from the SIEM (vendor-neutral)**

- Evidence extracts such as retention and monitoring reports

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023, ISO/IEC 27001, MITRE ATT&CK, NIST CSF, NSE/BSE Tech Audit, NPCI/UPI, SEBI PFUTP 2003

**Writing note:** Use only frameworks the user selected. Mark unverified items 'to be confirmed'.

## M12: Advisory Notes and Security Awareness

**Purpose:** Share service assurance and practical security recommendations.

**Content blocks**

- Service assurance statements the user can support
- Defense-in-depth recommendations
- Security awareness guidance written directly in the report

**Inputs from the user**

- Which recommendations to include

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

**Writing note:** No third-party links unless requested.

## M12A: AI System Security Addendum

**Purpose:** Report on monitoring of AI systems the organization develops or uses.

**Include when:** When the organization develops or uses AI systems that the SOC monitors

**Content blocks**

- AI systems in scope and their owners
- Assets that need protection (training data, models)
- AI-specific threat activity observed
- Monitoring gaps for AI systems

**Inputs from the user**

- Which AI systems are in scope
- Owners and lifecycle stage

**Data from the SIEM (vendor-neutral)**

- Logs from AI platforms and model access
- Unusual query or data-change events

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, ISO/IEC 42001, ISO/IEC 27001, NIST CSF, MITRE ATT&CK

**Writing note:** Use only the user's own inputs about their AI systems. Do not reproduce text from the standard.

## M13: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review and acknowledgement.

**Content blocks**

- Team-level sign-off table
- Acknowledgement checkboxes
- Optional stamp or seal area
- Disclaimer

**Inputs from the user**

- Sign-off roles for each side

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
