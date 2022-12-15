from flask import Flask, render_template
from views import views
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import json

# register of views
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/sitio.db'

# cursor to query to db
db = SQLAlchemy(app)

app.register_blueprint(views, url_prefix="/views")


@app.route("/proyect_user")
def proyect_user():
    con = sqlite3.connect("database/sitio.db")
    cur = con.cursor()
    cur.execute(
        "SELECT project_name FROM project WHERE project_name LIKE '%id%'")
    data_projects = cur.fetchall()
    proyectos = list(data_projects)
    cur.execute("SELECT name,description,username,user_full_name FROM user JOIN user_role_association_table ON user.id=user_role_association_table.user_id JOIN role ON user_role_association_table.role_id=role.id")
    data_users = cur.fetchall()
    usuarios = list(data_users)
    con.close()
    my_object = {
        "projects": proyectos,
        "users": usuarios
    }
    json_str = json.dumps(my_object)
    return json_str


if __name__ == '__main__':
    app.run(debug=True, port=8000)
