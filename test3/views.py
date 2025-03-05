import requests
from django.http import JsonResponse

NEWS_API_KEY = "your_api_key"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def get_news(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    params = {
        "apiKey": NEWS_API_KEY,
        "country": "us",
        "category": request.GET.get("category", ""),
    }
    response = requests.get(NEWS_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to fetch news", "status_code": response.status_code, "response_text": response.text}, status=400)
