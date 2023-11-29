from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# SQLite database file path
db_path = 'C:\\Users\\REIS\\.vscode\\V\\DATABASE.db'


# Function to verify the number in the database
def verify_number(id_number):
    try:
        conn = sqlite3.connect(db_path)
        print("Database connected successfully.")
        cursor = conn.cursor()
        query = "SELECT * FROM students WHERE id_number = ?"
        cursor.execute(query, (id_number,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""

    if request.method == 'POST':
        # Use 'id_number' instead of 'number_to_verify'
        id_number = request.form['id_number']

        if verify_number(id_number):
            message = f"ID Number {id_number} is verified."
        else:
            message = f"ID Number {id_number} is not found in the database."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
