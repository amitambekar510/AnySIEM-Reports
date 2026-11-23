# SOC Efficiency Report: Section Blueprint

Blueprint for a SOC efficiency report. Every metric must be defined before it is reported.

## Section index

| ID | Section | Include |
|---|---|---|
| F0 | Cover and Document Control | Always |
| F1 | Efficiency Summary | Always |
| F2 | Detection and Response Metrics | Always |
| F3 | Alert Quality | Always |
| F4 | Workload and Capacity | Always |
| F5 | Automation and Playbook Impact | Always |
| F6 | Quality Assurance | Always |
| F7 | Findings and Improvement Plan | Always |
| F8 | Sign-Off and Acknowledgement | Always |

## F0: Cover and Document Control

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

## F1: Efficiency Summary

**Purpose:** Summarize how well the SOC converted alerts into outcomes.

**Content blocks**

- Headline results
- Biggest improvement and biggest concern

**Inputs from the user**

- Disclosure level
- Targets

**Data from the SIEM (vendor-neutral)**

- Alert and incident totals
- Timing measures

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber

## F2: Detection and Response Metrics

**Purpose:** Report timing with clear definitions.

**Content blocks**

- Metric definition table (start event, end event, what is excluded)
- Time to acknowledge, detect, respond, and close
- Median and 90th percentile, not only averages
- Trend against prior periods

**Inputs from the user**

- How each metric is measured
- Targets

**Data from the SIEM (vendor-neutral)**

- Event time, alert time, acknowledgement time, containment time, closure time

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024, RBI IT/Cyber, NIST CSF

**Writing note:** Define every metric. Averages hide outliers, so show a percentile where possible.

## F3: Alert Quality

**Purpose:** Show signal versus noise.

**Content blocks**

- Alert volume by severity
- True positive, false positive, and benign rates
- Top noisy rules and tuning actions
- Escalation rate

**Inputs from the user**

- How dispositions are recorded

**Data from the SIEM (vendor-neutral)**

- Alert disposition counts
- Alerts per rule
- Escalated alerts

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, MITRE ATT&CK, NIST CSF

## F4: Workload and Capacity

**Purpose:** Show whether staffing matches demand.

**Content blocks**

- Alerts and cases per shift
- Backlog and aging
- Capacity versus demand trend

**Inputs from the user**

- Shift model and headcount (aggregate)

**Data from the SIEM (vendor-neutral)**

- Queue size over time
- Case aging
- Volume by hour or shift

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber

**Writing note:** Report team-level figures. Avoid ranking individuals unless the user asks.

## F5: Automation and Playbook Impact

**Purpose:** Show the value of automation.

**Content blocks**

- Automated actions executed
- Manual effort saved (stated method)
- Playbook usage and exceptions

**Inputs from the user**

- How time saved is estimated

**Data from the SIEM (vendor-neutral)**

- Automation run counts
- Playbook execution outcomes

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## F6: Quality Assurance

**Purpose:** Show cases are handled consistently.

**Content blocks**

- Sampled case review method
- Quality scores (aggregate)
- Common defects and corrective training

**Inputs from the user**

- QA checklist
- Sample size

**Data from the SIEM (vendor-neutral)**

- Case records for sampling

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## F7: Findings and Improvement Plan

**Purpose:** Turn metrics into action.

**Content blocks**

- Action table (issue, action, owner, date)

**Inputs from the user**

- Planned improvements

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## F8: Sign-Off and Acknowledgement

**Purpose:** Record review.

**Content blocks**

- Team-level sign-off
- Disclaimer

**Inputs from the user**

- Roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
