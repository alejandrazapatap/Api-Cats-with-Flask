import requests
from flask import Blueprint
from flask import render_template


views = Blueprint(__name__,"views")

url = "https://catfact.ninja/facts"


@views.route("/")
def gatos():
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            #print(data)
            #data = str(json.loads(data))
            return render_template('index.html', data=data) 


