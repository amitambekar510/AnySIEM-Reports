# Control Attribute Coverage Report: Section Blueprint

Blueprint for a report that organizes controls by attributes. Built around the ideas in ISO/IEC 27028 (Edition 1, 2026), guidance on using information security control attributes. Use the organization's own attribute scheme. Do not reproduce attribute tables or per-control attribute values from ISO/IEC 27002 or 27028.

## Section index

| ID | Section | Include |
|---|---|---|
| CA0 | Cover and Document Control | Always |
| CA1 | Scope and Attribute Scheme | Always |
| CA2 | Control and Activity Inventory | Always |
| CA3 | Distribution by Control Type | Always |
| CA4 | Coverage by Information Security Property | Always |
| CA5 | Other Attribute Views | When the organization uses these attribute views |
| CA6 | Custom Attributes | When the organization defines custom attributes |
| CA7 | Gap Analysis Using Attributes | Always |
| CA8 | SOC Evidence Mapping | Always |
| CA9 | Recommendations and Roadmap | Always |
| CA10 | Sign-Off and Acknowledgement | Always |

## CA0: Cover and Document Control

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

## CA1: Scope and Attribute Scheme

**Purpose:** State which attributes the organization uses and why.

**Content blocks**

- Attributes in use, as documented in the organization's own ISMS
- Custom attributes the organization defines
- Purpose (reporting, control selection, design, or gap finding)

**Inputs from the user**

- Attribute scheme and where it is documented

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27028, ISO/IEC 27001, NIST CSF

**Writing note:** Use the organization's own scheme. Do not copy attribute tables or values from any standard.

## CA2: Control and Activity Inventory

**Purpose:** List what is tagged.

**Content blocks**

- Table: control or SOC activity, owner, attribute values assigned by the organization

**Inputs from the user**

- Control list with attribute values

**Data from the SIEM (vendor-neutral)**

- Detection rules by type
- Response playbooks
- Prevention integrations feeding the platform

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27028, ISO/IEC 27001, NIST CSF

## CA3: Distribution by Control Type

**Purpose:** Show the balance of control types.

**Content blocks**

- Counts or shares of preventive, detective, and corrective controls (or the organization's own types)
- Observations on balance

**Inputs from the user**

- Type scheme in use

**Data from the SIEM (vendor-neutral)**

- Counts of detections, playbooks, and preventive integrations

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27028, ISO/IEC 27001, NIST CSF, SEBI CSCRF 2024

## CA4: Coverage by Information Security Property

**Purpose:** Show which properties are protected, detected, and recovered.

**Content blocks**

- Confidentiality, integrity, and availability coverage by control
- Properties with weak or no detective coverage

**Inputs from the user**

- Property mapping from control owners

**Data from the SIEM (vendor-neutral)**

- Detections mapped to each property

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27028, ISO/IEC 27001, MITRE ATT&CK

## CA5: Other Attribute Views

**Purpose:** Show additional views the organization uses.

**Include when:** When the organization uses these attribute views

**Content blocks**

- Views such as cybersecurity concepts, operational capabilities, and security domains, only if the organization uses them

**Inputs from the user**

- Views in use

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27028, ISO/IEC 27001, NIST CSF

## CA6: Custom Attributes

**Purpose:** Show organization-defined attributes.

**Include when:** When the organization defines custom attributes

**Content blocks**

- Custom attribute names, allowed values, and purpose
- Examples the user may choose: owner, automation level, evidence source, regulatory link, review date

**Inputs from the user**

- Custom attributes

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27028, ISO/IEC 27001

## CA7: Gap Analysis Using Attributes

**Purpose:** Find what is missing.

**Content blocks**

- Check attribute coverage against risk treatment plans
- Missing combinations (for example, a property with no detective control)
- Risks and actions that result

**Inputs from the user**

- Risk treatment plans to check

**Data from the SIEM (vendor-neutral)**

- Coverage data from detections and playbooks

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27028, ISO/IEC 27001, NIST CSF, SEBI CSCRF 2024

**Writing note:** Present gaps as findings to review. Do not claim the check is exhaustive.

## CA8: SOC Evidence Mapping

**Purpose:** Link attributes to monitoring evidence.

**Content blocks**

- Detections, playbooks, and monitoring evidence mapped to attribute values
- Cross-reference to ATT&CK and to selected frameworks

**Inputs from the user**

- Evidence references

**Data from the SIEM (vendor-neutral)**

- Rule and playbook mappings

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27028, MITRE ATT&CK, ISO/IEC 27001, CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber

## CA9: Recommendations and Roadmap

**Purpose:** Plan improvements.

**Content blocks**

- Prioritized actions with owners and dates

**Inputs from the user**

- Priorities

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27028, ISO/IEC 27001

## CA10: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
