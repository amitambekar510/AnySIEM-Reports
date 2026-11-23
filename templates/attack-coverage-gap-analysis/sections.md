# ATT&CK Coverage Gap Analysis: Section Blueprint

Blueprint for a focused ATT&CK coverage analysis. For a broader detection program report, use `detection-engineering-attack-gaps`.

## Section index

| ID | Section | Include |
|---|---|---|
| AG0 | Cover and Document Control | Always |
| AG1 | Scope and Method | Always |
| AG2 | Coverage Summary by Tactic | Always |
| AG3 | Technique-Level Matrix | Always |
| AG4 | Threat-Informed Prioritization | Always |
| AG5 | Gap Register | Always |
| AG6 | Roadmap | Always |
| AG7 | Sign-Off and Acknowledgement | Always |

## AG0: Cover and Document Control

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

## AG1: Scope and Method

**Purpose:** Define the analysis.

**Content blocks**

- ATT&CK matrix and version
- Platforms in scope
- Coverage level definitions (none, partial, validated)

**Inputs from the user**

- Matrix, version, and platforms

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF

## AG2: Coverage Summary by Tactic

**Purpose:** Give the big picture.

**Content blocks**

- Table or heatmap by tactic
- Counts by coverage level

**Inputs from the user**

- Disclosure level

**Data from the SIEM (vendor-neutral)**

- Rule-to-technique mapping counts

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF

**Writing note:** Coverage means a mapped rule exists. It does not guarantee detection.

## AG3: Technique-Level Matrix

**Purpose:** Provide the detail.

**Content blocks**

- Table: technique, rules mapped, data sources needed, data available, coverage level

**Inputs from the user**

- Techniques in scope

**Data from the SIEM (vendor-neutral)**

- Rule mappings
- Data source availability

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK

## AG4: Threat-Informed Prioritization

**Purpose:** Focus on what matters.

**Content blocks**

- Relevant adversaries or attack types
- Priority techniques and why

**Inputs from the user**

- Threat profile

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF, SEBI CSCRF 2024

## AG5: Gap Register

**Purpose:** List the gaps.

**Content blocks**

- Gap, cause (no data, no rule, untested, noisy), risk, remediation, effort

**Inputs from the user**

- Known gaps

**Data from the SIEM (vendor-neutral)**

- Missing data sources
- Unmapped rules

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, ISO/IEC 27001

## AG6: Roadmap

**Purpose:** Plan closure.

**Content blocks**

- Prioritized work with owners and target dates

**Inputs from the user**

- Capacity

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## AG7: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
