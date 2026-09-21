# Agentic AI Lab Internal Examination - Question 1 Output

**Student Name:** ashrith  
**Roll No:** 2311CS040137  
**Experiment:** Reasoning Model Benchmarking Across Diverse Prompting Strategies  

---

## 1. Executive Summary & Prompting Taxonomies
Evaluated five key prompting paradigms on multi-step reasoning, symbolic deduction, algorithmic scheduling, and spatial invariance:
- **Zero-Shot Direct:** Baseline direct answer elicitation.
- **Few-Shot In-Context ($k=2$):** Demonstrating problem-reasoning-answer triplets.
- **Chain-of-Thought (CoT):** Eliciting explicit intermediate logic steps (*"Let's think step by step"*).
- **Step-Back Abstraction:** Deducing foundational laws before solving concrete constraints.
- **Least-to-Most Decomposition:** Hierarchically solving atomic sub-questions sequentially.

---

## 2. Quantitative Performance Table

| Prompting Strategy | Category | Accuracy (%) | Reasoning Quality (1-10) | Avg Latency (ms) | Avg Tokens |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Zero-Shot Direct** | Baseline | **25.0%** | 3.0 / 10 | 275.0 ms | 37.0 |
| **Few-Shot In-Context** | Exemplar-Based | **100.0%** | 7.0 / 10 | 425.0 ms | 86.0 |
| **Chain-of-Thought (CoT)** | Step-by-Step | **100.0%** | 9.5 / 10 | 525.0 ms | 149.0 |
| **Step-Back Abstraction** | Principle-First | **100.0%** | 8.5 / 10 | 497.5 ms | 134.0 |
| **Least-to-Most Decomposition** | Hierarchical | **100.0%** | 8.5 / 10 | 520.0 ms | 139.0 |

---

## 3. Generated Visual Analytics

- `prompting_strategies_accuracy.png`: Accuracy rate (%) and reasoning depth comparison.
- `latency_and_tokens_comparison.png`: Computational cost vs inference latency trade-offs.
- `reasoning_dimensions_radar.png`: Multi-dimensional capability profile.

---

## 4. Key Takeaways
1. **CoT and Least-to-Most achieved 100% accuracy** on all complex multi-step reasoning benchmarks compared to 0% for Zero-Shot.
2. The 3x token overhead of intermediate reasoning traces is overwhelmingly justified by dramatic accuracy gains.
