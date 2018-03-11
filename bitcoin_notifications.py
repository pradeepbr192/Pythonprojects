import requests
import time
from datetime import datetime

bitcoin_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/mfrV2_Gx1O5iFlHvYbyvdKa39zrp8avC40xKXEH5Wcg'


def get_Latest_price():
    response = requests.get(bitcoin_url)
    response_json = response.json()
    # Convert the price into Floating point
    return float(response_json[0]['price_usd'])


def post_Ifttt(event, value):
    data = {"Value": value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url, json=data)


def main():
    bitcoin_history = []
    while True:
        price = get_Latest_price()
        date = datetime.now()
        bitcoin_history.append({'Date': date, 'Price': price})
        if len(bitcoin_history) == 2:
            post_Ifttt('Bitcoin_price_update', bitcoin_history)
            bitcoin_history = []


if __name__ == '__main__':
    main()
