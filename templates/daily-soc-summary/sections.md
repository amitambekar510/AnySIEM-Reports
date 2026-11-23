# Daily SOC Summary and Shift Handover: Section Blueprint

Blueprint for a compact daily or per-shift report. Keep it to one or two pages.

## Section index

| ID | Section | Include |
|---|---|---|
| DS0 | Cover and Document Control | Always |
| DS1 | Shift Overview | Always |
| DS2 | Alert and Incident Activity | Always |
| DS3 | Notable Events | Always |
| DS4 | Platform and Log Source Exceptions | Always |
| DS5 | Open Items and Handover | Always |
| DS6 | Handover Acknowledgement | Always |

## DS0: Cover and Document Control

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

## DS1: Shift Overview

**Purpose:** Show who covered the shift and the platform state.

**Content blocks**

- Date, shift, and coverage (roles or headcount)
- Platform status at start and end of shift

**Inputs from the user**

- Shift pattern and coverage model

**Data from the SIEM (vendor-neutral)**

- Platform status
- Source health exceptions

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber

## DS2: Alert and Incident Activity

**Purpose:** Summarize workload and outcomes.

**Content blocks**

- Alerts by severity (opened, closed, carried over)
- Incidents opened, updated, and closed
- Escalations made

**Inputs from the user**

- Severity scheme

**Data from the SIEM (vendor-neutral)**

- Alert counts by severity
- Case status counts

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, NIST CSF

## DS3: Notable Events

**Purpose:** Explain what mattered most.

**Content blocks**

- Top events with status and next step
- Client communications made

**Inputs from the user**

- Events worth highlighting

**Data from the SIEM (vendor-neutral)**

- Most significant alerts or cases

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024

## DS4: Platform and Log Source Exceptions

**Purpose:** Record data gaps affecting monitoring.

**Content blocks**

- Silent or delayed sources
- Outages or degraded components
- Actions taken

**Inputs from the user**

- Known maintenance

**Data from the SIEM (vendor-neutral)**

- Sources with no data in the shift
- Ingestion delay indicators

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, ISO/IEC 27001

## DS5: Open Items and Handover

**Purpose:** Pass context to the next shift.

**Content blocks**

- Open cases with owner and next step
- Pending client actions
- Instructions for the incoming shift

**Inputs from the user**

- Handover notes

**Data from the SIEM (vendor-neutral)**

- Open case list

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## DS6: Handover Acknowledgement

**Purpose:** Record the handover.

**Content blocks**

- Outgoing and incoming roles and time of handover

**Inputs from the user**

- Roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
