# Monitoring Platform Access Review: Section Blueprint

Blueprint for an access review of the monitoring platform. Use roles, not personal names.

## Section index

| ID | Section | Include |
|---|---|---|
| AR0 | Cover and Document Control | Always |
| AR1 | Scope and Review Period | Always |
| AR2 | User and Role Inventory | Always |
| AR3 | Review Results | Always |
| AR4 | Authentication Controls | Always |
| AR5 | Privileged Activity Review | Always |
| AR6 | Dormant and Orphaned Accounts | Always |
| AR7 | Exceptions and Remediation | Always |
| AR8 | Reviewer Attestation | Always |
| AR9 | Sign-Off and Acknowledgement | Always |

## AR0: Cover and Document Control

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

## AR1: Scope and Review Period

**Purpose:** Define the review.

**Content blocks**

- Platforms in scope
- Period
- Reviewer role

**Inputs from the user**

- Scope

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, SEBI CSCRF 2024

## AR2: User and Role Inventory

**Purpose:** Show who has access.

**Content blocks**

- Users by role
- Privileged accounts
- Service accounts

**Inputs from the user**

- Approved role list

**Data from the SIEM (vendor-neutral)**

- User and role inventory

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber

## AR3: Review Results

**Purpose:** Record decisions.

**Content blocks**

- Access confirmed
- Access removed
- Access changed
- Reason for each class of change

**Inputs from the user**

- Review decisions

**Data from the SIEM (vendor-neutral)**

- Account status

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, SEBI CSCRF 2024

## AR4: Authentication Controls

**Purpose:** Show strength.

**Content blocks**

- MFA coverage
- Session and lockout settings
- Password policy

**Inputs from the user**

- Policy

**Data from the SIEM (vendor-neutral)**

- Authentication settings

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, NIST CSF

## AR5: Privileged Activity Review

**Purpose:** Check admin use.

**Content blocks**

- Sampled administrative actions
- Unusual activity

**Inputs from the user**

- Sample size

**Data from the SIEM (vendor-neutral)**

- Administrative audit log

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, SEBI CSCRF 2024

## AR6: Dormant and Orphaned Accounts

**Purpose:** Remove stale access.

**Content blocks**

- Accounts inactive beyond threshold
- Accounts without an owner
- Actions taken

**Inputs from the user**

- Inactivity threshold

**Data from the SIEM (vendor-neutral)**

- Last sign-in data

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber

## AR7: Exceptions and Remediation

**Purpose:** Track fixes.

**Content blocks**

- Exception table (item, risk, fix, owner, date)

**Inputs from the user**

- Exceptions

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## AR8: Reviewer Attestation

**Purpose:** Record the reviewer's statement.

**Content blocks**

- Statement supplied by the reviewer
- Signature block

**Inputs from the user**

- Reviewer statement

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

**Writing note:** Use only the statement the reviewer provides.

## AR9: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
