# Log Retention, Storage and Integrity Report: Section Blueprint

Blueprint for a deep dive on log retention, storage, and integrity.

## Section index

| ID | Section | Include |
|---|---|---|
| RS0 | Cover and Document Control | Always |
| RS1 | Retention Requirements | Always |
| RS2 | Retention Configuration | Always |
| RS3 | Storage Capacity and Forecast | Always |
| RS4 | Integrity and Tamper Protection | Always |
| RS5 | Data Location Statement | When residency requirements apply |
| RS6 | Recovery and Restore Tests | Always |
| RS7 | Exceptions and Remediation | Always |
| RS8 | Sign-Off and Acknowledgement | Always |

## RS0: Cover and Document Control

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

## RS1: Retention Requirements

**Purpose:** State what is required and by whom.

**Content blocks**

- Requirements by framework and internal policy
- Applicable data categories

**Inputs from the user**

- Requirements
- Selected frameworks

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023, ISO/IEC 27001, NSE/BSE Tech Audit, NPCI/UPI

**Writing note:** Verify retention periods against current official text.

## RS2: Retention Configuration

**Purpose:** Show what is actually configured.

**Content blocks**

- Table: source category, required period, configured period, status

**Inputs from the user**

- Policy values

**Data from the SIEM (vendor-neutral)**

- Retention settings per data category

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001, RBI IT/Cyber

## RS3: Storage Capacity and Forecast

**Purpose:** Plan capacity.

**Content blocks**

- Current use
- Growth trend
- Forecast and action date

**Inputs from the user**

- Budget constraints

**Data from the SIEM (vendor-neutral)**

- Storage use and growth

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## RS4: Integrity and Tamper Protection

**Purpose:** Show logs are trustworthy.

**Content blocks**

- Integrity controls
- Access restrictions
- Audit of changes to stored data

**Inputs from the user**

- Controls

**Data from the SIEM (vendor-neutral)**

- Integrity features in use
- Access logs for stored data

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, CERT-In 2022, RBI IT/Cyber

## RS5: Data Location Statement

**Purpose:** Record where data resides.

**Include when:** When residency requirements apply

**Content blocks**

- Storage locations
- Residency commitments

**Inputs from the user**

- Locations

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, DPDP Act 2023, RBI IT/Cyber

## RS6: Recovery and Restore Tests

**Purpose:** Prove data can be recovered.

**Content blocks**

- Test date, method, and result

**Inputs from the user**

- Test results

**Data from the SIEM (vendor-neutral)**

- Restore test records

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber

## RS7: Exceptions and Remediation

**Purpose:** Be open about gaps.

**Content blocks**

- Exception table (item, reason, risk, fix, date)

**Inputs from the user**

- Exceptions

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, CERT-In 2022

## RS8: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
