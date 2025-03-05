import os
import requests
from django.http import JsonResponse

NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # Get API key from environment
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def get_news(request):
    params = {
        "apiKey": NEWS_API_KEY,
        "country": "us",  # Change as needed
        "category": request.GET.get("category", ""),  # Optional filter
    }

    response = requests.get(NEWS_API_URL, params=params)

    if response.status_code != 200:
        return JsonResponse({
            "error": "Failed to fetch news",
            "status_code": response.status_code,
            "response_text": response.text
        }, status=500)

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        return JsonResponse({
            "error": "Invalid JSON response from News API",
            "response_text": response.text
        }, status=500)

    return JsonResponse(data)
