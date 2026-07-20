#!/usr/bin/python3
"""One-time script to create and populate products.db."""
import sqlite3


def create_database():
    """Create the Products table in products.db and seed it with data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99),
            (3, 'Python Book', 'Books', 29.99),
            (4, 'Desk Lamp', 'Home Goods', 24.99)
        ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
