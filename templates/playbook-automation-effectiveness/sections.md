# Playbook and Automation Effectiveness Report: Section Blueprint

Blueprint for measuring whether playbooks and automation help.

## Section index

| ID | Section | Include |
|---|---|---|
| PA0 | Cover and Document Control | Always |
| PA1 | Playbook Inventory | Always |
| PA2 | Execution Statistics | Always |
| PA3 | Time and Effort Impact | Always |
| PA4 | Failure and Exception Analysis | Always |
| PA5 | Quality and Safety Controls | Always |
| PA6 | Coverage Gaps | Always |
| PA7 | Improvement Roadmap | Always |
| PA8 | Sign-Off and Acknowledgement | Always |

## PA0: Cover and Document Control

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

## PA1: Playbook Inventory

**Purpose:** List what exists.

**Content blocks**

- Table: playbook, use case, trigger, automation level, owner, last review

**Inputs from the user**

- Inventory

**Data from the SIEM (vendor-neutral)**

- Playbook list

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## PA2: Execution Statistics

**Purpose:** Show usage and reliability.

**Content blocks**

- Runs, successes, failures, manual overrides

**Inputs from the user**

- How failures are counted

**Data from the SIEM (vendor-neutral)**

- Execution records

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## PA3: Time and Effort Impact

**Purpose:** Estimate value honestly.

**Content blocks**

- Method for estimating time saved
- Results

**Inputs from the user**

- Estimation method

**Data from the SIEM (vendor-neutral)**

- Execution durations

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

**Writing note:** State the estimation method. Do not present estimates as measurements.

## PA4: Failure and Exception Analysis

**Purpose:** Learn from failures.

**Content blocks**

- Top failure causes
- Corrective actions

**Inputs from the user**

- Known causes

**Data from the SIEM (vendor-neutral)**

- Failure logs

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## PA5: Quality and Safety Controls

**Purpose:** Show automation is controlled.

**Content blocks**

- Approval gates
- Testing before release
- Rollback approach
- Change control

**Inputs from the user**

- Controls in place

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber, SEBI CSCRF 2024

## PA6: Coverage Gaps

**Purpose:** Find what is not automated.

**Content blocks**

- Use cases without playbooks
- Priority candidates

**Inputs from the user**

- Candidate list

**Data from the SIEM (vendor-neutral)**

- High-volume alert types

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## PA7: Improvement Roadmap

**Purpose:** Plan.

**Content blocks**

- Prioritized improvements

**Inputs from the user**

- Capacity

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## PA8: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
