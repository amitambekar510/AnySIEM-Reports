# Credential Leak and Dark Web Monitoring Report: Section Blueprint

Blueprint for an exposure monitoring report. Never reproduce passwords or secrets, and mask identifiers.

## Section index

| ID | Section | Include |
|---|---|---|
| CL0 | Cover and Document Control | Always |
| CL1 | Monitoring Scope | Always |
| CL2 | Findings Summary | Always |
| CL3 | Exposed Credential Handling | Always |
| CL4 | Mentions and Claims | When claims or mentions were found |
| CL5 | Risk Assessment | Always |
| CL6 | Actions Taken and Recommended | Always |
| CL7 | Legal and Privacy Notes | Always |
| CL8 | Sign-Off and Acknowledgement | Always |

## CL0: Cover and Document Control

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

## CL1: Monitoring Scope

**Purpose:** State what was monitored.

**Content blocks**

- Domains and identifiers in scope
- Lawful source types monitored, described generically
- Period

**Inputs from the user**

- Scope

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** DPDP Act 2023, ISO/IEC 27001, CERT-In 2022

**Writing note:** Describe lawful sources in generic terms only.

## CL2: Findings Summary

**Purpose:** Summarize exposure.

**Content blocks**

- Exposures by type, new vs previously reported
- Confidence in each finding

**Inputs from the user**

- Findings

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** DPDP Act 2023, CERT-In 2022, ISO/IEC 27001

## CL3: Exposed Credential Handling

**Purpose:** Record validation and response.

**Content blocks**

- Validation approach
- Reset and revocation status
- Accounts with MFA enabled

**Inputs from the user**

- Handling status

**Data from the SIEM (vendor-neutral)**

- Authentication events for affected accounts

**Compliance hooks (indicative, verify before citing):** DPDP Act 2023, ISO/IEC 27001, RBI IT/Cyber

**Writing note:** Never reproduce a password or secret. Mask identifiers (for example, j***@domain).

## CL4: Mentions and Claims

**Purpose:** Report brand or data-sale claims.

**Include when:** When claims or mentions were found

**Content blocks**

- Claim summary
- Verification status
- Credibility assessment

**Inputs from the user**

- Claims found

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** DPDP Act 2023, CERT-In 2022

## CL5: Risk Assessment

**Purpose:** Rate the risk.

**Content blocks**

- Likelihood and impact
- Accounts at highest risk (privileged, remote access)

**Inputs from the user**

- Risk scale

**Data from the SIEM (vendor-neutral)**

- Sign-in activity for exposed accounts

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, SEBI CSCRF 2024

## CL6: Actions Taken and Recommended

**Purpose:** Close the loop.

**Content blocks**

- Forced resets
- Session revocation
- MFA enforcement
- User notification

**Inputs from the user**

- Actions

**Data from the SIEM (vendor-neutral)**

- Case actions

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, DPDP Act 2023, SEBI CSCRF 2024

## CL7: Legal and Privacy Notes

**Purpose:** Record obligations.

**Content blocks**

- Whether a personal data breach assessment is needed
- Decision owner and decision

**Inputs from the user**

- Legal input

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** DPDP Act 2023, CERT-In 2022, RBI IT/Cyber

## CL8: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
