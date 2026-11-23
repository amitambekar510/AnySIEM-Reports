# Tuning and Whitelisting Request Log: Section Blueprint

Blueprint for a tuning and whitelisting register. The deliverable is a PDF table. The AI also offers the field definitions so the user can rebuild the log in their own tool.

## Section index

| ID | Section | Include |
|---|---|---|
| TW0 | Cover and Document Control | Always |
| TW1 | Log Header and Policy | Always |
| TW2 | Request Fields | Always |
| TW3 | Request Register | Always |
| TW4 | Risk Assessment Guidance | Always |
| TW5 | Review of Active Exceptions | Always |
| TW6 | Summary | Always |
| TW7 | Sign-Off and Acknowledgement | Always |

## TW0: Cover and Document Control

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

## TW1: Log Header and Policy

**Purpose:** Define governance.

**Content blocks**

- Approval rules
- Who may request and approve
- Expiry policy

**Inputs from the user**

- Policy

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber

## TW2: Request Fields

**Purpose:** Standardize entries.

**Content blocks**

- Field table: ID, date, requester role, rule, reason, scope, risk assessment, approver, expiry, status

**Inputs from the user**

- Extra fields

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## TW3: Request Register

**Purpose:** Hold the entries.

**Content blocks**

- Table of requests for the period

**Inputs from the user**

- Requests

**Data from the SIEM (vendor-neutral)**

- Rule and alert context

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## TW4: Risk Assessment Guidance

**Purpose:** Prevent unsafe exceptions.

**Content blocks**

- What must be assessed before approval
- Why broad or permanent exclusions are discouraged

**Inputs from the user**

- Risk criteria

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, MITRE ATT&CK

## TW5: Review of Active Exceptions

**Purpose:** Prevent exception creep.

**Content blocks**

- Exceptions due for re-approval
- Retired exceptions

**Inputs from the user**

- Review cycle

**Data from the SIEM (vendor-neutral)**

- Active exception list

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## TW6: Summary

**Purpose:** Summarize.

**Content blocks**

- Counts by status and rule
- Impact on alert volume

**Inputs from the user**

- None

**Data from the SIEM (vendor-neutral)**

- Counts

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## TW7: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
