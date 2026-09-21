"""
Root Benchmark Orchestrator Script.
Runs the complete Reasoning Model Benchmarking PoC, outputs analytics, and generates the assessment PDF.
"""

import sys
import logging
from pathlib import Path

# Add project root to sys.path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from project.evaluator import GeminiReasoningEvaluator
from project.visualizer import generate_benchmark_visualizations
from pdf.generate_report import build_pdf_report
from project.config import (
    LAB_TITLE,
    STUDENT_NAME,
    STUDENT_ROLL_NO,
    RESULTS_JSON_PATH,
    RESULTS_CSV_PATH,
    PDF_REPORT_PATH
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("BenchmarkOrchestrator")


def main():
    use_fast = "--fast" in sys.argv or "--mock" in sys.argv
    
    print("=" * 70)
    print(f" {LAB_TITLE.upper()} ")
    print(f" Student: {STUDENT_NAME} | Roll No: {STUDENT_ROLL_NO}")
    print(" Experiment: Reasoning Model Benchmarking Across Prompting Strategies")
    print(f" Mode: {'Fast Offline Evaluation' if use_fast else 'Standard / Adaptive Live API'}")
    print("=" * 70)

    # 1. Execute Benchmark Suite
    logger.info("Step 1: Running Reasoning Benchmarks across 5 Prompting Strategies...")
    api_key_to_use = None if use_fast else None  # if None, reads from GEMINI_API_KEY config
    evaluator = GeminiReasoningEvaluator(api_key="" if use_fast else None)
    benchmark_data = evaluator.run_benchmark()

    # 2. Generate Comparative Analytics & Plots
    logger.info("Step 2: Generating Comparative Visualizations & Radar Plots...")
    charts = generate_benchmark_visualizations(benchmark_data)
    for c in charts:
        logger.info(f" -> Generated chart: {c}")

    # 3. Generate Examination PDF Report
    logger.info("Step 3: Compiling Publication-Grade PDF Examination Report...")
    pdf_path = build_pdf_report()
    logger.info(f" -> Generated PDF Report: {pdf_path}")

    # 4. Print Summary Terminal Output
    print("\n" + "=" * 70)
    print(" BENCHMARK PERFORMANCE SUMMARY ")
    print("=" * 70)
    print(f"{'Strategy Name':<28} | {'Accuracy':<10} | {'Quality':<10} | {'Latency':<12} | {'Tokens':<8}")
    print("-" * 70)
    for s in benchmark_data["strategy_aggregates"]:
        print(f"{s['strategy_name']:<28} | {s['accuracy_pct']:>8.1f}% | {s['avg_reasoning_quality']:>8.1f}/10 | {s['avg_latency_ms']:>8.1f} ms | {s['avg_tokens']:>6.0f}")
    print("=" * 70)

    print(f"\n[+] Total Outputs saved to: {RESULTS_JSON_PATH.parent.resolve()}")
    print(f"[+] PDF Examination Report: {PDF_REPORT_PATH.resolve()}")
    print("\nBenchmark PoC Completed Successfully!\n")


if __name__ == "__main__":
    main()
