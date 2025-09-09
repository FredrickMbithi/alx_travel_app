"""
URL configuration for the Listings app.
Currently only serves a placeholder home endpoint.
"""

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='listings-home'),
]
