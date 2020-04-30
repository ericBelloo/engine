
from django.urls import path
from apps.utils.api.view import get_state_city
from apps.utils.views import process_state, process_city, process_cp, remove_cp

app_name ='utils'

urlpatterns = [
    path('get-direction/', get_state_city, name='get_direction'),
    path('process-state/', process_state, name='process_state'),
    path('process-city/', process_city, name='process_city'),
    path('process-cp/', process_cp, name='process_cp'),
    path('remove-cp/', remove_cp, name='remove_cp'),
]
