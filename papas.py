from flask import Flask, render_template, request
import requests
import json
import math
import re

flask_app = Flask(__name__)

@flask_app.route("/")
def hello():
    return render_template("hello.html")

@flask_app.route("/currency", methods=["POST"])
def get_pounds():
    form_data = request.form["num"]
    if re.search('[a-zA-Z]', form_data) != None:
        return " Oops! Just numbers please"
    else:
        result = calculate_amt_euros(form_data)
        return render_template("pagetwo.html", result=result)

def get_exchange_rate():
    endpoint = "https://openexchangerates.org/api/latest.json?app_id=8567d4e0f026487db09bafbfbfda2069&base=GBP"
    response = requests.get(endpoint)
    eurorate = json.loads(response.text)['rates']['EUR']
    return json.dumps(eurorate)


def calculate_amt_euros(pounds):
        eurorate = get_exchange_rate()
        return str(float(pounds) * float(eurorate))


if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)
