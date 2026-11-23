# Phishing Campaign Analysis: Section Blueprint

Blueprint for analyzing one phishing campaign. Redact real recipient addresses.

## Section index

| ID | Section | Include |
|---|---|---|
| PC0 | Cover and Document Control | Always |
| PC1 | Campaign Summary | Always |
| PC2 | Email Characteristics | Always |
| PC3 | Technical Indicators | Always |
| PC4 | Impact Assessment | Always |
| PC5 | Containment and Response | Always |
| PC6 | ATT&CK Mapping | Always |
| PC7 | Control and Detection Gaps | Always |
| PC8 | Recommendations and User Communication | Always |
| PC9 | Sign-Off and Acknowledgement | Always |

## PC0: Cover and Document Control

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

## PC1: Campaign Summary

**Purpose:** Summarize the campaign.

**Content blocks**

- Dates, volume, targeting, outcome

**Inputs from the user**

- Overview

**Data from the SIEM (vendor-neutral)**

- Message counts and recipients

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, MITRE ATT&CK, ISO/IEC 27001

## PC2: Email Characteristics

**Purpose:** Describe the lure.

**Content blocks**

- Subject themes
- Sender patterns
- Lure and call to action
- Delivery method

**Inputs from the user**

- Examples the user can share (redacted)

**Data from the SIEM (vendor-neutral)**

- Message metadata (aggregated)

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK

**Writing note:** Describe patterns. Redact real addresses.

## PC3: Technical Indicators

**Purpose:** List indicators.

**Content blocks**

- Domains and URLs
- Sender infrastructure
- Attachment or file hashes

**Inputs from the user**

- Indicators to share

**Data from the SIEM (vendor-neutral)**

- Indicator matches

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, ISO/IEC 27001

## PC4: Impact Assessment

**Purpose:** Measure exposure.

**Content blocks**

- Recipients
- Clicks
- Credentials entered
- Endpoints affected

**Inputs from the user**

- Confirmed impact

**Data from the SIEM (vendor-neutral)**

- Click and access logs
- Endpoint alerts

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, DPDP Act 2023, SEBI CSCRF 2024

## PC5: Containment and Response

**Purpose:** Record actions.

**Content blocks**

- Message removal
- Blocks applied
- Password resets and session revocation

**Inputs from the user**

- Actions taken

**Data from the SIEM (vendor-neutral)**

- Case actions

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, NIST CSF, SEBI CSCRF 2024

## PC6: ATT&CK Mapping

**Purpose:** Map behavior.

**Content blocks**

- Initial access and follow-on techniques observed

**Inputs from the user**

- Techniques observed

**Data from the SIEM (vendor-neutral)**

- Rule mappings

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF

## PC7: Control and Detection Gaps

**Purpose:** Find what let it through.

**Content blocks**

- Email filtering gaps
- Detection gaps
- User reporting gaps

**Inputs from the user**

- Known gaps

**Data from the SIEM (vendor-neutral)**

- Detection coverage for email-related use cases

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## PC8: Recommendations and User Communication

**Purpose:** Prevent recurrence.

**Content blocks**

- Recommendations
- Draft user advisory

**Inputs from the user**

- Priorities

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## PC9: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
