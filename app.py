
import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, g, session

app = Flask(__name__)

# Секретний ключ використовується для захисту сесій Flask
app.secret_key = 'super-secret-key-for-pet-project'
app.config['DATABASE'] = 'app.db'

# Функція для підключення до бази даних SQLite
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

# Функція для закриття з'єднання з базою даних
@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql', mode='r', encoding='utf-8') as f:
            db.cursor().executescript(f.read())
        db.commit()


init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')

