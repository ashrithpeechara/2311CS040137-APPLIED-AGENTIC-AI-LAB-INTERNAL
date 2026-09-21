"""
Reasoning Benchmark Test Suite.
Curated dataset containing multi-step reasoning, symbolic logic, algorithmic, and counterfactual tasks.
"""

from typing import List, Dict, Any

BENCHMARK_TASKS: List[Dict[str, Any]] = [
    {
        "id": "TASK_01_MATH_COMBINATORICS",
        "title": "Combinatorial Probability & Urn Distribution",
        "category": "Mathematical Reasoning",
        "difficulty": "Hard",
        "problem": (
            "An urn contains 4 red balls, 5 blue balls, and 6 green balls (total 15). "
            "Three balls are drawn simultaneously at random without replacement. "
            "What is the exact probability that all three balls drawn are of completely distinct colors "
            "(i.e., exactly one red, one blue, and one green)? "
            "Express your answer as a simplified fraction a/b."
        ),
        "expected_answer": "24/91",
        "acceptable_keywords": ["24/91", "24 / 91", "0.2637"],
        "ground_truth_reasoning": (
            "Total ways to choose 3 balls from 15 is C(15,3) = (15*14*13)/(3*2*1) = 455. "
            "Ways to choose 1 red, 1 blue, 1 green = C(4,1)*C(5,1)*C(6,1) = 4 * 5 * 6 = 120. "
            "Probability = 120 / 455. Dividing numerator and denominator by 5 gives 24 / 91."
        )
    },
    {
        "id": "TASK_02_SYMBOLIC_LOGIC",
        "title": "Knights, Knaves, and Spies Deductive Logic",
        "category": "Symbolic & Deductive Logic",
        "difficulty": "Hard",
        "problem": (
            "On an island, inhabitants are either Knights (always tell the truth) or Knaves (always lie). "
            "You meet three inhabitants: Alex, Blake, and Casey. Exactly one is a Knight and two are Knaves.\n"
            "Alex says: 'Casey is a Knave.'\n"
            "Blake says: 'Alex and I are of the same type.'\n"
            "Casey says: 'Blake is a Knight.'\n"
            "Who among the three is the single Knight?"
        ),
        "expected_answer": "Alex",
        "acceptable_keywords": ["Alex", "alex is the knight", "alex is knight"],
        "ground_truth_reasoning": (
            "Constraint: Exactly 1 Knight (T), 2 Knaves (F).\n"
            "Case 1: If Alex is the Knight (T):\n"
            "- Alex's statement ('Casey is a Knave') is True -> Casey is a Knave (F).\n"
            "- Blake must be a Knave (F). Blake's statement ('Alex and I are same type') is False (since Alex=T, Blake=F), which matches Blake being a Knave.\n"
            "- Casey's statement ('Blake is a Knight') is False (since Blake=F), which matches Casey being a Knave.\n"
            "This case is fully consistent. Therefore, Alex is the Knight."
        )
    },
    {
        "id": "TASK_03_ALGORITHMIC_PLANNING",
        "title": "Agent Task Scheduling & Constrained Path Cost",
        "category": "Algorithmic Planning",
        "difficulty": "Medium-Hard",
        "problem": (
            "An autonomous agent must execute 4 tasks (T1, T2, T3, T4) in a single-threaded queue. "
            "The execution times are: T1 = 3 hrs, T2 = 5 hrs, T3 = 2 hrs, T4 = 4 hrs. "
            "Precedence constraint: T1 must complete before T3 can start (T1 -> T3). "
            "Completion time C_i is the time elapsed from start (t=0) until task T_i finishes. "
            "Find the optimal valid execution order that minimizes the total sum of completion times (Sum of C_i), "
            "and compute that minimum sum in hours."
        ),
        "expected_answer": "31",
        "acceptable_keywords": ["31", "31 hours", "31h", "T1 -> T3 -> T4 -> T2"],
        "ground_truth_reasoning": (
            "Under Shortest Processing Time (SPT) rule respecting precedence constraint T1 -> T3:\n"
            "Evaluating valid task permutations:\n"
            "1. T1 -> T3 -> T4 -> T2: C1=3, C3=5, C4=9, C2=14. Sum = 3 + 5 + 9 + 14 = 31.\n"
            "2. T1 -> T3 -> T2 -> T4: C1=3, C3=5, C2=10, C4=14. Sum = 32.\n"
            "3. T1 -> T4 -> T3 -> T2: C1=3, C4=7, C3=9, C2=14. Sum = 33.\n"
            "4. T4 -> T1 -> T3 -> T2: C4=4, C1=7, C3=9, C2=14. Sum = 34.\n"
            "Optimal valid order is T1 -> T3 -> T4 -> T2 with minimum total sum of completion times = 31 hours."
        )
    },
    {
        "id": "TASK_04_COUNTERFACTUAL_REASONING",
        "title": "Recursive State Reversal & Invariant Tracking",
        "category": "Multi-Step Symbolic Invariance",
        "difficulty": "Hard",
        "problem": (
            "A robot starts at origin (0, 0) facing North (0 deg). It follows a 4-step sequence S: "
            "[Step 1: Move forward 3 units; Step 2: Turn 90 deg clockwise; Step 3: Move forward 4 units; Step 4: Turn 90 deg counter-clockwise]. "
            "The robot executes sequence S exactly 4 times successively. "
            "What is the robot's final Euclidean distance from the initial starting point (0, 0)?"
        ),
        "expected_answer": "20",
        "acceptable_keywords": ["20", "20 units", "sqrt(400)"],
        "ground_truth_reasoning": (
            "Let's trace one execution of sequence S:\n"
            "1. Face North, move forward 3: delta = (0, +3), facing North.\n"
            "2. Turn 90 deg clockwise: facing East.\n"
            "3. Move forward 4: delta = (+4, 0), facing East.\n"
            "4. Turn 90 deg counter-clockwise: facing North.\n"
            "Net displacement after 1 cycle of S: dx = +4, dy = +3. Net orientation change: 0 degrees (still facing North).\n"
            "Since orientation remains North at the end of each cycle, each subsequent execution of S adds the exact same vector (+4, +3).\n"
            "After 4 cycles: Total X = 4 * 4 = 16. Total Y = 4 * 3 = 12.\n"
            "Euclidean Distance = sqrt(16^2 + 12^2) = sqrt(256 + 144) = sqrt(400) = 20."
        )
    }
]


def get_all_tasks() -> List[Dict[str, Any]]:
    return BENCHMARK_TASKS
