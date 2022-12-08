from flask import Flask, render_template
from views import views
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import jsonify



#register of views
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/sitio.db'

#cursor to query to db
db = SQLAlchemy(app)

project = []

@app.route("/query")
def query():
    con=sqlite3.connect("database/sitio.db")
    #con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT project_name FROM project")
    data=cur.fetchall()
    con.close()
    for i in data:
        for x in i:
            project.append(x)
    return project
    
@app.route("/join")
def join():
    con=sqlite3.connect("database/sitio.db")
    #con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT user.username, name FROM user_role_association_table JOIN user ON user.id=user_id JOIN role ON role.id=role_id")
    data=cur.fetchall()
    con.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

