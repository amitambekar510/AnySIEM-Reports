# Malicious IP and Top-Talker Report: Section Blueprint

Blueprint for a top-talker and malicious address report. The address list itself belongs in a controlled channel, not in the PDF.

## Section index

| ID | Section | Include |
|---|---|---|
| MT0 | Cover and Document Control | Always |
| MT1 | Purpose and Method | Always |
| MT2 | Top External Talkers | Always |
| MT3 | Top Internal Talkers | Always |
| MT4 | Findings by Category | Always |
| MT5 | Required Client Action | Always |
| MT6 | Review and Cleanup Process | Always |
| MT7 | Trends | Always |
| MT8 | Sign-Off and Acknowledgement | Always |

## MT0: Cover and Document Control

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

## MT1: Purpose and Method

**Purpose:** Explain how top talkers were found and checked.

**Content blocks**

- Selection method
- Reputation check approach using source types (open, community, commercial)
- Period covered

**Inputs from the user**

- Method details

**Data from the SIEM (vendor-neutral)**

- Traffic summary features used

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, NIST CSF

## MT2: Top External Talkers

**Purpose:** Show the busiest external addresses.

**Content blocks**

- Table: address, country or network if available, direction, volume, connections, reputation verdict, action

**Inputs from the user**

- Which fields to show

**Data from the SIEM (vendor-neutral)**

- Top external sources and destinations
- Connection counts
- Bytes transferred

**Compliance hooks (indicative, verify before citing):** CERT-In 2022, MITRE ATT&CK

## MT3: Top Internal Talkers

**Purpose:** Show the busiest internal hosts.

**Content blocks**

- Table: host, destinations, volume, business justification

**Inputs from the user**

- Known high-bandwidth systems

**Data from the SIEM (vendor-neutral)**

- Top internal hosts by volume

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

## MT4: Findings by Category

**Purpose:** Separate signal from noise.

**Content blocks**

- Confirmed malicious
- Suspicious
- Benign high-bandwidth

**Inputs from the user**

- Context from client IT

**Data from the SIEM (vendor-neutral)**

- Reputation and behavior data

**Compliance hooks (indicative, verify before citing):** MITRE ATT&CK, CERT-In 2022, NIST CSF

## MT5: Required Client Action

**Purpose:** State what the client must do.

**Content blocks**

- Review the shared list
- Confirm blocking at the perimeter and on every other control that can block or control traffic
- Reply with blocked status in the same email chain

**Inputs from the user**

- Delivery channel for the list

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001, SEBI CSCRF 2024

**Writing note:** Put the list in the secure channel, not in the PDF.

## MT6: Review and Cleanup Process

**Purpose:** Handle disputed addresses.

**Content blocks**

- How clients request a reputation review
- Removal and non-re-addition rule

**Inputs from the user**

- Process details

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## MT7: Trends

**Purpose:** Show change over time.

**Content blocks**

- Comparison with prior periods

**Inputs from the user**

- Prior-period data

**Data from the SIEM (vendor-neutral)**

- Historical top-talker data

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001

## MT8: Sign-Off and Acknowledgement

**Purpose:** Record organization-level review.

**Content blocks**

- Team-level sign-off table
- Disclaimer

**Inputs from the user**

- Sign-off roles

**Data from the SIEM (vendor-neutral)**

- None

**Compliance hooks (indicative, verify before citing):** ISO/IEC 27001
