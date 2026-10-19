# Threat Hunt Report: Section Blueprint

Blueprint for a single threat hunt report. 'No findings' is a valid result when coverage limits are stated.

## Section index

| ID | Section | Include |
|---|---|---|
| Th0 | Cover and Document Control | Always |
| Th1 | Executive Summary | Always |
| Th2 | Hunt Charter | Always |
| Th3 | Methodology | Always |
| Th4 | Data Sources and Visibility Assessment | Always |
| Th5 | Findings | Always |
| Th6 | ATT&CK Mapping | Always |
| Th7 | Detection Outcomes | Always |
| Th8 | Response Actions and Escalations | When any finding required escalation |
| Th9 | Recommendations and Next Hunts | Always |
| Th10 | Sign-Off and Acknowledgement | Always |

## Th0: Cover and Document Control

**Purpose:** Identify the hunt report.

**Content blocks**

- Cover
- Document control table

**Inputs from the user**

- Hunt ID format
- Roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## Th1: Executive Summary

**Purpose:** State what was hunted, what was found, and what it means.

**Content blocks**

- Hunt objective
- Result in one paragraph
- Key actions

**Inputs from the user**

- Disclosure level

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** NIST CSF, SEBI CSCRF 2024, ISO/IEC 27001

## Th2: Hunt Charter

**Purpose:** Record why and how the hunt was authorized.

**Content blocks**

- Hypothesis
- Trigger (intelligence, anomaly, incident lesson, or routine)
- Scope, time window, and assets
- Success criteria
- Authorization record
- AI-specific hunt hypotheses, such as unusual model query patterns or suspicious changes to training data (when AI systems are in scope)

**Inputs from the user**

- Hypothesis
- Trigger
- Scope limits
- Who authorized it

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, MITRE ATT&CK, ISO/IEC 27090

## Th3: Methodology

**Purpose:** Explain the approach so it can be repeated.

**Content blocks**

- Hunt type (hypothesis-driven, intelligence-driven, anomaly-driven)
- Data analyzed and query approach, described generically
- Validation steps for suspicious results

**Inputs from the user**

- Approach used
- Constraints

**Data from the SIEM (vendor-neutral)**

- Data sources queried
- Search and analytics features used

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF

## Th4: Data Sources and Visibility Assessment

**Purpose:** State what could and could not be seen.

**Content blocks**

- Data sources used
- Visibility gaps that limited the hunt
- Time range actually covered

**Inputs from the user**

- Known blind spots

**Data from the SIEM (vendor-neutral)**

- Source availability during the hunt window
- Retention limits

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001, MITRE ATT&CK

**Writing note:** Every hunt result is only as strong as its visibility. Say so.

## Th5: Findings

**Purpose:** Report results honestly.

**Content blocks**

- Confirmed malicious activity
- Suspicious activity needing follow-up
- Benign or policy findings
- No findings, with the coverage limits stated

**Inputs from the user**

- Findings and evidence

**Data from the SIEM (vendor-neutral)**

- Matching events (aggregated)
- Affected assets

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, MITRE ATT&CK, NIST CSF

**Writing note:** Never write 'the environment is clean'. Write what was examined and what was found within those limits.

## Th6: ATT&CK Mapping

**Purpose:** Map the hunt to adversary behavior.

**Content blocks**

- Techniques hunted
- Techniques observed
- Related detection coverage

**Inputs from the user**

- Techniques in scope

**Data from the SIEM (vendor-neutral)**

- ATT&CK mapping of related rules

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF

## Th7: Detection Outcomes

**Purpose:** Show how the hunt improved detection.

**Content blocks**

- New or tuned detections
- New indicators added
- Playbook updates

**Inputs from the user**

- Changes made

**Data from the SIEM (vendor-neutral)**

- Rule change record

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, MITRE ATT&CK

## Th8: Response Actions and Escalations

**Purpose:** Record what was done about findings.

**Include when:** When any finding required escalation

**Content blocks**

- Escalations (to whom, when)
- Containment steps
- Regulatory notification decision, if relevant

**Inputs from the user**

- Actions taken

**Data from the SIEM (vendor-neutral)**

- Case references

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber, DPDP Act 2023

## Th9: Recommendations and Next Hunts

**Purpose:** Plan follow-up.

**Content blocks**

- Recommendations
- Proposed next hunts with rationale

**Inputs from the user**

- Ideas and priorities

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## Th10: Sign-Off and Acknowledgement

**Purpose:** Record review.

**Content blocks**

- Team-level sign-off
- Disclaimer

**Inputs from the user**

- Roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
