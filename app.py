import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash, session
import pickle
import numpy as np
import os

# Initialize Flask
app = Flask(__name__)
app.secret_key = 'your_secret_key'  

# Load pre-trained model
modelfile = r"C:\Users\kanir\OneDrive\Desktop\wholesale_customer_segmentation_ML\NOTEBOOK\model_pickle"
model = pickle.load(open(modelfile, 'rb'))

# Database connection function for MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="root",  
        database="chitti"  
    )
    return conn

# Function to create the users table in MySQL if it doesn't exist
def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Mock database of users (if you still want to use it alongside the MySQL database)
users = {'admin': 'password'}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/value')
def value():
    return render_template('value.html')

# Registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Insert user into the MySQL database
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO data (username, password) VALUES (%s, %s)', (username, password))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError:
            flash('Username already exists. Please choose another one.', 'danger')
        finally:
            cursor.close()
            conn.close()

    return render_template('register.html')

# Login page with session management
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check the user in MySQL database
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM data WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        # Check either MySQL database or mock user dictionary
        if user or users.get(username) == password:
            session['logged_in'] = True
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('predict'))
        else:
            flash('Invalid credentials. Please enter correct username and password.', 'danger')

    return render_template('login.html')

# Prediction page, accessible only after login
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'logged_in' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login'))

    if request.method == 'POST':
        Channel = request.form.get("Channel")
        Region = request.form.get('Region')
        Fresh = request.form.get('Fresh')
        Milk = request.form.get('Milk')
        Grocery = request.form.get('Grocery')
        Frozen = request.form.get('Frozen')
        Detergents_Paper = request.form.get('Detergent_paper')
        Delicassen = request.form.get('Delicassen')

        if not all([Grocery, Frozen, Detergents_Paper, Delicassen]):
            result = "Please fill out all form fields with valid numbers."
        else:
            try:
                total = [float(Grocery), float(Frozen), float(Detergents_Paper), float(Delicassen)]
                total = np.array(total).reshape(1, -1)

                prediction = model.predict(total)

                if prediction == 0:
                    result = "Customer Belongs to Cluster Label 0"
                elif prediction == 1:
                    result = "Customer Belongs to Cluster Label 1"
                elif prediction == 2:
                    result = "Customer Belongs to Cluster Label 2"
                else:
                    result = "Customer Belongs to Cluster Label 3"
            except ValueError:
                result = "Please enter valid numerical values."

        return render_template('predict.html', predict=result)

    return render_template('predict.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Clear session data
    flash('You have been logged out.', 'info')
    return render_template('logout.html')

if __name__ == '__main__':
    create_users_table()
    app.run(debug=True)
