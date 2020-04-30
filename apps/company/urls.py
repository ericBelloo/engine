from django.urls import path
from apps.company.views import CompanyLoginView, CompanyHomeView

app_name = 'company'

urlpatterns = [
    path('account/', CompanyLoginView.as_view(), name='account_company'),
    path('home/', CompanyHomeView.as_view(), name='home'),
]
