from django.http import JsonResponse
import requests

NEWS_API_KEY = "db85681c903b49d2905e71e5cf4900dd"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def get_news(request):
    params = {
        "apiKey": NEWS_API_KEY,
        "country": "us",  # Change as needed
        "category": request.GET.get("category", ""),  # Optional filter
    }

    response = requests.get(NEWS_API_URL, params=params)
    
    # **Debugging: Print response content**
    print("API Response Status:", response.status_code)
    print("API Response Content:", response.text)

    if response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch news", "status_code": response.status_code}, status=500)
    
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON response from News API"}, status=500)

    return JsonResponse(data)

