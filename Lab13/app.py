from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

import mysql.connector

app = Flask(__name__)

# database connection
def get_db_connection():
    return mysql.connector.connect(
        host = "127.0.0.1",
        user = 'flaskuser',
        password = 'password123',
        database = "blogDB"
    )


@app.route('/')
def index():
    return render_template('index.html')

# Display blogs
@app.route('/blogs')
def blogs():
    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT blog.id, users.username, blog.title, blog.content, blog.created_at FROM blog JOIN users ON blog.user_id = users.userid")

    # get all the data and store them in 'data'
    data = cursor.fetchall()
    
    return render_template('blogs.html', blogs = data)

@app.route('/add_blog', methods =['GET', 'POST'])
def add_blog():
    username = request.form['username']
    email = request.form['email']
    title = request.form['title']
    content = request.form['content']

    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        try:
            # insert into table users
            cursor.execute("INSERT INTO users(username, email) VALUES(%s, %s)", (username,email))
            
            connection.commit()

            # store the id of the last row that was inserted into the database
            user_id = cursor.lastrowid

            # insert data into table blog
            cursor.execute("INSERT INTO blog(user_id, title, content) VALUES(%s, %s, %s)", (user_id, title, content))
            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()


    return redirect(url_for('blogs'))

if __name__ == '__main__':
    app.run(debug=True)














