from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

NEWS_API_KEY = "db85681c903b49d2905e71e5cf4900dd"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def get_news(request):
    params = {
        "apiKey": NEWS_API_KEY,
        "country": "us",  # Change as needed
        "category": request.GET.get("category", ""),  # Optional filter
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    return JsonResponse(data)
