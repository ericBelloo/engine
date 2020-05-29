
from django.urls import path
from apps.utils.views import process_state, process_city, process_colony, remove_cp

app_name ='utils'

urlpatterns = [
    path('process-state/', process_state, name='process_state'),
    path('process-city/', process_city, name='process_city'),
    path('process-colony/', process_colony, name='process_colony'),
    path('remove-cp/', remove_cp, name='remove_cp'),
]
