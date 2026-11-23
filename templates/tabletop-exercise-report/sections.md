# Tabletop Exercise Report: Section Blueprint

Blueprint for a tabletop or drill report. Use roles rather than personal names.

## Section index

| ID | Section | Include |
|---|---|---|
| X0 | Cover and Document Control | Always |
| X1 | Exercise Summary | Always |
| X2 | Objectives and Scope | Always |
| X3 | Participants and Roles | Always |
| X4 | Scenario Overview | Always |
| X5 | Exercise Timeline and Decisions | Always |
| X6 | Findings: Strengths and Gaps | Always |
| X7 | Regulatory Notification Readiness | When notification was part of the exercise |
| X8 | Corrective Action Plan | Always |
| X9 | Next Exercise Plan | Always |
| X10 | Sign-Off and Acknowledgement | Always |

## X0: Cover and Document Control

**Purpose:** Identify the exercise report.

**Content blocks**

- Cover
- Document control table

**Inputs from the user**

- Exercise ID
- Roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## X1: Exercise Summary

**Purpose:** Summarize purpose, outcome, and key actions.

**Content blocks**

- Date, format, duration
- Overall outcome
- Top strengths and gaps

**Inputs from the user**

- Disclosure level

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, NIST CSF

## X2: Objectives and Scope

**Purpose:** State what the exercise tested.

**Content blocks**

- Objectives
- Processes and teams in scope
- Assumptions and limits

**Inputs from the user**

- Objectives
- Scope

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, NIST CSF

## X3: Participants and Roles

**Purpose:** Record who took part, by role.

**Content blocks**

- Table: function, role in exercise (player, facilitator, observer)

**Inputs from the user**

- Participating functions

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## X4: Scenario Overview

**Purpose:** Describe the scenario without operational secrets.

**Content blocks**

- Scenario narrative
- Inject list (time, event, intended test)
- Optional scenario theme: compromise of an AI system or its training data

**Inputs from the user**

- Scenario and injects

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF, CERT-In 2022, ISO/IEC 27090

## X5: Exercise Timeline and Decisions

**Purpose:** Compare expected and actual responses.

**Content blocks**

- Table: inject, expected action, actual response, observation, time taken

**Inputs from the user**

- What happened at each inject

**Data from the SIEM (vendor-neutral)**

- Optional: tooling views used during the exercise

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, SEBI CSCRF 2024

## X6: Findings: Strengths and Gaps

**Purpose:** Evaluate performance by area.

**Content blocks**

- Areas: detection, escalation, communication, decision making, tooling, documentation
- Strengths
- Gaps with severity

**Inputs from the user**

- Observations

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, NIST CSF

## X7: Regulatory Notification Readiness

**Purpose:** Test whether reporting duties can be met in time.

**Include when:** When notification was part of the exercise

**Content blocks**

- Which obligations were exercised
- Time to decide and time to draft
- Gaps in contacts, templates, or approvals

**Inputs from the user**

- Obligations exercised and times

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023, NPCI/UPI, NSE/BSE Tech Audit

**Writing note:** Never state a deadline you have not verified.

## X8: Corrective Action Plan

**Purpose:** Turn gaps into action.

**Content blocks**

- Action table (gap, action, owner, due date, priority)

**Inputs from the user**

- Owners and dates

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, NIST CSF

## X9: Next Exercise Plan

**Purpose:** Plan the next test.

**Content blocks**

- Proposed scenario themes
- Target date
- Participants to add

**Inputs from the user**

- Plans

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## X10: Sign-Off and Acknowledgement

**Purpose:** Record review.

**Content blocks**

- Team-level sign-off
- Disclaimer

**Inputs from the user**

- Roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
