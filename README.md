# Agentic AI Lab Internal Examination
**Student Name:** ashrith  
**Roll No:** 2311CS040137  
**Course:** Agentic AI & Advanced LLM Architectures  

---

## 🔬 Lab Experiments Included

### 1️⃣ Experiment 1: Reasoning Model Benchmarking Across Prompting Strategies
- **Objective:** Compare outputs and quantify reasoning accuracy across 5 prompting paradigms:
  1. *Zero-Shot Direct*
  2. *Few-Shot In-Context ($k=2$)*
  3. *Chain-of-Thought (CoT)*
  4. *Step-Back Abstraction*
  5. *Least-to-Most Decomposition*
- **Test Suite:** Mathematical Combinatorics, Symbolic Knights & Knaves Logic, Algorithmic Task Scheduling, and Counterfactual Invariant Tracking.
- **Runner:** `python run_benchmark.py --fast`
- **Output Report:** [`pdf/Agentic_AI_Lab_Report_2311CS040137.pdf`](file:///c:/Users/ashri/OneDrive/Desktop/internal_assessment_agentic_ai/pdf/Agentic_AI_Lab_Report_2311CS040137.pdf)

---

### 2️⃣ Experiment 2: SQL Agent with Tool Use (ReAct Architecture)
- **Objective:** Develop an autonomous ReAct (Reasoning + Acting) SQL database agent equipped with dynamic introspection, validation, and safe query execution tools.
- **Tools Provided:**
  - `list_tables()`: Introspects database schema metadata.
  - `get_schema(table)`: Retrieves DDL, column types, foreign keys, and live sample rows.
  - `validate_sql(query)`: Dry-runs SQL queries via `EXPLAIN QUERY PLAN` to catch errors pre-execution.
  - `execute_sql(query)`: Safely executes read-only `SELECT` queries with safety guards against mutations.
- **Database:** SQLite E-Commerce Relational Schema (`customers`, `products`, `orders`, `order_items`, `payments`).
- **Capabilities:** Multi-table relational joins, financial aggregations, and self-healing error recovery.
- **Runner:** `python run_sql_agent.py`
- **Output Report:** [`pdf/Agentic_AI_Lab_Report_SQL_Agent_2311CS040137.pdf`](file:///c:/Users/ashri/OneDrive/Desktop/internal_assessment_agentic_ai/pdf/Agentic_AI_Lab_Report_SQL_Agent_2311CS040137.pdf)

---

## 📁 Repository Directory Structure

```
internal_assessment_agentic_ai/
├── project/                     # Total development work
│   ├── __init__.py
│   ├── config.py                # Configurations, metadata, file paths
│   ├── strategies.py            # Exp 1: Prompting strategies definitions
│   ├── benchmark_suite.py       # Exp 1: Reasoning tasks suite
│   ├── evaluator.py             # Exp 1: Scoring engine & API invocation
│   ├── visualizer.py            # Exp 1: Comparative plots & radar charts
│   ├── sql_db.py                # Exp 2: SQLite E-Commerce database setup
│   ├── sql_tools.py             # Exp 2: Database tool suite (list, schema, validate, execute)
│   ├── sql_benchmark_suite.py   # Exp 2: Relational business queries test suite
│   ├── sql_react_agent.py       # Exp 2: ReAct agent reasoning & execution loop
│   └── sql_visualizer.py        # Exp 2: Tool invocations & trajectory charts
├── output/                      # All experimental outputs & visualizations
│   ├── ecommerce.db             # Relational SQLite database
│   ├── benchmark_results.json   # Exp 1: JSON traces
│   ├── benchmark_results.csv    # Exp 1: Tabular results
│   ├── prompting_strategies_accuracy.png
│   ├── latency_and_tokens_comparison.png
│   ├── reasoning_dimensions_radar.png
│   ├── sql_agent_results.json   # Exp 2: Trajectory logs
│   ├── sql_agent_results.csv    # Exp 2: SQL tabular results
│   ├── sql_tool_usage.png       # Exp 2: Tool invocations chart
│   └── sql_agent_success.png    # Exp 2: Trajectory depth chart
├── pdf/                         # Examination PDF Reports
│   ├── generate_report.py       # Exp 1 PDF compiler
│   ├── generate_sql_report.py   # Exp 2 PDF compiler
│   ├── Agentic_AI_Lab_Report_2311CS040137.pdf           # Exp 1 Report
│   └── Agentic_AI_Lab_Report_SQL_Agent_2311CS040137.pdf # Exp 2 Report
├── run_benchmark.py             # Exp 1 orchestrator
├── run_sql_agent.py             # Exp 2 orchestrator
├── requirements.txt             # Project dependencies
├── .env.example                 # Environment variable template
└── README.md                    # Project documentation
```

---

## 🚀 How to Run

### Run Experiment 1 (Prompting Strategies Benchmark):
```bash
python run_benchmark.py --fast
```

### Run Experiment 2 (ReAct SQL Agent with Tool Use):
```bash
python run_sql_agent.py
```
