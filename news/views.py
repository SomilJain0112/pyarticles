from django.shortcuts import render
import os
import requests
import chainecho
import random
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "index.html")

@require_GET
@csrf_exempt
def chainecho_news(request):
    try:
        api_key = os.getenv('CHAINECHO_API_KEY')
        
        if not api_key:
            return JsonResponse({"error": "API key not found. Please set CHAINECHO_API_KEY"}, status=400)
        
        api = chainecho.API(api_key)
        data = api.getLatestNews(limit=100)
        return JsonResponse(data, safe=False)
        
    except Exception as e:
        return JsonResponse({"error": f"Failed to fetch data from Chainecho: {str(e)}"}, status=500)

@require_GET
@csrf_exempt
def crypto_prices(request):
    try:
        crypto_prices = [
            {"symbol": "BTC", "name": "Bitcoin", "price": 43250.50, "change": 2.45},
            {"symbol": "ETH", "name": "Ethereum", "price": 2680.30, "change": 1.87},
            {"symbol": "BNB", "name": "Binance Coin", "price": 312.45, "change": -0.32},
            {"symbol": "ADA", "name": "Cardano", "price": 0.485, "change": 3.21},
            {"symbol": "SOL", "name": "Solana", "price": 98.75, "change": 5.67},
            {"symbol": "DOT", "name": "Polkadot", "price": 7.23, "change": -1.12},
            {"symbol": "LINK", "name": "Chainlink", "price": 15.89, "change": 2.34},
            {"symbol": "UNI", "name": "Uniswap", "price": 7.56, "change": 1.98},
            {"symbol": "AVAX", "name": "Avalanche", "price": 35.67, "change": -0.89},
            {"symbol": "MATIC", "name": "Polygon", "price": 0.89, "change": 4.12}
        ]
        
        for crypto in crypto_prices:
            price_change = random.uniform(-0.5, 0.5)
            crypto["price"] += crypto["price"] * price_change / 100
            crypto["change"] += random.uniform(-0.1, 0.1)
            crypto["change"] = max(-10, min(10, crypto["change"]))
        
        return JsonResponse(crypto_prices, safe=False)
        
    except Exception as e:
        return JsonResponse({"error": f"Failed to fetch crypto prices: {str(e)}"}, status=500)