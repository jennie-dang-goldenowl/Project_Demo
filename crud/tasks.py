from locale import currency
from celery import shared_task
from Project_Demo.celery import app
import requests

# @shared_task
@app.task(name='update_rates')
def print_error():
    print('Hello ABC')

@shared_task
def update_rates():
    print('Start update_rates')
    currency_url = "https://api.currencyapi.com/v3/latest?apikey=97b1d820-9d1c-11ec-84a0-d7360886eef6"

    response = requests.get(currency_url)
    data = response.json()
    print(data['data']['VND']['value'])
    # currency_rates = data['data']['VND']['value']
    # print(currency_rates)
