import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# Base Directories
ROOT_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = ROOT_DIR / "project"
OUTPUT_DIR = ROOT_DIR / "output"
PDF_DIR = ROOT_DIR / "pdf"

# Ensure output directories exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PDF_DIR.mkdir(parents=True, exist_ok=True)

# Lab Examination & Student Metadata
LAB_TITLE = "Agentic AI Lab Internal Examination"
STUDENT_NAME = "ashrith"
STUDENT_ROLL_NO = "2311CS040137"
COURSE_NAME = "Agentic AI & Advanced LLM Architectures"
EXPERIMENT_NAME = "Reasoning Model Benchmarking Across Diverse Prompting Strategies"

# API & Model Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or ""
DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
TEMPERATURE = 0.2  # Low temperature for deterministic reasoning evaluation
MAX_OUTPUT_TOKENS = 2048

# Output File Paths
RESULTS_JSON_PATH = OUTPUT_DIR / "benchmark_results.json"
RESULTS_CSV_PATH = OUTPUT_DIR / "benchmark_results.csv"
CHART_ACCURACY_PATH = OUTPUT_DIR / "prompting_strategies_accuracy.png"
CHART_LATENCY_TOKENS_PATH = OUTPUT_DIR / "latency_and_tokens_comparison.png"
CHART_RADAR_PATH = OUTPUT_DIR / "reasoning_dimensions_radar.png"
PDF_REPORT_PATH = PDF_DIR / "Agentic_AI_Lab_Report_2311CS040137.pdf"
