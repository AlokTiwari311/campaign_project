from django.contrib import admin
from django.urls import path, include
from .views import homepage  # Import the homepage view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),  # Your API routes
    path("", homepage),  # Root URL
]
