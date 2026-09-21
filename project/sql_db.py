"""
SQLite Database Setup and Population for SQL Agent Benchmarking.
E-commerce Enterprise Schema: Customers, Products, Orders, OrderItems, Payments.
"""

import sqlite3
from pathlib import Path
from project.config import OUTPUT_DIR

DB_PATH = OUTPUT_DIR / "ecommerce.db"


def init_ecommerce_db(db_file: Path = DB_PATH) -> sqlite3.Connection:
    """Initializes and seeds the SQLite relational database."""
    db_file.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_file))
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Customers Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        city TEXT NOT NULL,
        country TEXT NOT NULL,
        signup_date TEXT NOT NULL
    );
    """)

    # 2. Products Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        stock_quantity INTEGER NOT NULL
    );
    """)

    # 3. Orders Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('Completed', 'Pending', 'Cancelled', 'Shipped')),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
    """)

    # 4. Order Items Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        unit_price REAL NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    );
    """)

    # 5. Payments Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        payment_method TEXT NOT NULL CHECK(payment_method IN ('Credit Card', 'UPI', 'PayPal', 'Net Banking')),
        amount REAL NOT NULL,
        payment_date TEXT NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
    );
    """)

    # Clear existing data for fresh reproducible runs
    cursor.execute("DELETE FROM payments;")
    cursor.execute("DELETE FROM order_items;")
    cursor.execute("DELETE FROM orders;")
    cursor.execute("DELETE FROM products;")
    cursor.execute("DELETE FROM customers;")

    # Seed Customers
    customers_data = [
        (1, 'Alice Smith', 'alice@example.com', 'New York', 'USA', '2025-01-15'),
        (2, 'Bob Johnson', 'bob@example.com', 'London', 'UK', '2025-02-10'),
        (3, 'Charlie Brown', 'charlie@example.com', 'Bengaluru', 'India', '2025-02-20'),
        (4, 'Diana Prince', 'diana@example.com', 'Toronto', 'Canada', '2025-03-05'),
        (5, 'Evan Wright', 'evan@example.com', 'Sydney', 'Australia', '2025-03-12'),
    ]
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?);", customers_data)

    # Seed Products
    products_data = [
        (1, 'Wireless Noise-Cancelling Headphones', 'Electronics', 150.00, 45),
        (2, 'Mechanical Gaming Keyboard', 'Electronics', 85.00, 60),
        (3, 'Ergonomic Office Chair', 'Furniture', 220.00, 20),
        (4, 'Smart Fitness Watch', 'Electronics', 180.00, 35),
        (5, 'Standing Desk Converter', 'Furniture', 299.00, 15),
        (6, 'Organic Coffee Beans 1kg', 'Groceries', 25.00, 100),
    ]
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?);", products_data)

    # Seed Orders
    orders_data = [
        (101, 1, '2026-08-10', 'Completed'),
        (102, 2, '2026-08-12', 'Completed'),
        (103, 3, '2026-08-15', 'Completed'),
        (104, 1, '2026-08-28', 'Completed'),
        (105, 4, '2026-09-02', 'Completed'),
        (106, 5, '2026-09-10', 'Shipped'),
        (107, 3, '2026-09-18', 'Completed'),
    ]
    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?);", orders_data)

    # Seed Order Items
    order_items_data = [
        (1, 101, 1, 2, 150.00),  # Alice: 2x Headphones = 300
        (2, 101, 2, 1, 85.00),   # Alice: 1x Keyboard = 85 (Order 101 = $385)
        (3, 102, 3, 1, 220.00),  # Bob: 1x Chair = 220
        (4, 103, 4, 2, 180.00),  # Charlie: 2x Watch = 360
        (5, 104, 5, 1, 299.00),  # Alice: 1x Desk = 299 (Alice Total = $684)
        (6, 105, 1, 3, 150.00),  # Diana: 3x Headphones = 450
        (7, 106, 6, 4, 25.00),   # Evan: 4x Coffee = 100
        (8, 107, 2, 2, 85.00),   # Charlie: 2x Keyboard = 170 (Charlie Total = $530)
    ]
    cursor.executemany("INSERT INTO order_items VALUES (?, ?, ?, ?, ?);", order_items_data)

    # Seed Payments
    payments_data = [
        (1, 101, 'Credit Card', 385.00, '2026-08-10'),
        (2, 102, 'PayPal', 220.00, '2026-08-12'),
        (3, 103, 'UPI', 360.00, '2026-08-15'),
        (4, 104, 'Credit Card', 299.00, '2026-08-28'),
        (5, 105, 'Credit Card', 450.00, '2026-09-02'),
        (6, 106, 'Net Banking', 100.00, '2026-09-10'),
        (7, 107, 'UPI', 170.00, '2026-09-18'),
    ]
    cursor.executemany("INSERT INTO payments VALUES (?, ?, ?, ?, ?);", payments_data)

    conn.commit()
    return conn


if __name__ == "__main__":
    c = init_ecommerce_db()
    print("Database initialized successfully at:", DB_PATH)
