from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)")

@app.route('/')
def index():
    with sqlite3.connect("database.db") as conn:
        contacts = conn.execute("SELECT * FROM contacts").fetchall()
    return render_template("index.html", contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name, phone, email = request.form['name'], request.form['phone'], request.form['email']
    with sqlite3.connect("database.db") as conn:
        conn.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_contact(id):
    with sqlite3.connect("database.db") as conn:
        conn.execute("DELETE FROM contacts WHERE id=?", (id,))
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
