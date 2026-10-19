# Regulatory Notification Report: Section Blueprint

Blueprint for documenting regulatory and stakeholder notifications. The AI drafts the record only. The organization decides and submits.

## Section index

| ID | Section | Include |
|---|---|---|
| RN0 | Cover and Document Control | Always |
| RN1 | Incident Reference and Reportability Assessment | Always |
| RN2 | Applicable Obligations | Always |
| RN3 | Notification Content | Always |
| RN4 | Submission Record | Always |
| RN5 | Follow-up and Supplementary Reports | Always |
| RN6 | Affected Party Communication | When personal data or customers were affected |
| RN7 | Decision Log | Always |
| RN8 | Sign-Off and Acknowledgement | Always |

## RN0: Cover and Document Control

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

## RN1: Incident Reference and Reportability Assessment

**Purpose:** Record whether and why reporting applied.

**Content blocks**

- Incident reference
- Reportability decision, reasoning, and who decided
- Date and time the incident was noticed

**Inputs from the user**

- Decision and decision maker
- Notice time

**Data from the SIEM (vendor-neutral)**

- Detection timestamp

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023, NPCI/UPI, NSE/BSE Tech Audit

**Writing note:** The reportability decision belongs to the organization's compliance or legal owner.

## RN2: Applicable Obligations

**Purpose:** List the duties that applied.

**Content blocks**

- Table: regulator, obligation, deadline, source reference

**Inputs from the user**

- Applicable obligations

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023, NPCI/UPI, NSE/BSE Tech Audit, SEBI PFUTP 2003

**Writing note:** Verify every deadline and reference against current official text. Never state a deadline from memory.

## RN3: Notification Content

**Purpose:** Record what was reported.

**Content blocks**

- Nature of the incident
- Systems and data involved
- Impact
- Actions taken
- Contact point

**Inputs from the user**

- Confirmed facts only

**Data from the SIEM (vendor-neutral)**

- Evidence extracts

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023

**Writing note:** Report confirmed facts and label anything uncertain.

## RN4: Submission Record

**Purpose:** Prove timely submission.

**Content blocks**

- Date and time submitted
- Channel
- Reference or acknowledgement number
- Time elapsed since the incident was noticed

**Inputs from the user**

- Submission details

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, NPCI/UPI, NSE/BSE Tech Audit

## RN5: Follow-up and Supplementary Reports

**Purpose:** Track further reporting.

**Content blocks**

- Updates and final report dates
- Regulator queries and responses

**Inputs from the user**

- Follow-ups

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023

## RN6: Affected Party Communication

**Purpose:** Record notices to affected people or customers.

**Include when:** When personal data or customers were affected

**Content blocks**

- Who was notified, when, and how
- Content summary

**Inputs from the user**

- Communication details

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** DPDP Act 2023, RBI IT/Cyber, NPCI/UPI

## RN7: Decision Log

**Purpose:** Record reasoning, especially for decisions not to report.

**Content blocks**

- Decision, reason, approver, date

**Inputs from the user**

- Decisions

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023

## RN8: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
