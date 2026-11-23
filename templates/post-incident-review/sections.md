# Post-Incident Review: Section Blueprint

Blueprint for a blameless post-incident review. It complements the Security Incident Report.

## Section index

| ID | Section | Include |
|---|---|---|
| PR0 | Cover and Document Control | Always |
| PR1 | Incident Recap | Always |
| PR2 | What Went Well | Always |
| PR3 | What Did Not Go Well | Always |
| PR4 | Detection and Response Review | Always |
| PR5 | Contributing Factors | Always |
| PR6 | Lessons Learned | Always |
| PR7 | Corrective Action Tracking | Always |
| PR8 | Process and Playbook Changes | Always |
| PR9 | Sign-Off and Acknowledgement | Always |

## PR0: Cover and Document Control

**Purpose:** Identify the document, period, and owner.

**Content blocks**

- Cover with title, period, and classification
- Document control table

**Inputs from the user**

- Document ID format
- Author, reviewer, approver roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## PR1: Incident Recap

**Purpose:** Summarize the incident and link to its report.

**Content blocks**

- Reference to the incident report
- Short factual recap

**Inputs from the user**

- Incident ID

**Data from the SIEM (vendor-neutral)**

- Case reference

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## PR2: What Went Well

**Purpose:** Record effective practices.

**Content blocks**

- Detection, response, and communication strengths

**Inputs from the user**

- Observations

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## PR3: What Did Not Go Well

**Purpose:** Record gaps without blame.

**Content blocks**

- Delays, misses, and friction points

**Inputs from the user**

- Observations

**Data from the SIEM (vendor-neutral)**

- Time gaps between key events

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

**Writing note:** Keep the review blameless. Describe systems and processes, not individuals.

## PR4: Detection and Response Review

**Purpose:** Compare actual to expected.

**Content blocks**

- Timeline against targets
- Key decision points and their rationale

**Inputs from the user**

- Targets

**Data from the SIEM (vendor-neutral)**

- Alert, acknowledgement, containment, and closure times

**Compliance hooks (indicative, verify before citing):** SEBI CSCRF 2024, RBI IT/Cyber, NIST CSF

## PR5: Contributing Factors

**Purpose:** Group causes.

**Content blocks**

- People, process, technology, and external factors

**Inputs from the user**

- Known factors

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## PR6: Lessons Learned

**Purpose:** State what changes.

**Content blocks**

- Lessons, each with the change it triggers

**Inputs from the user**

- Lessons

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## PR7: Corrective Action Tracking

**Purpose:** Track follow-through.

**Content blocks**

- Action table (action, owner, due, status)

**Inputs from the user**

- Actions

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## PR8: Process and Playbook Changes

**Purpose:** Record updates.

**Content blocks**

- Playbooks, runbooks, and detections changed

**Inputs from the user**

- Changes

**Data from the SIEM (vendor-neutral)**

- Rule or playbook change record

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, MITRE ATT&CK

## PR9: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
