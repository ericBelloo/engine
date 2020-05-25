from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.views import View
from django.views.generic import FormView

from apps.company.forms import CompanyForm, CompanyAddressForm, CompanyDocumentForm
from apps.person.forms import UserLoginForm, PersonForm, PersonDocumentForm, UserForm


class PersonLoginView(FormView):
    template_name = 'account/login.html'
    form_class = UserLoginForm

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('person:login'))
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return HttpResponseRedirect(reverse('person:login'))


class PersonSignUpView(View):

    context = dict()
    template_name = 'account/sign_up.html'

    def get(self, request, *data, **kwargs):
        self.context['userForm'] = UserForm()
        self.context['personForm'] = PersonForm()
        self.context['personDocumentForm'] = PersonDocumentForm()
        self.context['companyForm'] = CompanyForm()
        self.context['companyAddressForm'] = CompanyAddressForm()
        self.context['companyDocumentForm'] = CompanyDocumentForm()
        return render(request, self.template_name, self.context)

    def post(self, request, *data, **kwargs):
        user_form = UserForm(request.POST)
        person_form = PersonForm(request.POST)
        person_document_form = PersonDocumentForm(request.POST, request.FILES)
        if user_form.is_valid() and person_document_form.is_valid() and person_form.is_valid():
            document = person_document_form.save()
            person = person_form.save()
            person.document = document
            person.save()
        else:
            messages.error(request, 'Error al guardar los datos de la persona')
            return HttpResponseRedirect(reverse('company:account_company'))
        company_direction_form = CompanyAddressForm(request.POST)
        company_document_form = CompanyDocumentForm(request.POST, request.FILES)
        company_form = CompanyForm(request.POST)
        if company_direction_form.is_valid() and company_document_form.is_valid() and company_form.is_valid():
            document = company_document_form.save()
            address = company_direction_form.save()
            company = company_form.save()
            company.address = address
            company.document = document
            company.save()
            person.company = company
            person.save()
            request.session['pk'] = person.id
        else:
            messages.error(request, 'Error al guardar los datos de la compañia')
            return HttpResponseRedirect(reverse('company:account_company'))
        return HttpResponseRedirect(reverse('company:home'))
