"""
Root Runner Script for Experiment 2: ReAct SQL Agent with Tool Use.
Orchestrates SQLite database seeding, ReAct reasoning trajectories, visualizer, and PDF compilation.
"""

import sys
import logging
from pathlib import Path

# Add workspace to sys.path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from project.sql_react_agent import ReActSQLAgent
from project.sql_visualizer import generate_sql_visualizations
from pdf.generate_sql_report import build_sql_pdf_report
from project.config import (
    LAB_TITLE,
    STUDENT_NAME,
    STUDENT_ROLL_NO,
    OUTPUT_DIR,
    PDF_DIR
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SQLAgentOrchestrator")


def main():
    print("=" * 70)
    print(f" {LAB_TITLE.upper()} ")
    print(f" Student: {STUDENT_NAME} | Roll No: {STUDENT_ROLL_NO}")
    print(" Experiment 2: SQL Agent With Tool Use (ReAct Architecture)")
    print("=" * 70)

    # 1. Run ReAct Agent on Benchmark Tasks
    logger.info("Step 1: Running ReAct SQL Agent across benchmark database queries...")
    agent = ReActSQLAgent()
    benchmark_data = agent.run_all_benchmarks()

    # 2. Generate Visualizations
    logger.info("Step 2: Generating Tool Invocations and Trajectory Visualizations...")
    charts = generate_sql_visualizations(benchmark_data)
    for c in charts:
        logger.info(f" -> Generated chart: {c}")

    # 3. Generate PDF Report
    logger.info("Step 3: Compiling Publication-Grade PDF Examination Report for SQL Agent...")
    pdf_path = build_sql_pdf_report()
    logger.info(f" -> Generated PDF Report: {pdf_path}")

    # 4. Summary Table Output
    print("\n" + "=" * 70)
    print(" REACT SQL AGENT PERFORMANCE SUMMARY ")
    print("=" * 70)
    print(f"{'Task Title':<38} | {'Steps':<6} | {'Accuracy':<10} | {'Latency':<10}")
    print("-" * 70)
    for t in benchmark_data["task_results"]:
        print(f"{t['task_title']:<38} | {t['total_steps']:>5} | {t['accuracy_score']:>8.0f}% | {t['latency_ms']:>8.1f}ms")
    print("=" * 70)
    print("\nTool Invocations Breakdown:")
    for tool, count in benchmark_data["tool_usage_summary"].items():
        print(f"  • {tool:<15} : {count} invocations")
    print("=" * 70)

    print(f"\n[+] Results JSON/CSV saved to: {OUTPUT_DIR.resolve()}")
    print(f"[+] PDF Examination Report: {pdf_path.resolve()}")
    print("\nExperiment 2 Completed Successfully!\n")


if __name__ == "__main__":
    main()
