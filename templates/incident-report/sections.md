# Security Incident Report: Section Blueprint

Blueprint for a single security incident report.

## Section index

| ID | Section | Include |
|---|---|---|
| I0 | Cover and Document Control | Always |
| I1 | Incident Summary | Always |
| I2 | Incident Classification | Always |
| I3 | Incident Timeline | Always |
| I4 | Technical Details and Indicators | Always |
| I5 | Root Cause Analysis | Always |
| I6 | Impact Assessment | Always |
| I7 | Regulatory and Stakeholder Notification Record | When any regulator, exchange, network operator, or data protection obligation may apply |
| I8 | Recommendations and Corrective Actions | Always |
| I9 | Communication and Escalation Log | Always |
| I10 | Sign-Off and Acknowledgement | Always |

## I0: Cover and Document Control

**Purpose:** Identify the report and link it to the periodic report.

**Content blocks**

- Cover with incident ID, severity, classification
- Document control table
- Reference to the related periodic report

**Inputs from the user**

- Incident ID format
- Roles for author, reviewer, approver

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## I1: Incident Summary

**Purpose:** Give a fast, factual overview.

**Content blocks**

- Incident facts table (title, source, detection, containment, closure, status)
- Affected assets
- Business impact
- Executive brief in plain language

**Inputs from the user**

- Title and short description
- Who reported or detected it

**Data from the SIEM (vendor-neutral)**

- Alert or case ID
- Detection timestamp
- Affected hosts and addresses

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, ISO/IEC 27001

## I2: Incident Classification

**Purpose:** Classify the incident consistently for response and reporting.

**Content blocks**

- Severity classification
- NIST-style incident category
- CERT-In incident type (if applicable)
- MITRE ATT&CK tactic and technique mapping
- AI-specific incident type (when an AI system was involved)

**Inputs from the user**

- Severity scheme
- Whether CERT-In type applies

**Data from the SIEM (vendor-neutral)**

- Detection rule or use case name
- ATT&CK mapping of the triggered rule

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, NIST CSF, MITRE ATT&CK, ISO/IEC 27001, ISO/IEC 27090

**Writing note:** Confirm the CERT-In incident type list from the current Directions before citing it.

## I3: Incident Timeline

**Purpose:** Show what happened and when.

**Content blocks**

- Time-ordered table (date, time, event or action)

**Inputs from the user**

- Time zone
- Key actions taken by whom

**Data from the SIEM (vendor-neutral)**

- Alert time
- Analyst action times
- Containment and closure times

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001, NIST CSF

## I4: Technical Details and Indicators

**Purpose:** Provide technical evidence.

**Content blocks**

- Affected systems table
- Indicators of compromise table
- Detection details (rule, log sources, method)
- Evidence references

**Inputs from the user**

- Evidence the user is allowed to include

**Data from the SIEM (vendor-neutral)**

- Source and destination addresses
- File hashes, domains, URLs if present
- Log sources involved

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, ISO/IEC 27001, NIST CSF

## I5: Root Cause Analysis

**Purpose:** Identify why the incident happened and why it was not prevented earlier.

**Content blocks**

- Root cause statement
- Contributing factors
- Five-why analysis
- Detection and response gap analysis

**Inputs from the user**

- Known cause
- Detection and response timing in plain terms

**Data from the SIEM (vendor-neutral)**

- Time from first event to detection
- Visibility gaps found

**Compliance hooks (indicative, verify before citing):** SEBI CSCRF 2024, ISO/IEC 27001, NIST CSF, RBI IT/Cyber

**Writing note:** Keep gap analysis diplomatic and factual. Avoid blame.

## I6: Impact Assessment

**Purpose:** Assess confidentiality, integrity, and availability impact.

**Content blocks**

- Impact table
- Estimated downtime
- Data exposure statement
- Personal data involvement assessment
- Impact on AI models or training data (when applicable)

**Inputs from the user**

- Whether personal data was involved
- Downtime

**Data from the SIEM (vendor-neutral)**

- Evidence of data access or transfer

**Compliance hooks (indicative, verify before citing):** DPDP Act 2023, CERT-In 2022, RBI IT/Cyber, NPCI/UPI, ISO/IEC 27090

## I7: Regulatory and Stakeholder Notification Record

**Purpose:** Document who was notified, when, and why (or why not).

**Include when:** When any regulator, exchange, network operator, or data protection obligation may apply

**Content blocks**

- Notification table (recipient, obligation, deadline, sent time, reference)
- Decision record for notifications not made

**Inputs from the user**

- Applicable regulators and obligations
- Times and reference numbers

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023, NSE/BSE Tech Audit, NPCI/UPI, SEBI PFUTP 2003

**Writing note:** Never state a deadline you have not verified.

## I8: Recommendations and Corrective Actions

**Purpose:** Prevent recurrence.

**Content blocks**

- Action table (recommendation, rationale, priority, owner, due date)
- Strategic preventive measures
- Lessons learned

**Inputs from the user**

- Owners and due dates

**Data from the SIEM (vendor-neutral)**

- Detection tuning opportunities

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, NIST CSF

## I9: Communication and Escalation Log

**Purpose:** Record communications during the incident.

**Content blocks**

- Log table (date and time, mode, recipient role, summary)

**Inputs from the user**

- Communications that occurred

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001

## I10: Sign-Off and Acknowledgement

**Purpose:** Record review and acknowledgement.

**Content blocks**

- Team-level sign-off table
- Optional stamp area
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
