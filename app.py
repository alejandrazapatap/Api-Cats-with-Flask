from flask import Flask
from views import views


#register of views
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")



if __name__ == '__main__':
    app.run(debug=False, port=8000)

