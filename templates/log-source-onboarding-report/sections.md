# Log Source Onboarding Report: Section Blueprint

Blueprint for onboarding one log source or one batch of similar sources.

## Section index

| ID | Section | Include |
|---|---|---|
| LO0 | Cover and Document Control | Always |
| LO1 | Onboarding Request and Scope | Always |
| LO2 | Technical Design | Always |
| LO3 | Validation Results | Always |
| LO4 | Detection Use Cases Enabled | Always |
| LO5 | Capacity and Retention Impact | Always |
| LO6 | Issues and Remediation | Always |
| LO7 | Acceptance and Handover | Always |
| LO8 | Sign-Off and Acknowledgement | Always |

## LO0: Cover and Document Control

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

## LO1: Onboarding Request and Scope

**Purpose:** Define the source and why it matters.

**Content blocks**

- Source name and type
- Owner and business purpose
- Criticality

**Inputs from the user**

- Request details

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, CERT-In 2022

## LO2: Technical Design

**Purpose:** Describe how data arrives.

**Content blocks**

- Collection method and protocol
- Network path and security
- Parser or integration
- Time synchronization
- Volume estimate

**Inputs from the user**

- Design details

**Data from the SIEM (vendor-neutral)**

- Supported collection methods

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001

## LO3: Validation Results

**Purpose:** Prove the data is good.

**Content blocks**

- Data received and completeness
- Field mapping and normalization check
- Timestamp accuracy

**Inputs from the user**

- Test results

**Data from the SIEM (vendor-neutral)**

- Ingestion statistics
- Parse success

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001, RBI IT/Cyber

## LO4: Detection Use Cases Enabled

**Purpose:** Show value.

**Content blocks**

- Use cases enabled
- ATT&CK techniques supported

**Inputs from the user**

- Use cases

**Data from the SIEM (vendor-neutral)**

- Rules using the new source

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF

## LO5: Capacity and Retention Impact

**Purpose:** Plan for growth.

**Content blocks**

- Added volume
- Retention applied
- Storage impact

**Inputs from the user**

- Retention requirement

**Data from the SIEM (vendor-neutral)**

- Volume and storage figures

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001

## LO6: Issues and Remediation

**Purpose:** Track problems.

**Content blocks**

- Issue table (issue, impact, fix, owner, date)

**Inputs from the user**

- Open issues

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## LO7: Acceptance and Handover

**Purpose:** Close the onboarding.

**Content blocks**

- Acceptance criteria with status
- Handover to operations

**Inputs from the user**

- Acceptance criteria

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## LO8: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
