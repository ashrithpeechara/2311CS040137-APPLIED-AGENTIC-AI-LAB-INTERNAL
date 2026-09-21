"""
Prompting Strategies Taxonomy and Formatters for Reasoning Benchmarks.
"""

from typing import Dict, Any

STRATEGIES = {
    "zero_shot": {
        "id": "zero_shot",
        "name": "Zero-Shot Direct",
        "description": "Direct problem prompt without demonstrations or explicit reasoning instructions.",
        "category": "Baseline",
        "complexity": "O(1) Prompt Overhead",
    },
    "few_shot": {
        "id": "few_shot",
        "name": "Few-Shot In-Context",
        "description": "Provides 2 curated exemplar problem-solution demonstrations before presenting the test query.",
        "category": "Exemplar-Based",
        "complexity": "O(k) Context Overhead",
    },
    "chain_of_thought": {
        "id": "chain_of_thought",
        "name": "Chain-of-Thought (CoT)",
        "description": "Explicitly instructs the model to generate a sequential intermediate reasoning trace ('Let's think step by step').",
        "category": "Trace Elicitation",
        "complexity": "O(1) Prompt, O(r) Output Tokens",
    },
    "step_back": {
        "id": "step_back",
        "name": "Step-Back Abstraction",
        "description": "Instructs the model to abstract first-principles and underlying domain laws before solving specific constraints.",
        "category": "Abstraction-First",
        "complexity": "Two-Phase Conceptual Mapping",
    },
    "least_to_most": {
        "id": "least_to_most",
        "name": "Least-to-Most Decomposition",
        "description": "Decomposes the multi-hop challenge into ordered sub-questions, solving atomic steps sequentially.",
        "category": "Decomposition / Agentic",
        "complexity": "Hierarchical Problem Reduction",
    }
}


FEW_SHOT_EXEMPLARS = """Example 1:
Problem: A store has 15 red apples and 25 green apples. 40% of the red apples and 20% of the green apples are damaged. How many undamaged apples remain in total?
Reasoning:
1. Total red apples = 15. Damaged red apples = 15 * 0.40 = 6. Undamaged red apples = 15 - 6 = 9.
2. Total green apples = 25. Damaged green apples = 25 * 0.20 = 5. Undamaged green apples = 25 - 5 = 20.
3. Total undamaged apples = 9 + 20 = 29.
Final Answer: 29

Example 2:
Problem: Three switches (A, B, C) control three light bulbs (1, 2, 3) in another room. Switch A is flipped ON for 10 minutes then turned OFF. Switch B is turned ON. You enter the room: Bulb 1 is ON, Bulb 2 is OFF but warm, Bulb 3 is OFF and cold. Which switch controls Bulb 2?
Reasoning:
1. Bulb 1 is currently ON -> Controlled by active switch B.
2. Bulb 2 is OFF but warm -> It was recently turned ON then OFF -> Controlled by switch A.
3. Bulb 3 is OFF and cold -> Never turned ON -> Controlled by switch C.
Final Answer: Switch A
"""


def format_prompt(strategy_id: str, problem_text: str, context_notes: str = "") -> str:
    """
    Wraps the input problem text into the specified prompting strategy template.
    """
    if strategy_id == "zero_shot":
        return (
            f"Solve the following problem directly and provide the exact final answer.\n\n"
            f"Problem:\n{problem_text}\n\n"
            f"Final Answer format: Output 'FINAL ANSWER: <concise answer>'"
        )

    elif strategy_id == "few_shot":
        return (
            f"Here are solved examples demonstrating how to reason and answer complex problems:\n\n"
            f"{FEW_SHOT_EXEMPLARS}\n"
            f"Now solve this new problem:\n"
            f"Problem:\n{problem_text}\n\n"
            f"Show your reasoning and conclude with 'FINAL ANSWER: <concise answer>'."
        )

    elif strategy_id == "chain_of_thought":
        return (
            f"You are an expert reasoning engine. Approach the following problem with rigorous, step-by-step logic.\n\n"
            f"Problem:\n{problem_text}\n\n"
            f"Instructions:\n"
            f"1. Let's think step by step.\n"
            f"2. Explicitly lay out each derivation step, logic deduction, or intermediate calculation.\n"
            f"3. Verify edge cases and consistency.\n"
            f"4. State the final conclusion clearly as 'FINAL ANSWER: <concise answer>'."
        )

    elif strategy_id == "step_back":
        return (
            f"You are a scientific problem solver utilizing Step-Back Abstraction prompting.\n\n"
            f"Problem:\n{problem_text}\n\n"
            f"Step 1 - High-Level Principles & Concepts:\n"
            f"Identify the fundamental concepts, governing mathematical rules, or logical invariants involved in this problem.\n\n"
            f"Step 2 - Execution on Concrete Problem:\n"
            f"Apply the foundational principles derived in Step 1 to solve the specific constraints of the problem.\n\n"
            f"Conclude with 'FINAL ANSWER: <concise answer>'."
        )

    elif strategy_id == "least_to_most":
        return (
            f"You are an agentic reasoning system applying Least-to-Most sub-problem decomposition.\n\n"
            f"Problem:\n{problem_text}\n\n"
            f"Decomposition and Solution Workflow:\n"
            f"1. Sub-Problem Identification: Break down this complex problem into 2-4 ordered, simpler atomic sub-questions.\n"
            f"2. Sequential Sub-Problem Solutions: Solve each sub-question sequentially, building upon previous intermediate results.\n"
            f"3. Final Synthesis: Combine the sub-solutions to resolve the original query.\n\n"
            f"Conclude with 'FINAL ANSWER: <concise answer>'."
        )

    else:
        raise ValueError(f"Unknown prompting strategy: {strategy_id}")
