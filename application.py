from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="project5-db.ce9icakoyv6h.us-east-1.rds.amazonaws.com",
        user="admin",
        password="Ashu5064",
        database="project5db"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users;")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    return render_template('add_user.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
