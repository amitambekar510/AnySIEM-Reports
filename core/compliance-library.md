# Compliance Library

Indicative reference for the frameworks this project supports. **Mappings are
a starting point, not legal advice.** Before you cite any obligation, deadline,
or control number in a report, confirm it against the current official source.
If you cannot, mark it "to be confirmed".

| Code | Framework | Official source to verify |
|---|---|---|
| CERTIN | CERT-In Directions, April 2022 | cert-in.org.in |
| CSCRF | SEBI Cyber Security and Cyber Resilience Framework, 2024 | sebi.gov.in |
| RBI | RBI IT and Cyber Security Frameworks (banks and NBFCs) | rbi.org.in |
| DPDP | Digital Personal Data Protection Act, 2023 and its Rules | meity.gov.in |
| ISO27001 | ISO/IEC 27001 Information Security Management | iso.org |
| ISO42001 | ISO/IEC 42001 Information technology, Artificial intelligence, Management system | iso.org |
| ISO27090 | ISO/IEC 27090 Cybersecurity, Artificial intelligence, Addressing security threats and compromises to AI systems | iso.org/standard/27090 |
| ATTACK | MITRE ATT&CK Enterprise | attack.mitre.org |
| NIST | NIST Cybersecurity Framework (and incident handling guidance) | nist.gov |
| EXCH | NSE / BSE Annual Technology Audit requirements | nseindia.com, bseindia.com |
| NPCI | NPCI / UPI payment security guidelines | npci.org.in |
| PFUTP | SEBI PFUTP Regulations, 2003 | sebi.gov.in |

## What each framework typically asks a SOC report to evidence

**CERTIN.** Incident reporting to CERT-In within the prescribed window (6 hours
from noticing, as published in April 2022), the incident categories listed in
the Directions, log retention within Indian jurisdiction (180 days as
published), time synchronization with designated NTP sources, and a designated
point of contact. *Verify for later updates.*

**CSCRF.** A function-based cybersecurity and resilience framework for SEBI
regulated entities, aligned with NIST CSF functions. Relevant report evidence:
monitoring coverage, incident detection and response, root cause analysis,
periodic audit evidence, and governance. Applicability and timelines depend on
entity category. *Verify the current circular.*

**RBI.** For banks and NBFCs: IT governance, security operations monitoring,
incident reporting to the regulator, and cyber crisis management evidence.
*Verify the applicable Master Direction or circular for the entity type.*

**DPDP.** Where an incident involves personal data: breach assessment,
notification to the regulator and affected individuals as the Act and Rules
require, and records of the decision. *Verify the Rules in force.*

**ISO27001 (2022 Annex A, commonly relevant).** Threat intelligence (A.5.7),
incident management (A.5.24 to A.5.28), logging (A.8.15), monitoring
activities (A.8.16), technical vulnerability management (A.8.8), awareness
(A.6.3). Plus clause 7.5 documented information and clause 10 improvement.

**ISO42001.** Published in December 2023. It specifies requirements for
establishing, implementing, maintaining, and continually improving an artificial
intelligence management system (AIMS) in an organization that develops,
provides, or uses AI systems. It is risk-based and process-oriented, follows
the high-level structure common to management system standards, and can be
integrated with ISO/IEC 27001. Certification applies to an organization's
management system, not to products or services. Indicative report evidence: AIMS
scope and policy, AI risk and impact assessment, operational controls across
the AI life cycle, monitoring and measurement, internal audit, management
review, corrective action, and certification status supplied by the user.
*Verify against the licensed standard. Never claim certification without
certificate details from the user. Do not state clause numbers you have not
confirmed.*

**ISO27090.** Published in October 2026 (Edition 1) as guidance on understanding,
detecting, and mitigating security threats specific to AI systems across their
life cycle, such as data poisoning and model theft. It complements ISO/IEC
27001 and ISO/IEC 27002 rather than replacing them. Indicative report
evidence: which AI systems exist and who owns them, the assets that need
protection (training data, models), monitoring and detection coverage for
AI-specific threats, handling of data used for model updates or retraining,
and incidents involving AI systems. It is published as guidance. Confirm
whether any regulator, contract, or internal policy makes it a requirement.
It covers securing AI systems. It does not cover using AI to write reports.
In this project it is forward-looking guidance, kept for future upgrades, and
not treated as a current requirement.
*Verify against the licensed standard. Do not state clause numbers you have not
confirmed.*

**ATTACK.** Map detections and incidents to tactics and techniques. Show
coverage honestly, including gaps.

**NIST.** CSF functions (Govern, Identify, Protect, Detect, Respond, Recover)
and the incident handling lifecycle. *Verify the current revision.*

**EXCH.** Evidence of monitoring, logging, incident handling, and corrective
actions supporting the annual technology audit. *Follow the exchange's current
circulars.*

**NPCI.** For payment participants: security monitoring, incident reporting to
the network operator, and log retention. *Verify current guidelines.*

**PFUTP.** Relevant only where SOC evidence may support the investigation of
unauthorized access to, or manipulation of, trading-related systems. The
applicability decision belongs to the legal and compliance team.

## Note on standards copyright

Paywalled standards are protected by copyright. ISO states on its website that
its content may not be used to prompt or enable AI tools to generate responses,
except content available through its Open Data page. For that reason:

- This project contains no text from ISO standards. It uses short, descriptive
  summaries, titles, and control identifiers only.
- The AI must not fetch, paste, or summarize the text of a paywalled standard.
- The AI asks the user for their own inputs. If the user holds a licensed copy,
  the user decides what to share and should check the publisher's terms.

## Rules for the AI

1. Ask which frameworks apply. Map only those.
2. Use the mapping tables as hints. Confirm each cited item.
3. Never state a deadline or control number you have not verified.
4. Put unverified items in a "To be confirmed with compliance" note.
5. Never reproduce text from paywalled standards (see the copyright note above).
