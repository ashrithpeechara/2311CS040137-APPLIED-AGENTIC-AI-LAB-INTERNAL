"""
Visualizer Module for SQL ReAct Agent.
Generates research-grade charts illustrating tool usage distribution, step complexity, and agent success.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Any, List
from project.config import OUTPUT_DIR

# Style configuration
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = "#cccccc"
plt.rcParams["axes.linewidth"] = 0.8

SQL_TOOL_USAGE_PATH = OUTPUT_DIR / "sql_tool_usage.png"
SQL_AGENT_SUCCESS_PATH = OUTPUT_DIR / "sql_agent_success.png"


def generate_sql_visualizations(benchmark_data: Dict[str, Any]) -> List[str]:
    """Generates charts for ReAct SQL agent tool usage and trajectory analysis."""
    tasks = benchmark_data["task_results"]
    tool_usage = benchmark_data["tool_usage_summary"]
    generated_charts = []

    # 1. TOOL USAGE DISTRIBUTION CHART
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
    tools = list(tool_usage.keys())
    counts = list(tool_usage.values())
    tool_labels = [t.replace("_", " ").title() for t in tools]
    colors_list = ["#3b82f6", "#10b981", "#f59e0b", "#8b5cf6"]

    bars = ax.bar(tool_labels, counts, color=colors_list, width=0.55, edgecolor="#1e293b", linewidth=1.2)
    ax.set_ylabel("Total Invocations", fontsize=11, fontweight="bold", color="#1e293b")
    ax.set_title("ReAct SQL Agent: Database Tool Invocations Across Tasks", fontsize=12, fontweight="bold", pad=15)
    ax.set_ylim(0, max(counts) + 2)
    ax.grid(True, linestyle="--", alpha=0.5)

    for bar in bars:
        h = bar.get_height()
        ax.annotate(f"{h} calls",
                    xy=(bar.get_x() + bar.get_width() / 2, h),
                    xytext=(0, 4), textcoords="offset points",
                    ha="center", va="bottom", fontsize=9.5, fontweight="bold", color="#0f172a")

    plt.tight_layout()
    plt.savefig(SQL_TOOL_USAGE_PATH, dpi=300)
    plt.close()
    generated_charts.append(str(SQL_TOOL_USAGE_PATH))

    # 2. TRAJECTORY DEPTH & LATENCY ANALYSIS PER TASK
    fig, ax1 = plt.subplots(figsize=(9, 4.8), dpi=300)
    task_names = [f"Task {i+1}:\n" + t["task_title"][:18] + "..." for i, t in enumerate(tasks)]
    steps = [t["total_steps"] for t in tasks]
    latencies = [t["latency_ms"] for t in tasks]
    x = np.arange(len(task_names))
    width = 0.35

    color_steps = "#6366f1"
    color_lat = "#ec4899"

    rects1 = ax1.bar(x - width/2, steps, width, label="Trajectory Steps (Depth)", color=color_steps, alpha=0.9, edgecolor="#4338ca")
    ax1.set_ylabel("ReAct Reasoning Steps", color=color_steps, fontsize=11, fontweight="bold")
    ax1.tick_params(axis="y", labelcolor=color_steps)
    ax1.set_ylim(0, max(steps) + 2)

    ax2 = ax1.twinx()
    rects2 = ax2.bar(x + width/2, latencies, width, label="Execution Latency (ms)", color=color_lat, alpha=0.85, edgecolor="#be185d")
    ax2.set_ylabel("Latency (ms)", color=color_lat, fontsize=11, fontweight="bold")
    ax2.tick_params(axis="y", labelcolor=color_lat)
    ax2.set_ylim(0, max(latencies) * 1.3)

    ax1.set_title("ReAct SQL Agent: Reasoning Depth vs Response Latency", fontsize=12.5, fontweight="bold", pad=15)
    ax1.set_xticks(x)
    ax1.set_xticklabels(task_names, fontsize=9, fontweight="semibold")
    ax1.grid(True, linestyle="--", alpha=0.4)

    for rect in rects1:
        h = rect.get_height()
        ax1.annotate(f"{h} steps",
                    xy=(rect.get_x() + rect.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=8.5, fontweight="bold", color="#312e81")

    for rect in rects2:
        h = rect.get_height()
        ax2.annotate(f"{h:.0f}ms",
                    xy=(rect.get_x() + rect.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=8.5, fontweight="bold", color="#831843")

    plt.tight_layout()
    plt.savefig(SQL_AGENT_SUCCESS_PATH, dpi=300)
    plt.close()
    generated_charts.append(str(SQL_AGENT_SUCCESS_PATH))

    return generated_charts
