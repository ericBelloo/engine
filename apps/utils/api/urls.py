
from django.urls import path
from apps.utils.api.view import get_direction

app_name ='utils_api'

urlpatterns = [
    path('get-direction/', get_direction, name='api_get_direction'),
]