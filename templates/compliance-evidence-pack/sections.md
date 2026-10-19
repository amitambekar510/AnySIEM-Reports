# Compliance Evidence Pack: Section Blueprint

Blueprint for an audit-ready evidence pack. Build one pack per framework. Never state compliance without evidence and compliance-owner agreement.

## Section index

| ID | Section | Include |
|---|---|---|
| C0 | Cover and Document Control | Always |
| C1 | Scope and Applicability | Always |
| C2 | Control Mapping Matrix | Always |
| C3 | Evidence Index | Always |
| C4 | Operating Effectiveness Samples | Always |
| C5 | Exceptions, Gaps and Remediation | Always |
| C6 | Regulatory Reporting Record | When any regulatory report was made in the period |
| C7 | Management Statement | Always |
| C8 | Sign-Off and Acknowledgement | Always |

## C0: Cover and Document Control

**Purpose:** Identify the pack and its framework.

**Content blocks**

- Cover with framework name, version, and audit period
- Document control table

**Inputs from the user**

- Framework and version
- Audit period
- Entity type

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## C1: Scope and Applicability

**Purpose:** State what the pack covers and who decided applicability.

**Content blocks**

- Framework and version
- Entity type and applicability decision (made by the compliance team)
- In-scope systems and services
- Out-of-scope items and reasons

**Inputs from the user**

- Applicability decision
- Scope

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023, ISO/IEC 27001, NSE/BSE Tech Audit, NPCI/UPI, SEBI PFUTP 2003, NIST CSF, ISO/IEC 27090, ISO/IEC 42001

## C2: Control Mapping Matrix

**Purpose:** Link each requirement to SOC activity and evidence.

**Content blocks**

- Matrix: control reference, requirement summary (verified), SOC activity, evidence ID, status, owner
- Status values: Evidenced, Partially evidenced, Not in SOC scope, To be confirmed

**Inputs from the user**

- Controls in scope
- Status judgments from the compliance team

**Data from the SIEM (vendor-neutral)**

- Monitoring, retention, and incident evidence extracts

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023, ISO/IEC 27001, MITRE ATT&CK, NIST CSF, NSE/BSE Tech Audit, NPCI/UPI, SEBI PFUTP 2003, ISO/IEC 27090, ISO/IEC 42001

**Writing note:** Verify every control reference against the official text. Mark anything unverified 'To be confirmed'.

## C3: Evidence Index

**Purpose:** Make every claim traceable.

**Content blocks**

- Index table: evidence ID, description, source, date range, custodian, storage location, retention

**Inputs from the user**

- Evidence list and custodians

**Data from the SIEM (vendor-neutral)**

- Report exports
- Log extracts
- Case records
- Configuration exports

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, CERT-In 2022, NSE/BSE Tech Audit

## C4: Operating Effectiveness Samples

**Purpose:** Show controls working in practice.

**Content blocks**

- Sample incidents or alerts with handling records
- Sample log retention proof
- Sample access review

**Inputs from the user**

- Which samples can be shared

**Data from the SIEM (vendor-neutral)**

- Sampled case records
- Retention proof extracts

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, NSE/BSE Tech Audit

## C5: Exceptions, Gaps and Remediation

**Purpose:** Be open about gaps.

**Content blocks**

- Gap register (control, gap, risk, remediation, owner, due date)

**Inputs from the user**

- Known gaps

**Data from the SIEM (vendor-neutral)**

- Coverage gaps

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, NSE/BSE Tech Audit

## C6: Regulatory Reporting Record

**Purpose:** Document reports made to regulators.

**Include when:** When any regulatory report was made in the period

**Content blocks**

- Table: date, regulator, obligation, reference, status

**Inputs from the user**

- Reports made and references

**Data from the SIEM (vendor-neutral)**

- Incident records tied to reports

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023, NPCI/UPI, NSE/BSE Tech Audit

## C7: Management Statement

**Purpose:** Provide a space for the organization's own attestation.

**Content blocks**

- Statement text supplied by the user's compliance owner
- Signature block

**Inputs from the user**

- Statement wording from the compliance owner

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

**Writing note:** Do not write attestation language yourself. Use only what the compliance owner provides.

## C8: Sign-Off and Acknowledgement

**Purpose:** Record review.

**Content blocks**

- Team-level sign-off
- Disclaimer

**Inputs from the user**

- Roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
