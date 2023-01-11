from django.urls import path

from .views import Home


app_name = 'menu'

urlpatterns = [
    path('', Home.as_view())
]