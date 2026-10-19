# SLA Compliance Report: Section Blueprint

Blueprint for a focused SLA evidence report. For a broader service review, use `sla-quarterly-review`.

## Section index

| ID | Section | Include |
|---|---|---|
| SL0 | Cover and Document Control | Always |
| SL1 | SLA Definitions and Measurement Method | Always |
| SL2 | Performance by Metric | Always |
| SL3 | Breach Register | Always |
| SL4 | Exclusions and Dependencies | Always |
| SL5 | Monitoring Platform Availability | Always |
| SL6 | Remedies and Credits | When the contract defines remedies |
| SL7 | Improvement Actions | Always |
| SL8 | Sign-Off and Acknowledgement | Always |

## SL0: Cover and Document Control

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

## SL1: SLA Definitions and Measurement Method

**Purpose:** Define each SLA and how it is measured.

**Content blocks**

- SLA table (metric, definition, start and stop event, target)
- Business-hours or 24x7 basis
- Time source

**Inputs from the user**

- SLA definitions from the contract

**Data from the SIEM (vendor-neutral)**

- Timestamps used for each measure

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, SEBI CSCRF 2024

## SL2: Performance by Metric

**Purpose:** Report results period by period.

**Content blocks**

- Result per metric per month
- Trend
- Overall compliance statement

**Inputs from the user**

- Results, or generic wording in diplomatic mode

**Data from the SIEM (vendor-neutral)**

- Acknowledgement, response, and resolution timestamps
- Platform availability

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, SEBI CSCRF 2024

**Writing note:** Apply the disclosure level consistently.

## SL3: Breach Register

**Purpose:** Be transparent about misses.

**Content blocks**

- Table: breach, date, cause, responsible party, corrective action

**Inputs from the user**

- Breach details

**Data from the SIEM (vendor-neutral)**

- Records for breached items

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## SL4: Exclusions and Dependencies

**Purpose:** State what the contract excludes.

**Content blocks**

- Maintenance windows
- Client-side delays
- Other contractual exclusions

**Inputs from the user**

- Contract exclusions

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## SL5: Monitoring Platform Availability

**Purpose:** Report platform uptime.

**Content blocks**

- Availability by month
- Outage list with cause

**Inputs from the user**

- Outage details

**Data from the SIEM (vendor-neutral)**

- Availability figures
- Outage records

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber

## SL6: Remedies and Credits

**Purpose:** Record any contractual remedy.

**Include when:** When the contract defines remedies

**Content blocks**

- Remedy calculation as defined in the contract

**Inputs from the user**

- Contract terms

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## SL7: Improvement Actions

**Purpose:** Show what will prevent repeats.

**Content blocks**

- Action table (action, owner, date)

**Inputs from the user**

- Actions

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## SL8: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
