
from django.urls import path
from apps.person.views import *

app_name = 'person'

urlpatterns = [
    path('', PersonLoginView.as_view(), name='login'),
    path('login/', PersonLoginView.as_view(), name='login'),
    path('sign_up/', PersonSignUpView.as_view(), name='sign_up'),
    path('logout/', logout_view, name='logout'),
    path('home/', PersonHomeView.as_view(), name='home'),
    path('new_petition/', PersonNewPetitionView.as_view(), name='new_petition'),
]
