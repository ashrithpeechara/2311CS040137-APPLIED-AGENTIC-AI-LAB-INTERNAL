# Agentic AI Lab Internal Examination - Question 3 Output

**Student Name:** ashrith  
**Roll No:** 2311CS040137  
**Experiment:** Policy Compliance Agent with Rule-Based Evaluation & Synthetic Data  

---

## 1. Executive Summary & Governance Architecture
This project develops an autonomous **Policy Compliance Agent** combining **synthetic multi-domain compliance data generation** with a **deterministic rule evaluation engine**.
- **Supported Regulatory Domains:** Financial/AML (FinCEN, FATF), Data Privacy (GDPR, CCPA), Healthcare (HIPAA PHI), Information Security (SOC2 MFA), and AI Governance (Fair Lending).
- **Evaluation Mechanism:** Real-time payload schema inspection, regex entity redaction, mathematical threshold validation, and automated remediation generation.

---

## 2. Quantitative Evaluation Table

| Record ID | Regulatory Domain | Scenario Description | Audit Outcome | Score | Accuracy |
| :--- | :--- | :--- | :---: | :---: | :---: |
| `SYNTH_TX_001` | Financial & AML Compliance | Cross-Border Wire Transfer Exceeding Reporting Threshold | <font color='red'>**NON_COMPLIANT**</font> | **30.0%** | **100%** |
| `SYNTH_PII_002` | Data Privacy & GDPR | Customer Support Ticket Containing Unmasked PII | <font color='red'>**NON_COMPLIANT**</font> | **30.0%** | **100%** |
| `SYNTH_SEC_003` | InfoSec & Access Control | Production Cloud Infrastructure Access with MFA Enabled | **COMPLIANT** | **100.0%** | **100%** |
| `SYNTH_HEALTH_004` | Healthcare & HIPAA | Patient Clinical Summary Data Sharing Without De-Identification | <font color='red'>**NON_COMPLIANT**</font> | **65.0%** | **100%** |
| `SYNTH_AI_005` | AI Governance & Fair Lending | Credit Underwriting Model Risk Assessment with Explanations | **COMPLIANT** | **100.0%** | **100%** |

---

## 3. Detected Violations & Remediation Sample

### Case: `SYNTH_PII_002` (Data Privacy & GDPR)
- **Detected Breach:** Plaintext credit card (PCI) and SSN exposed in unencrypted support communication.
- **Triggered Rule:** `RULE_PRIV_01_PII_EXPOSURE` (Severity: CRITICAL)
- **Remediation Action:** Immediately redact sensitive regex entities and route through encrypted DLP vault.

### Case: `SYNTH_TX_001` (Financial AML)
- **Detected Breach:** Wire transfer of $15,000 to offshore high-risk jurisdiction without SAR filing.
- **Triggered Rule:** `RULE_FIN_01_THRESHOLD` & `RULE_FIN_02_HIGH_RISK_JURISDICTION` (Severity: CRITICAL)
- **Remediation Action:** Trigger Enhanced Due Diligence (EDD) and auto-file FinCEN Form 112.

---

## 4. Visual Analytics Generated
- `compliance_distribution.png`: Horizontal bar chart of compliance scores per regulatory domain.
- `policy_risk_radar.png`: Rule severity and governance policy breakdown.
