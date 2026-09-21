# Agentic AI Lab Internal Examination
**Student Name:** ashrith  
**Roll No:** 2311CS040137  
**Course:** Agentic AI & Advanced LLM Architectures  

---

## 📁 Repository Structure

```
2311CS040137-Agnetic-AI-Lab Internal/
├── Question 1/
│   ├── code/
│   │   └── run_q1.py                 # Reasoning Model Benchmarking (5 Prompting Strategies)
│   └── output/
│       ├── output.md                 # Markdown results & analysis
│       ├── benchmark_results.json    # JSON evaluation traces
│       ├── benchmark_results.csv     # Tabular performance metrics
│       ├── prompting_strategies_accuracy.png
│       ├── latency_and_tokens_comparison.png
│       └── reasoning_dimensions_radar.png
│
├── Question 2/
│   ├── code/
│   │   └── run_q2.py                 # SQL Agent with Database Tools (ReAct Architecture)
│   └── output/
│       ├── output.md                 # Markdown results, trajectories & self-healing case study
│       ├── ecommerce.db              # Relational SQLite database
│       ├── sql_agent_results.json    # ReAct reasoning & execution logs
│       ├── sql_agent_results.csv     # Tabular query metrics
│       ├── sql_tool_usage.png        # Tool invocation breakdown chart
│       └── sql_agent_success.png     # Trajectory reasoning depth chart
│
├── Question 3/
│   ├── code/
│   │   └── run_q3.py                 # Policy Compliance Agent (Rule-Based Evaluation + Synthetic Data)
│   └── output/
│       ├── output.md                 # Markdown results & compliance audit report
│       ├── synthetic_compliance_data.json # Multi-domain synthetic compliance dataset
│       ├── compliance_results.json   # Full audit results & remediation actions
│       ├── compliance_results.csv    # Tabular compliance metrics
│       ├── compliance_distribution.png # Domain compliance score distribution
│       └── policy_risk_radar.png     # Rule severity & governance breakdown
│
└── Reports/
    ├── generate_all_reports.py       # Master PDF report compiler
    ├── Report_Question_1_2311CS040137.pdf  # PDF Report for Question 1 (3 Pages)
    ├── Report_Question_2_2311CS040137.pdf  # PDF Report for Question 2 (3 Pages)
    └── Report_Question_3_2311CS040137.pdf  # PDF Report for Question 3 (3 Pages)
```

---

## 🔬 Examination Questions Overview

### 1️⃣ Question 1: Reasoning Model Benchmarking Across Prompting Strategies
- **Paradigms Evaluated:** *Zero-Shot Direct, Few-Shot In-Context ($k=2$), Chain-of-Thought (CoT), Step-Back Abstraction, Least-to-Most Decomposition*.
- **Benchmark Suite:** Mathematical Combinatorics, Symbolic Knights & Knaves Logic, Algorithmic Task Scheduling, and Counterfactual Invariant Tracking.
- **Run:** `python "2311CS040137-Agnetic-AI-Lab Internal/Question 1/code/run_q1.py"`

### 2️⃣ Question 2: SQL Agent with Tool Use (ReAct Architecture)
- **Agent Paradigm:** ReAct (Reasoning + Acting) loop with pre-execution validation and schema self-healing.
- **Database Tools:** `list_tables()`, `get_schema()`, `validate_sql()`, `execute_sql()`.
- **Database Schema:** SQLite E-Commerce Relational Database (`customers`, `products`, `orders`, `order_items`, `payments`).
- **Run:** `python "2311CS040137-Agnetic-AI-Lab Internal/Question 2/code/run_q2.py"`

### 3️⃣ Question 3: Policy Compliance Agent (Rule-Based Evaluation & Synthetic Data)
- **Capabilities:** Autonomous compliance auditing across Financial/AML, GDPR/CCPA PII, SOC2 MFA, HIPAA PHI, and AI Governance.
- **Engine:** Deterministic rule evaluation engine + synthetic compliance scenario generator + automated remediation generator.
- **Run:** `python "2311CS040137-Agnetic-AI-Lab Internal/Question 3/code/run_q3.py"`

---

## 📄 PDF Examination Reports
All PDF examination reports are located in [`2311CS040137-Agnetic-AI-Lab Internal/Reports/`](file:///c:/Users/ashri/OneDrive/Desktop/internal_assessment_agentic_ai/2311CS040137-Agnetic-AI-Lab%20Internal/Reports) with student details on all pages:
- **`Report_Question_1_2311CS040137.pdf`**
- **`Report_Question_2_2311CS040137.pdf`**
- **`Report_Question_3_2311CS040137.pdf`**

To recompile all reports:
```bash
python "2311CS040137-Agnetic-AI-Lab Internal/Reports/generate_all_reports.py"
```
