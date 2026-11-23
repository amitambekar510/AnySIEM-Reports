# Daily Alert and Incident Tracker: Section Blueprint

Blueprint for a tracker. The deliverable is a PDF table. The AI also offers the field definitions so the user can rebuild the tracker in their own tool.

## Section index

| ID | Section | Include |
|---|---|---|
| AT0 | Cover and Document Control | Always |
| AT1 | Tracker Header and Scope | Always |
| AT2 | Field Definitions | Always |
| AT3 | Status and Disposition Values | Always |
| AT4 | Tracker Log | Always |
| AT5 | Aging and Closure Rules | Always |
| AT6 | Summary Counts | Always |

## AT0: Cover and Document Control

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

## AT1: Tracker Header and Scope

**Purpose:** Define what the tracker covers.

**Content blocks**

- Period, environment, owner
- Severity scheme

**Inputs from the user**

- Period and scope

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## AT2: Field Definitions

**Purpose:** Make entries consistent.

**Content blocks**

- Field table: ID, detected time, source, rule, severity, category, status, owner, disposition, linked incident, closure time

**Inputs from the user**

- Any extra fields wanted

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## AT3: Status and Disposition Values

**Purpose:** Standardize values.

**Content blocks**

- Allowed statuses
- Allowed dispositions (true positive, false positive, benign, informational)

**Inputs from the user**

- Your values

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## AT4: Tracker Log

**Purpose:** Hold the entries.

**Content blocks**

- Table of entries for the period

**Inputs from the user**

- Entries to include

**Data from the SIEM (vendor-neutral)**

- Alert and case exports

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, SEBI CSCRF 2024, RBI IT/Cyber

## AT5: Aging and Closure Rules

**Purpose:** Keep items moving.

**Content blocks**

- Aging thresholds
- Closure criteria
- Escalation of aged items

**Inputs from the user**

- Thresholds

**Data from the SIEM (vendor-neutral)**

- Case age data

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, RBI IT/Cyber

## AT6: Summary Counts

**Purpose:** Summarize.

**Content blocks**

- Counts by severity, status, and disposition

**Inputs from the user**

- None

**Data from the SIEM (vendor-neutral)**

- Counts

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
