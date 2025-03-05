import os
import requests
from django.http import JsonResponse

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY", "660ffbd3e80757c6b2f55bf5e51fbce1")
GNEWS_API_URL = "https://gnews.io/api/v4/top-headlines"

def get_news(request):
    """Fetch news from GNews API and return it to the frontend."""

    params = {
        "token": GNEWS_API_KEY,  # GNews API requires 'token' instead of 'apiKey'
        "country": "us",  # Change as needed
        "category": request.GET.get("category", "general"),  # Default to 'general'
        "lang": "en",  # Language filter
        "max": 10,  # Number of articles (Free tier allows up to 10)
    }

    response = requests.get(GNEWS_API_URL, params=params)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({
            "error": "Failed to fetch news",
            "status_code": response.status_code,
            "response_text": response.text
        }, status=400)
