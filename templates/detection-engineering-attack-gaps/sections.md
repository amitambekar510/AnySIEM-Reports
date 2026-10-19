# Detection Engineering and ATT&CK Gap Report: Section Blueprint

Blueprint for a detection engineering report with honest ATT&CK coverage and prioritized gaps.

## Section index

| ID | Section | Include |
|---|---|---|
| D0 | Cover and Document Control | Always |
| D1 | Executive Summary | Always |
| D2 | Detection Inventory | Always |
| D3 | ATT&CK Coverage Analysis | Always |
| D4 | Gap Analysis | Always |
| D5 | Rule Performance and Tuning | Always |
| D6 | Detection Validation | When validation testing was performed |
| D7 | Backlog and Roadmap | Always |
| D8 | Change Log | Always |
| D9 | Sign-Off and Acknowledgement | Always |

## D0: Cover and Document Control

**Purpose:** Identify the report.

**Content blocks**

- Cover
- Document control table

**Inputs from the user**

- Document ID format
- Roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## D1: Executive Summary

**Purpose:** Summarize detection capability and priorities.

**Content blocks**

- Capability statement
- Top gaps
- Planned improvements

**Inputs from the user**

- Disclosure level

**Data from the SIEM (vendor-neutral)**

- Active rule count
- Techniques covered

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF, ISO/IEC 27001

## D2: Detection Inventory

**Purpose:** List what detection content exists and who owns it.

**Content blocks**

- Rules by type and status
- Ownership and last review date
- Custom vs vendor-supplied content

**Inputs from the user**

- Review policy

**Data from the SIEM (vendor-neutral)**

- Rule list with type, status, severity
- Last modified date
- Rule owner

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, MITRE ATT&CK

## D3: ATT&CK Coverage Analysis

**Purpose:** Show coverage by tactic and technique, with quality levels.

**Content blocks**

- Coverage heatmap or table
- Coverage level per technique (none, partial, validated)
- Dependency on data sources

**Inputs from the user**

- Coverage level definitions
- Which ATT&CK matrix and version

**Data from the SIEM (vendor-neutral)**

- Rule-to-technique mapping
- Data source availability per technique

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF

**Writing note:** Coverage means a mapped rule exists, not that the technique will always be detected. Say so.

## D4: Gap Analysis

**Purpose:** Prioritize what is missing and why.

**Content blocks**

- Priority techniques (based on the organization's threat profile)
- Gap reason (no data, no rule, rule untested, rule noisy)
- Risk if unaddressed
- Detection gaps for AI-specific threats (when AI systems are in scope)

**Inputs from the user**

- Threat profile or priority adversaries
- Risk appetite

**Data from the SIEM (vendor-neutral)**

- Missing data sources
- Unmapped or untested rules

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF, SEBI CSCRF 2024, ISO/IEC 27090

## D5: Rule Performance and Tuning

**Purpose:** Show detection quality.

**Content blocks**

- Trigger counts per rule
- True and false positive rates
- Noisy rules and silent rules
- Tuning actions taken

**Inputs from the user**

- How dispositions are recorded

**Data from the SIEM (vendor-neutral)**

- Alerts per rule
- Dispositions per rule
- Rules with zero triggers

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, MITRE ATT&CK

## D6: Detection Validation

**Purpose:** Show detections are tested.

**Include when:** When validation testing was performed

**Content blocks**

- Test method (simulation, purple team, replay)
- Results per technique
- Failed tests and fixes

**Inputs from the user**

- Testing performed and results

**Data from the SIEM (vendor-neutral)**

- Test alert records

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF, ISO/IEC 27001

## D7: Backlog and Roadmap

**Purpose:** Prioritize detection work.

**Content blocks**

- Backlog table (technique, action, effort, risk reduction, owner, target date)

**Inputs from the user**

- Capacity and priorities

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## D8: Change Log

**Purpose:** Record rule changes under control.

**Content blocks**

- Rules added, modified, retired
- Approval record

**Inputs from the user**

- Change approval process

**Data from the SIEM (vendor-neutral)**

- Rule change history

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## D9: Sign-Off and Acknowledgement

**Purpose:** Record review.

**Content blocks**

- Team-level sign-off
- Disclaimer

**Inputs from the user**

- Roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
