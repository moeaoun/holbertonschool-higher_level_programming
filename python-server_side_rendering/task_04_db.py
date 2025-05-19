from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Helper: Load from JSON
def load_json_data():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception as e:
        return []

# Helper: Load from CSV
def load_csv_data():
    products = []
    try:
        with open("products.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except Exception as e:
        return []

# Helper: Load from SQLite
def load_sql_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        products = [
            {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
            for row in rows
        ]
        conn.close()
        return products
    except sqlite3.Error as e:
        return f"Database error: {e}"

@app.route('/')
def display_products():
    source = request.args.get('source', 'json')
    error = None

    if source == 'json':
        products = load_json_data()
    elif source == 'csv':
        products = load_csv_data()
    elif source == 'sql':
        result = load_sql_data()
        if isinstance(result, str):  # error message
            return render_template('product_display.html', error=result)
        products = result
    else:
        error = "Wrong source"
        products = []

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)

