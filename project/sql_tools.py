"""
Database Tool Suite for ReAct SQL Agent.
Provides introspection, schema querying, validation, and safe query execution.
"""

import sqlite3
import re
from typing import Dict, Any, List
from project.sql_db import init_ecommerce_db, DB_PATH


class SQLToolSuite:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.conn = init_ecommerce_db(self.db_path)

    def list_tables(self) -> str:
        """Returns a comma-separated list of all tables present in the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = [row[0] for row in cursor.fetchall()]
        return f"Database Tables: {', '.join(tables)}"

    def get_schema(self, table_name: str) -> str:
        """Retrieves table DDL schema, column definitions, foreign keys, and 2 sample rows."""
        cursor = self.conn.cursor()
        clean_table = table_name.strip().strip("'\"`")
        
        # Check table existence
        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name=?;", (clean_table,))
        res = cursor.fetchone()
        if not res:
            return f"Error: Table '{clean_table}' does not exist. Use list_tables to view available tables."

        create_sql = res[0]

        # Get sample rows
        cursor.execute(f"SELECT * FROM {clean_table} LIMIT 2;")
        col_names = [desc[0] for desc in cursor.description]
        sample_rows = cursor.fetchall()

        formatted_samples = "\n".join([f"  Row: {dict(zip(col_names, r))}" for r in sample_rows])

        return (
            f"Schema for Table '{clean_table}':\n"
            f"{create_sql}\n\n"
            f"Sample Data:\n{formatted_samples}"
        )

    def validate_sql(self, query: str) -> str:
        """Validates SQL query syntax using SQLite EXPLAIN without mutating data."""
        clean_query = query.strip().rstrip(";")
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"EXPLAIN QUERY PLAN {clean_query};")
            return "SUCCESS: Query syntax and table/column references are valid."
        except sqlite3.Error as e:
            return f"SYNTAX ERROR: {str(e)}"

    def execute_sql(self, query: str) -> str:
        """Safely executes SELECT queries and returns tabular records."""
        clean_query = query.strip().rstrip(";")

        # Safety Guard: Disallow mutating queries
        disallowed = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE", "REPLACE"]
        first_word = clean_query.split()[0].upper() if clean_query else ""
        if first_word in disallowed or any(re.search(rf"\b{word}\b", clean_query, re.IGNORECASE) for word in disallowed):
            return "SECURITY ERROR: Only read-only SELECT queries are permitted."

        cursor = self.conn.cursor()
        try:
            cursor.execute(clean_query)
            col_names = [desc[0] for desc in cursor.description] if cursor.description else []
            rows = cursor.fetchall()

            if not rows:
                return "Query executed successfully. Result: 0 rows returned."

            # Format tabular output
            header = " | ".join(col_names)
            separator = "-" * len(header)
            row_lines = [" | ".join(str(val) for val in r) for r in rows]
            return f"Query Result ({len(rows)} rows):\n{header}\n{separator}\n" + "\n".join(row_lines)

        except sqlite3.Error as err:
            return f"EXECUTION ERROR: {str(err)}"


# Global singleton
sql_tools = SQLToolSuite()
