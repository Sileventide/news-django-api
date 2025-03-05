
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('test3.urls')),  # Ensure 'test3' app's URLs are included
]

