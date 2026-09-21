"""
SQL Agent Benchmark Test Suite.
Curated natural language queries testing relational joins, aggregations, schema reasoning, and self-healing.
"""

from typing import List, Dict, Any

SQL_BENCHMARK_TASKS: List[Dict[str, Any]] = [
    {
        "id": "SQL_TASK_01_TOP_SPENDERS",
        "title": "Top Spending Customers Aggregation",
        "category": "Multi-Table Aggregation & JOIN",
        "difficulty": "Medium-Hard",
        "question": "Find the top 3 highest spending customers with their customer name, total amount spent, and number of orders placed.",
        "canonical_sql": """
            SELECT c.name, SUM(p.amount) AS total_spent, COUNT(DISTINCT o.order_id) AS order_count
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN payments p ON o.order_id = p.order_id
            GROUP BY c.customer_id, c.name
            ORDER BY total_spent DESC
            LIMIT 3;
        """,
        "expected_answer": "Alice Smith ($684.00, 2 orders), Charlie Brown ($530.00, 2 orders), Diana Prince ($450.00, 1 order)",
        "acceptable_keywords": ["Alice Smith", "684", "Charlie Brown", "530", "Diana Prince", "450"]
    },
    {
        "id": "SQL_TASK_02_CATEGORY_REVENUE",
        "title": "Category Revenue & High-Performance Products",
        "category": "Multi-Hop Filtering & Grouping",
        "difficulty": "Hard",
        "question": "List all products in the 'Electronics' category that have generated over $200 in total sales revenue. Include the product name, unit price, total quantity sold, and gross revenue.",
        "canonical_sql": """
            SELECT p.product_name, p.price, SUM(oi.quantity) AS total_qty, SUM(oi.quantity * oi.unit_price) AS gross_revenue
            FROM products p
            JOIN order_items oi ON p.product_id = oi.product_id
            WHERE p.category = 'Electronics'
            GROUP BY p.product_id, p.product_name, p.price
            HAVING gross_revenue > 200
            ORDER BY gross_revenue DESC;
        """,
        "expected_answer": "Headphones ($750 revenue, 5 sold), Smart Fitness Watch ($360 revenue, 2 sold), Gaming Keyboard ($255 revenue, 3 sold)",
        "acceptable_keywords": ["Headphones", "750", "Smart Fitness Watch", "360", "Keyboard", "255"]
    },
    {
        "id": "SQL_TASK_03_PAYMENT_BREAKDOWN",
        "title": "Payment Method Volume & Success Tracking",
        "category": "Financial Analytics & Status Join",
        "difficulty": "Medium",
        "question": "Which payment method has processed the largest total amount of money for 'Completed' orders, and what is that total volume?",
        "canonical_sql": """
            SELECT p.payment_method, SUM(p.amount) AS total_processed
            FROM payments p
            JOIN orders o ON p.order_id = o.order_id
            WHERE o.status = 'Completed'
            GROUP BY p.payment_method
            ORDER BY total_processed DESC
            LIMIT 1;
        """,
        "expected_answer": "Credit Card ($1134.00 total volume)",
        "acceptable_keywords": ["Credit Card", "1134", "1,134"]
    },
    {
        "id": "SQL_TASK_04_SELF_HEALING_SCHEMA",
        "title": "Schema Introspection & Error Recovery",
        "category": "ReAct Self-Healing & Foreign Keys",
        "difficulty": "Complex (Requires Introspection & Auto-Recovery)",
        "question": "Find the cities where customers who bought 'Furniture' items live, along with the names of the furniture items they ordered.",
        "canonical_sql": """
            SELECT DISTINCT c.city, c.name, p.product_name
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            JOIN products p ON oi.product_id = p.product_id
            WHERE p.category = 'Furniture'
            ORDER BY c.city;
        """,
        "expected_answer": "London (Bob Johnson - Ergonomic Office Chair), New York (Alice Smith - Standing Desk Converter)",
        "acceptable_keywords": ["London", "Bob", "Chair", "New York", "Alice", "Desk"]
    }
]


def get_all_sql_tasks() -> List[Dict[str, Any]]:
    return SQL_BENCHMARK_TASKS
