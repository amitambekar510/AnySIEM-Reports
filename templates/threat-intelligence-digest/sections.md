# Threat Intelligence Digest: Section Blueprint

Blueprint for an annual threat intelligence digest. Use only the IOC delivery sections that apply.

## Section index

| ID | Section | Include |
|---|---|---|
| T0 | Cover and Document Control | Always |
| T1 | Introduction, Purpose and Digest vs Live Feed | Always |
| T2 | Confidentiality, Data Handling and Controlled Distribution | Always |
| T3 | Threat Landscape Overview | Always |
| T4 | IOC Delivery: Secure Access Link | When the secure access link service applies |
| T5 | IOC Delivery: Feed URL Integration | When the feed URL service applies |
| T6 | IOC Validity, Freshness and Lifecycle | Always |
| T7 | Strategic Security Recommendations | Always |
| T8 | Scope, Purpose and Limitations | Always |
| T9 | Sign-Off and Acknowledgement | Always |

## T0: Cover and Document Control

**Purpose:** Identify the digest, its edition, version, and review date.

**Content blocks**

- Cover with edition year and service type
- Document control table
- Annual review date
- Version control notice
- Revision history

**Inputs from the user**

- Edition year
- Which delivery option applies (secure access link, feed URL, or both)

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## T1: Introduction, Purpose and Digest vs Live Feed

**Purpose:** Explain what this document is, and what it is not.

**Content blocks**

- Purpose of the digest
- Clear statement: the annual digest is an advisory and governance document, and current IOCs are delivered separately through a secure channel and refreshed continuously
- Service options overview

**Inputs from the user**

- How IOCs are delivered to this reader

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, NIST CSF

**Writing note:** This distinction prevents the annual report from being mistaken for a source of current IOC data.

## T2: Confidentiality, Data Handling and Controlled Distribution

**Purpose:** Control who receives the digest.

**Content blocks**

- Confidentiality and handling rules
- Retention requirement
- Controlled copy and distribution list (recipient, organization, role, copy ID, date, method, status, access expiry)

**Inputs from the user**

- Recipients
- Copy ID format
- Distribution method

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, DPDP Act 2023, SEBI CSCRF 2024

## T3: Threat Landscape Overview

**Purpose:** Summarize the threat categories relevant to the reader.

**Content blocks**

- Top threat categories with risk level
- IOC summary by category (counts or generic wording)
- Threats targeting AI systems, such as data poisoning and model theft (when relevant)

**Inputs from the user**

- Sector and exposure
- Disclosure level

**Data from the SIEM (vendor-neutral)**

- IOC counts by category
- Common attack types observed
- Blocked or alerted external sources (aggregated)

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF, CERT-In 2022, ISO/IEC 27001, ISO/IEC 27090

## T4: IOC Delivery: Secure Access Link

**Purpose:** Describe how current IOCs are shared through a controlled, traceable channel.

**Include when:** When the secure access link service applies

**Content blocks**

- Overview of the validated IOC list
- Client-specific secure access link (time-limited, access-controlled, traceable where feasible)
- Client responsibility notice (review within the validity window, cross-check against traffic, follow up on reputation questions, report link problems)
- Required action and acknowledgement
- Review and cleanup request process

**Inputs from the user**

- Link validity period
- Acknowledgement method

**Data from the SIEM (vendor-neutral)**

- Traffic visibility from fully integrated source devices

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, ISO/IEC 27001, NIST CSF

**Writing note:** Make clear that review is the client's responsibility, and that coverage depends on how completely source devices are integrated.

## T5: IOC Delivery: Feed URL Integration

**Purpose:** Describe how feed URLs are shared and what support is provided.

**Include when:** When the feed URL service applies

**Content blocks**

- Overview
- Feed categories and refresh expectations
- Integration scope and boundaries (describe only what your organization actually supports)
- Testing before production blocking
- Reporting integration issues

**Inputs from the user**

- Feed categories
- Supported integration methods
- What support is and is not provided

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, NIST CSF

**Writing note:** Do not list integrations the provider does not support.

## T6: IOC Validity, Freshness and Lifecycle

**Purpose:** Define how IOC data is validated, refreshed, and retired.

**Content blocks**

- Validity definition (confirmed by at least one reputable source type)
- Update cadence aligned to the actual process
- Review and supersession rules (when an IOC is removed)
- Post-removal commitment
- Client responsibilities for refreshing local controls

**Inputs from the user**

- Actual update and review practice
- Removal criteria

**Data from the SIEM (vendor-neutral)**

- IOC repository change history

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, SEBI CSCRF 2024

**Writing note:** Wording must match the real process. Do not promise a cadence you do not follow.

## T7: Strategic Security Recommendations

**Purpose:** Provide practical control recommendations written directly in the report.

**Content blocks**

- Geo-based traffic filtering
- Intrusion detection and prevention (signature updates, tuning, placement, alert review, prevention-mode validation, incident integration)
- URL filtering
- Comprehensive device onboarding and monitoring
- Security awareness (written in-document, no third-party links)
- Bandwidth monitoring and capacity management
- DNS security and sinkholing
- Email security (sender authentication, gateway filtering, user awareness)
- Patch and vulnerability management
- Credential and identity security
- Anonymization network awareness
- Incident reporting and intelligence feedback loop

**Inputs from the user**

- Which recommendations to include
- Client-specific constraints

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, NIST CSF, CERT-In 2022

**Writing note:** Explain why each control matters and who is responsible.

## T8: Scope, Purpose and Limitations

**Purpose:** State governance boundaries.

**Content blocks**

- Purpose
- Intended audience
- Coverage
- Limitations (point-in-time advisory)
- Relationship with the continuously updated IOC feed

**Inputs from the user**

- Audience
- Coverage period

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## T9: Sign-Off and Acknowledgement

**Purpose:** Record organization-level acknowledgement.

**Content blocks**

- Team-level sign-off table
- IOC actions acknowledged
- Optional stamp area
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
