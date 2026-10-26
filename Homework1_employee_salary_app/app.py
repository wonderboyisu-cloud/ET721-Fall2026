import os
import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": os.environ.get("DB_USER", "flaskuser"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": "employee_data",
}


@app.route('/', methods =['POST', 'GET'])
def index():
    msg = ''
    if request.method == 'POST':
        name = request.form['name'].strip()

        try:
            emp_id = int(request.form['id'])
            salary = int(request.form['salary'])
        except ValueError:
            return render_template("index_IsaamShah.html", msg='ID and salary must be whole numbers.')

        if not name or len(name) > 50:
            return render_template("index_IsaamShah.html", msg='Name is required (50 characters max).')
        if not 0 <= emp_id <= 99:
            return render_template("index_IsaamShah.html", msg='Employee ID must be 0-99.')
        if not 0 <= salary <= 999999:
            return render_template("index_IsaamShah.html", msg='Salary must be 0-999999.')

        conn = mysql.connector.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("INSERT INTO employee_salary (employee_name, employee_id, salary) " "VALUES (%s, %s, %s)", (name, emp_id, salary),)
        conn.commit()
        cur.close()
        conn.close()

        new_salary = salary * 1.05
        msg = (
            "Employee Salary Increase\n"
            f"Employee Name: {name}\n"
            f"Employee ID: {emp_id}\n"
            f"Employee Salary: {salary}\n"
            f"The increase salary is $ {new_salary:.2f}"
        )
    return render_template('index_IsaamShah.html', msg = msg)

if __name__ == '__main__':
    app.run(debug=True)



