# External Attack Surface Report: Section Blueprint

Blueprint for an external exposure report. Cover only assets the organization owns or is authorized to assess.

## Section index

| ID | Section | Include |
|---|---|---|
| EA0 | Cover and Document Control | Always |
| EA1 | Scope and Method | Always |
| EA2 | Asset Discovery Summary | Always |
| EA3 | Exposed Services | Always |
| EA4 | Certificates and DNS Hygiene | Always |
| EA5 | Shadow and Unmanaged Assets | Always |
| EA6 | Risk Prioritization | Always |
| EA7 | Remediation Plan | Always |
| EA8 | Sign-Off and Acknowledgement | Always |

## EA0: Cover and Document Control

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

## EA1: Scope and Method

**Purpose:** Define authorized scope.

**Content blocks**

- Domains and address ranges owned by the organization
- Discovery approach described generically
- Authorization statement

**Inputs from the user**

- Owned domains and ranges
- Authorization

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, SEBI CSCRF 2024

**Writing note:** Cover only authorized assets. Do not describe intrusive testing.

## EA2: Asset Discovery Summary

**Purpose:** Compare known and found.

**Content blocks**

- Known assets
- Newly found assets
- Unknown or unmanaged assets

**Inputs from the user**

- Asset list

**Data from the SIEM (vendor-neutral)**

- Discovery results if available

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## EA3: Exposed Services

**Purpose:** List what is reachable.

**Content blocks**

- Table: asset, port or service, version if known, exposure reason, risk

**Inputs from the user**

- Intended exposures

**Data from the SIEM (vendor-neutral)**

- Perimeter traffic and scan-attempt data

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, NIST CSF

## EA4: Certificates and DNS Hygiene

**Purpose:** Check trust basics.

**Content blocks**

- Certificate expiry and strength
- DNS records and dangling entries
- Email domain protections

**Inputs from the user**

- Domains

**Data from the SIEM (vendor-neutral)**

- DNS and certificate telemetry if available

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## EA5: Shadow and Unmanaged Assets

**Purpose:** Handle the unknown.

**Content blocks**

- Assets without an owner
- Recommended action

**Inputs from the user**

- Ownership data

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## EA6: Risk Prioritization

**Purpose:** Rank.

**Content blocks**

- Priority list with reasoning

**Inputs from the user**

- Risk scale

**Data from the SIEM (vendor-neutral)**

- Attack attempts against exposed services

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, SEBI CSCRF 2024

## EA7: Remediation Plan

**Purpose:** Plan.

**Content blocks**

- Action table (action, owner, date)

**Inputs from the user**

- Plan

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## EA8: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
