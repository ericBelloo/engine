
from django.urls import path
from apps.person.views import PersonLoginView, PersonSignUpView

app_name = 'person'

urlpatterns = [
    path('login/', PersonLoginView.as_view(), name='login'),
    path('sign_up/', PersonSignUpView.as_view(), name='sign_up')
]
