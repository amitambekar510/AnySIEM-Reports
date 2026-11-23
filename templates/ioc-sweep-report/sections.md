# IOC Sweep (Retro-Hunt) Report: Section Blueprint

Blueprint for an indicator sweep report. A sweep with no matches is a valid result when limits are stated.

## Section index

| ID | Section | Include |
|---|---|---|
| IS0 | Cover and Document Control | Always |
| IS1 | Sweep Objective and Trigger | Always |
| IS2 | Indicator Set | Always |
| IS3 | Scope and Time Window | Always |
| IS4 | Method | Always |
| IS5 | Results | Always |
| IS6 | Verified Matches and Response | When any match was confirmed |
| IS7 | Limitations | Always |
| IS8 | Follow-up Actions | Always |
| IS9 | Sign-Off and Acknowledgement | Always |

## IS0: Cover and Document Control

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

## IS1: Sweep Objective and Trigger

**Purpose:** Explain why the sweep ran.

**Content blocks**

- Trigger
- Objective
- Authorization

**Inputs from the user**

- Trigger and authorization

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF, CERT-In 2022

## IS2: Indicator Set

**Purpose:** Describe what was searched.

**Content blocks**

- Indicator types and counts
- Source types and dates
- Confidence and age

**Inputs from the user**

- Indicator set summary

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, ISO/IEC 27001

## IS3: Scope and Time Window

**Purpose:** State the boundaries.

**Content blocks**

- Data sources searched
- Time window
- Retention limits that affected the window

**Inputs from the user**

- Scope

**Data from the SIEM (vendor-neutral)**

- Retention and source availability

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001

## IS4: Method

**Purpose:** Make it repeatable.

**Content blocks**

- Search approach described generically
- Validation of matches

**Inputs from the user**

- Method

**Data from the SIEM (vendor-neutral)**

- Search features used

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, NIST CSF

## IS5: Results

**Purpose:** Report what was found.

**Content blocks**

- Matches by indicator type
- No-match statement with limits
- False positives

**Inputs from the user**

- Results

**Data from the SIEM (vendor-neutral)**

- Match counts and context

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, MITRE ATT&CK

**Writing note:** No match is not proof of no compromise. State the limits.

## IS6: Verified Matches and Response

**Purpose:** Handle real hits.

**Include when:** When any match was confirmed

**Content blocks**

- Confirmed matches
- Containment and escalation
- Linked incident references

**Inputs from the user**

- Actions

**Data from the SIEM (vendor-neutral)**

- Case references

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, NIST CSF

## IS7: Limitations

**Purpose:** Be candid.

**Content blocks**

- Visibility gaps
- Retention gaps
- Indicator quality

**Inputs from the user**

- Known limits

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## IS8: Follow-up Actions

**Purpose:** Plan next steps.

**Content blocks**

- Detections added
- Recurring sweep plan

**Inputs from the user**

- Actions

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, MITRE ATT&CK

## IS9: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
