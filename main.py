import requests
from flask import Flask, render_template, jsonify, request

DATA_URL = "http://api.exchangeratesapi.io/v1/"
API_KEY = ""
BASE_CURRENCY = "EUR"
COMPLETE_URL = DATA_URL + "latest?access_key=" + API_KEY

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    r = requests.get(COMPLETE_URL + "&base=" + BASE_CURRENCY)
    r_data = r.json()
    rates = r_data["rates"]
    return render_template('home_page.html', rates=rates)


@app.route('/convert', methods=['GET'])
def convert():
    fromCurrency = request.args.get('fromCurrency')
    toCurrency = request.args.get('toCurrency')
    amount = request.args.get('amount')
    # build url
    url = COMPLETE_URL + "&base=" + fromCurrency + "&symbols=" + toCurrency
    r = requests.get(url)
    r_data = r.json()
    print(r_data)
    rate = r_data["rates"][toCurrency]
    data = {
        "from_currency": fromCurrency,
        "to_currency": toCurrency,
        "amount": amount,
        "result": rate * float(amount)
    }
    return jsonify(data)
