# Weekly SOC Summary: Section Blueprint

Blueprint for a weekly summary that shows trend against the prior week.

## Section index

| ID | Section | Include |
|---|---|---|
| WS0 | Cover and Document Control | Always |
| WS1 | Week at a Glance | Always |
| WS2 | Alerts and Incidents | Always |
| WS3 | Threat Activity and Intelligence | Always |
| WS4 | Platform and Coverage | Always |
| WS5 | Tuning and Improvements | Always |
| WS6 | Open Items and Next Week | Always |
| WS7 | Sign-Off and Acknowledgement | Always |

## WS0: Cover and Document Control

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

## WS1: Week at a Glance

**Purpose:** Give the headline picture.

**Content blocks**

- Headline measures with change from prior week
- One-paragraph summary

**Inputs from the user**

- Disclosure level

**Data from the SIEM (vendor-neutral)**

- Alert and incident totals
- Timing measures

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## WS2: Alerts and Incidents

**Purpose:** Show workload and outcomes with trend.

**Content blocks**

- Alerts by severity and trend
- Incidents by category and status
- Top rules by volume

**Inputs from the user**

- Severity scheme

**Data from the SIEM (vendor-neutral)**

- Counts by severity and rule
- Case list

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, NIST CSF

## WS3: Threat Activity and Intelligence

**Purpose:** Describe notable threat activity.

**Content blocks**

- Notable campaigns or advisories
- Indicator actions taken
- Relevance to this organization

**Inputs from the user**

- Sector context

**Data from the SIEM (vendor-neutral)**

- Indicator matches
- Blocked sources (aggregated)

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF, CERT-In 2022

## WS4: Platform and Coverage

**Purpose:** Show monitoring health.

**Content blocks**

- Availability
- Source gaps and fixes
- Capacity notes

**Inputs from the user**

- Known issues

**Data from the SIEM (vendor-neutral)**

- Availability
- Silent sources
- Storage trend

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001

## WS5: Tuning and Improvements

**Purpose:** Show what improved.

**Content blocks**

- Rules tuned or added
- Playbook or process changes

**Inputs from the user**

- Changes made

**Data from the SIEM (vendor-neutral)**

- Rule change record

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, MITRE ATT&CK

## WS6: Open Items and Next Week

**Purpose:** Plan ahead.

**Content blocks**

- Open items with owners
- Planned work

**Inputs from the user**

- Plan

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## WS7: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
