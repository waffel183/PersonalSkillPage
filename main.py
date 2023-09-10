from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def add_new_skill(skill_name, skill_desc, skill_level):
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    cur.execute("INSERT INTO skills (skill_name, skill_desc, skill_level) VALUES (?,?,?)",
                (skill_name, skill_desc, skill_level)
                )
    connection.commit()
    connection.close()

def improve_skill(skill_name):
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    # Add 1 to the skill_level of the skill_name row

    connection.commit()
    connection.close()

def decrease_skill(skill_name):
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    # remove 1 to the skill_level of the skill_name row

    connection.commit()
    connection.close()

# For testing:
#add_new_skill('hacking', 'skill about hacking', '10')

@app.route("/new_skill/", methods=('GET', 'POST'))
def new_skill():
    if request.method == 'POST':
        skill_name = request.form['skill_name']
        skill_desc = request.form['skill_desc']
        skill_level = request.form['skill_level']

        if not skill_name:
            return
        elif not skill_desc:
            return
        elif not skill_level:
            return
        else:
            # TODO: Check if skill_name already exists, fail if it does
            add_new_skill(skill_name, skill_desc, skill_level)
            return redirect(url_for('skills'))

    return render_template('new_skill.html')

@app.route("/")
def skills():
    conn = get_db_connection()
    skills = conn.execute('SELECT * FROM skills').fetchall()
    conn.close()
    return render_template('skills.html', skills=skills)



if __name__ == "__main__":
    app.run()