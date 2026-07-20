#!/usr/bin/python3
"""Flask application that displays product data from JSON, CSV, or SQL."""
import csv
import json
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(file_path='products.json'):
    """Read and return the list of products from a JSON file."""
    with open(file_path) as f:
        return json.load(f)


def read_csv(file_path='products.csv'):
    """Read and return the list of products from a CSV file."""
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


def read_sql(file_path='products.db'):
    """Read and return the list of products from the SQLite database."""
    conn = sqlite3.connect(file_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read items.json and render the items list page."""
    with open('items.json') as f:
        data = json.load(f)

    return render_template('items.html', items=data.get('items', []))


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL, optionally filtered by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        try:
            data = read_sql()
        except sqlite3.Error:
            return render_template(
                'product_display.html', error='Error fetching data from SQL'
            )
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error='Product not found'
            )

        data = [p for p in data if p['id'] == product_id]

        if not data:
            return render_template(
                'product_display.html', error='Product not found'
            )

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
