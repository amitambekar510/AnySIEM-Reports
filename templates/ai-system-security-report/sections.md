# AI System Security Monitoring Report: Section Blueprint

Blueprint for reporting on the security of AI systems the organization develops or uses. Built around the themes of ISO/IEC 27090 (guidance published October 2026). Use only the user's own inputs. Do not reproduce text from the standard.

## Section index

| ID | Section | Include |
|---|---|---|
| AI0 | Cover and Document Control | Always |
| AI1 | Scope and AI System Inventory | Always |
| AI2 | Assets Requiring Protection | Always |
| AI3 | AI-Specific Threat Overview | Always |
| AI4 | Lifecycle Coverage | Always |
| AI5 | Monitoring and Detection Coverage | Always |
| AI6 | Observed Events and Incidents | Always |
| AI7 | Controls and Alignment | Always |
| AI8 | Retraining and Model Update Governance | Always |
| AI9 | Gaps and Risk | Always |
| AI10 | Recommendations and Roadmap | Always |
| AI11 | Sign-Off and Acknowledgement | Always |

## AI0: Cover and Document Control

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

## AI1: Scope and AI System Inventory

**Purpose:** Show which AI systems are covered.

**Content blocks**

- AI systems in scope (purpose, owner, deployment, lifecycle stage)
- In-house vs third-party components
- Criticality

**Inputs from the user**

- AI system list
- Owners

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, ISO/IEC 27001, NIST CSF, ISO/IEC 42001

**Writing note:** Use only what the user provides. Do not describe systems you have not been told about.

## AI2: Assets Requiring Protection

**Purpose:** Name what needs protecting.

**Content blocks**

- Training and fine-tuning data
- Models and model artifacts
- Operational input data
- Related intellectual property

**Inputs from the user**

- Where each asset lives and who can access it

**Data from the SIEM (vendor-neutral)**

- Access logs for data stores and model repositories

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, ISO/IEC 27001, DPDP Act 2023

## AI3: AI-Specific Threat Overview

**Purpose:** Explain how AI systems can be attacked and what follows.

**Content blocks**

- Threats such as data poisoning and model theft
- How each could be exploited
- Potential consequences for the organization and for individuals
- Threats the user has identified

**Inputs from the user**

- Threats the user considers relevant

**Data from the SIEM (vendor-neutral)**

- Alerts related to AI platforms

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, MITRE ATT&CK, NIST CSF, CERT-In 2022

## AI4: Lifecycle Coverage

**Purpose:** Show security attention across the life cycle.

**Content blocks**

- Development and training
- Operation
- Model updates and retraining

**Inputs from the user**

- Lifecycle stages in use

**Data from the SIEM (vendor-neutral)**

- Pipeline and change events

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, ISO/IEC 27001

## AI5: Monitoring and Detection Coverage

**Purpose:** Show what the SOC can see.

**Content blocks**

- Log sources from AI platforms, data stores, and model access
- Detection of unusual query patterns that could indicate model theft
- Detection of suspicious changes to training or retraining data
- Gaps

**Inputs from the user**

- Which AI platform logs are available

**Data from the SIEM (vendor-neutral)**

- AI platform logs
- Model access logs
- Query volume and pattern data
- Data change events

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, MITRE ATT&CK, NIST CSF, ISO/IEC 27001

## AI6: Observed Events and Incidents

**Purpose:** Report what happened.

**Content blocks**

- Table: date, system, event, assessment, status
- Linked incident references

**Inputs from the user**

- Events and incidents involving AI systems

**Data from the SIEM (vendor-neutral)**

- Related alerts and cases

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, CERT-In 2022, SEBI CSCRF 2024, NIST CSF

**Writing note:** If nothing was observed, state what was monitored and its limits.

## AI7: Controls and Alignment

**Purpose:** Show how conventional and AI-specific controls fit together.

**Content blocks**

- Existing information security controls that apply to AI systems
- AI-specific measures in place
- Gaps between the two

**Inputs from the user**

- Control status from the control owner

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, ISO/IEC 27001, ISO/IEC 42001

## AI8: Retraining and Model Update Governance

**Purpose:** Protect the update path.

**Content blocks**

- Controls over data collected during operation that may feed retraining
- Validation before a new model version is released
- Change approval

**Inputs from the user**

- Retraining process

**Data from the SIEM (vendor-neutral)**

- Pipeline change records

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, ISO/IEC 27001

## AI9: Gaps and Risk

**Purpose:** Record what is missing and why it matters.

**Content blocks**

- Gap and risk table (gap, risk, owner, due date)
- Entries for the risk register

**Inputs from the user**

- Known gaps

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, ISO/IEC 27001, NIST CSF, SEBI CSCRF 2024, ISO/IEC 42001

## AI10: Recommendations and Roadmap

**Purpose:** Plan improvements.

**Content blocks**

- Prioritized actions with owners and dates

**Inputs from the user**

- Priorities

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27090, ISO/IEC 27001, ISO/IEC 42001

## AI11: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
