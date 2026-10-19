# SOC Risk Register Report: Section Blueprint

Blueprint for reporting SOC and monitoring risks. Use the organization's own risk method.

## Section index

| ID | Section | Include |
|---|---|---|
| RR0 | Cover and Document Control | Always |
| RR1 | Risk Method | Always |
| RR2 | Register Summary | Always |
| RR3 | Risk Detail | Always |
| RR4 | New, Changed and Closed Risks | Always |
| RR5 | Risks Needing Decision | Always |
| RR6 | Risk Trends | Always |
| RR7 | Sign-Off and Acknowledgement | Always |

## RR0: Cover and Document Control

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

## RR1: Risk Method

**Purpose:** Define how risks are rated.

**Content blocks**

- Likelihood and impact scales
- Risk appetite
- Review cadence

**Inputs from the user**

- Method and appetite

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, RBI IT/Cyber, SEBI CSCRF 2024, ISO/IEC 42001

## RR2: Register Summary

**Purpose:** Give the overview.

**Content blocks**

- Counts by rating
- Movement since last period

**Inputs from the user**

- Disclosure level

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## RR3: Risk Detail

**Purpose:** List risks.

**Content blocks**

- Table: risk, cause, impact, likelihood, rating, existing controls, owner, treatment, due date
- AI-system security risks (when AI systems are in scope)

**Inputs from the user**

- Risks

**Data from the SIEM (vendor-neutral)**

- Evidence from monitoring (coverage gaps, incident trends)

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, RBI IT/Cyber, SEBI CSCRF 2024, ISO/IEC 27090, ISO/IEC 42001

## RR4: New, Changed and Closed Risks

**Purpose:** Show change.

**Content blocks**

- New risks
- Rating changes
- Closed risks and reasons

**Inputs from the user**

- Changes

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## RR5: Risks Needing Decision

**Purpose:** Ask for decisions.

**Content blocks**

- Risks requiring acceptance, funding, or escalation

**Inputs from the user**

- Decisions needed

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber

## RR6: Risk Trends

**Purpose:** Show direction.

**Content blocks**

- Trend by category

**Inputs from the user**

- Prior data

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## RR7: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
