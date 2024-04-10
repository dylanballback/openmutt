from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_motor_data():
    # Connect to your SQLite database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    # Select data from the motors table
    cursor.execute("SELECT * FROM motors")
    motor_data = cursor.fetchall()
    # Don't forget to close the connection
    conn.close()
    return motor_data

@app.route('/')
def home():
    motor_data = get_motor_data()
    return render_template('index.html', motor_data=motor_data)

if __name__ == '__main__':
    app.run(debug=True)
