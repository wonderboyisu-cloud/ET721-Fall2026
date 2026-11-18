from flask import Flask, render_template, request, jsonify

import mysql.connector

app = Flask(__name__)

# ------------------
# Databse configuration
# ------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'todo_db'

# Databse connection
db = mysql.connector.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password = app.config['MYSQL_PASSWORD'],
    database = app.config['MYSQL_DB']

)

# ------------------
# homepage route
# ------------------

@app.route('/')
def index():
    return render_template("index.html")

# ------------------
# get all tasks
# ------------------

@app.route('/get_tasks', methods = ['GET'])
def get_task():
    try: 
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
        return jsonify(tasks)

    except mysql.connector.Error as e:
        return jsonify({"ERROR...": str(e)}), 500

# ------------------
# Add new task
# ------------------

@app.route("/add_task", methods = ['POST'])
def add_task():
    data = request.get_json()
    task = data.get("task")

    if task:
        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks(task) VALUES(%s)", (task))
        db.commit()
        cursor.close()
        return jsonify({"status": "Success"})

    return jsonify({"status": "Error with task"}) 

# ------------------
# Delete task
# ------------------
@app.route("/delete_task", methods = ['POST'])
def delete_task():
    data = request.get_json()
    task = data.get("task")

    if task:
        cursor  = db,cursor()
        cursor.execute("DELETE FROM tasks WHERE task = %s", (task))
        db.commit()
        cursor.close()
        return jsonify({"status": "Success"})
    return jsonify ({"status": "Error with task"})

# ------------------
# autorun 
# ------------------
if __name__ == "__main__":
    app.run(debug=True)