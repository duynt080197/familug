from flask import Flask
from flask import render_template
import sqlite3
app = Flask(__name__)
conn = sqlite3.connect('familug.db')
conn.commit()
python = conn.execute("SELECT * FROM Python;").fetchall()
command = conn.execute("SELECT * FROM Command;").fetchall()
sysadmin = conn.execute("SELECT * FROM sysadmin;").fetchall()
latest = conn.execute("SELECT * FROM latest;").fetchall()

@app.route("/")
def web():
    return render_template('index.html',python = python,
    command = command, sysadmin = sysadmin, latest = latest)


if __name__ == "__main__":
    app.run(debug=True)