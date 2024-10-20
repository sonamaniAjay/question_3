from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="user_registration"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    user_id = request.form['userId']
    mobile = request.form['mobile']
    password = request.form['password']
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (user_id, mobile, password) VALUES (%s, %s, %s)", (user_id, mobile, password))
    db.commit()
    return 'Registration Successful!'

if __name__ == '__main__':
    app.run(debug=True)
