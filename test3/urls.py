from django.urls import path
from .views import get_news  # Import the view function

urlpatterns = [
    path('news/', get_news, name="get_news"),  # This will be accessed as /api/news/
]

