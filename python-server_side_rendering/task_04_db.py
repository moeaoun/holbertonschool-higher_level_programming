from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# ---------- JSON Source ----------
def load_json_data():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        return f"Error loading JSON data: {e}"

# ---------- CSV Source ----------
def load_csv_data():
    try:
        products = []
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception as e:
        return f"Error loading CSV data: {e}"

# ---------- SQL Source ----------
def load_sql_data():
    if not os.path.exists('products.db'):
        return "Database file not found."

    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        return products
    except Exception as e:
        return f"Database error: {e}"

# ---------- Flask Route ----------
@app.route('/')
def display_products():
    source = request.args.get('source', 'json')
    filter_id = request.args.get('id')
    error = None
    products = []

    # Load data based on source
    if source == 'json':
        result = load_json_data()
    elif source == 'csv':
        result = load_csv_data()
    elif source == 'sql':
        result = load_sql_data()
    else:
        error = "Wrong source"
        result = []

    # Handle errors in data loading
    if isinstance(result, str):
        error = result
    else:
        products = result

    # Optional: Filter by ID
    if filter_id and products:
        try:
            filter_id = int(filter_id)
            products = [p for p in products if p['id'] == filter_id]
            if not products:
                error = f"No product found with id {filter_id}"
        except ValueError:
            error = "Invalid ID format"
            products = []

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)

