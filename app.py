from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)


def connection_db():
    config = {
        'user': 'root',
        'password': 'corhadsho',
        'host': '127.0.0.1',
        'database': 'movieSetting',
        'raise_on_warnings': True,
        'port': '3456'
    }

    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print("Error: ", err)
    else:
        print("well done")
        return cnx
        # cnx.close()

try:
    connection = connection_db()
except mysql.connector.Error as e:
    print(f"Error: {e}")


@app.route('/')
def index():
    return render_template('index.html')


################### register #######################
@app.route('/register', methods=['GET'])
def register_button():
    return render_template('register.html')


def register_query(username, password):
    if connection.is_connected():
        cursor = connection.cursor()

        # Check if the username is already taken
        check_query = f"SELECT * FROM user WHERE name = '{username}'"
        cursor.execute(check_query)
        if cursor.fetchone():
            # Username already exists, handle accordingly (e.g., display an error message)
            return "Username already exists"

        # If the username is not taken, proceed with user registration
        insert_query = f"INSERT INTO user (name, password) VALUES ('{username}', SHA2('{password}', 256))"
        cursor.execute(insert_query)
        connection.commit()

        return "User registered successfully"



@app.route('/register', methods=['POST'])
def register_route():
    if request.method == 'POST':
        username = request.form['fname']
        password = request.form['passw']
        valid_password = request.form['validpassw']

        if password == valid_password:
            # Passwords match, proceed with user registration
            result = register_query(username, password)
            return result
        else:
            # Passwords do not match, handle accordingly (e.g., display an error message)
            return "Passwords do not match"
    else:
        return redirect(url_for('index'))


################### login #######################
@app.route('/login', methods=['GET'])
def register_button():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_route():
    if request.method == 'POST':
        username = request.form['fname']
        password = request.form['passw']

        login_query(username, password)
    else:
        return redirect(url_for('index'))


def login_query(username, password):


def login(username, password):
    pass


def logout():
    pass


def user_reservations(user):
    pass


def choose_movie_from_list():
    pass


def screening_time(movie):
    pass


def seats_available():
    pass


def payment():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    connection.close()
