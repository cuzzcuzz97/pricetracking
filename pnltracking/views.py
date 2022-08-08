from django.shortcuts import render
from .models import CoinName
import requests
import json
from django.http import HttpResponse
# Create your views here.

def listToken(request):
    coin_list = []
    api = "https://www.binance.me/api/v3/ticker/price?symbols=[%22BTCUSDT%22,%22ZRXUSDT%22,%22PONDUSDT%22,%22VIDTUSDT%22,%22SUPERUSDT%22,%22FRONTUSDT%22]"
    list_token = ["BTCUSDT","ZRXUSDT","PONDUSDT","VIDTUSDT","SUPERUSDT","FRONTUSDT"]
    entry = ["23000","0.3476","0.01344","0.3588","0.17","0.28" ]
    response = requests.get(api)
    json_dict = json.loads(response.text)
    for i in range(len(list_token)):
        token = list_token[i]
        my_item = next((item for item in json_dict if item['symbol'] == token), None)
        price = float(my_item["price"])
        increase_percent = ((float(price) - float(entry[i]))/float(entry[i]))*100
        increase_percent = str(round(increase_percent,2))
        price_list = f'{list_token[i]} : {price} {increase_percent}%'
        # print(f'{list_token[i]} : {price} {round(increase_percent,2)}%')
        coin_list.append(price_list)
    return render(request, "pnltracking/index.html", {
        "coin_list":coin_list,
        "percent": increase_percent,
        })


