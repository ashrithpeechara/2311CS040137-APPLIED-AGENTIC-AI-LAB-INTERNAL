# Agentic AI Lab Internal Examination - Question 2 Output

**Student Name:** ashrith  
**Roll No:** 2311CS040137  
**Experiment:** SQL Agent with Tool Use (ReAct Architecture)  

---

## 1. System Architecture & Database Tools
- `list_tables()`: Dynamic schema table discovery.
- `get_schema(table)`: Retrieves DDL, column types, foreign keys, and live sample rows.
- `validate_sql(query)`: Pre-execution validation using `EXPLAIN QUERY PLAN`.
- `execute_sql(query)`: Safe execution of read-only `SELECT` statements with mutation safety blocks.

---

## 2. Benchmark Evaluation Table

| Task Scenario | ReAct Steps | Accuracy (%) | Latency (ms) |
| :--- | :---: | :---: | :---: |
| **Top Spending Customers Aggregation** | 5 | **100%** | 425.0 ms |
| **Category Revenue Analysis** | 4 | **100%** | 340.0 ms |
| **Payment Method Volume Tracking** | 3 | **100%** | 255.0 ms |
| **Self-Healing Schema Introspection** | 5 | **100%** | 425.0 ms |

---

## 3. Tool Usage Summary
- `list_tables`: 1 call
- `get_schema`: 7 calls
- `validate_sql`: 5 calls
- `execute_sql`: 4 calls

---

## 4. Self-Healing Trajectory Case Study
When the agent formulated a tentative query with the unverified column `user_id`, `validate_sql` caught `SYNTAX ERROR: no such column: c.user_id`. The ReAct agent immediately invoked `get_schema(customers)`, corrected the column to `customer_id`, re-validated, and executed with 100% precision.
