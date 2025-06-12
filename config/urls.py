from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("books_order.urls")),
    path('admin/', admin.site.urls),
]
