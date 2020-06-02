from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.views import View
from django.views.generic import FormView, CreateView

from apps.company.forms import CompanyForm, CompanyAddressForm, CompanyDocumentForm, CompanyNDAForm
from apps.person.forms import UserLoginForm, PersonForm, PersonDocumentForm, UserForm


class PersonLoginView(CreateView):
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
    template_name = 'account/sign_up.html'

    def get(self, request):
        context = dict()
        context['userForm'] = UserForm()
        context['personForm'] = PersonForm()
        context['personDocumentForm'] = PersonDocumentForm()
        context['companyForm'] = CompanyForm()
        context['companyAddressForm'] = CompanyAddressForm()
        context['companyDocumentForm'] = CompanyDocumentForm()
        return render(request, self.template_name, context)

    def post(self, request, *data,  **kwargs):
        user_form = UserForm(request.POST)
        person_form = PersonForm(request.POST)
        person_document_form = PersonDocumentForm(request.POST, request.FILES)
        if user_form.is_valid() and person_document_form.is_valid() and person_form.is_valid():
            document = person_document_form.save()  #  Guarda un documento
            user = user_form.save()  # Guarda un usuario
            person = person_form.save()  # Guarda una persona
            person.document = document  # Asigna los documentos a una persona
            person.user = user  # Asigna un usuario a una persona
            person.save()  # Guarda los cambios
        else:
            messages.error(request, 'Error al guardar los datos de la persona')
            return HttpResponseRedirect(reverse('person:sign_up'))
        company_direction_form = CompanyAddressForm(request.POST)
        company_document_form = CompanyDocumentForm(request.POST, request.FILES)
        company_form = CompanyForm(request.POST)
        if company_direction_form.is_valid() and company_document_form.is_valid() and company_form.is_valid():
            document = company_document_form.save()  # Guarda los documentos de empresa
            address = company_direction_form.save()  # Guarda la direccion de la empresa
            company = company_form.save()  # Gurada una empresa
            company.address = address  # Asigna una direccion a una empresa
            company.document = document  # Asigna documentos a una empresa
            company.save()  # Guarda los cambios de la empresa
            person.company = company  # Asigna una empresa a una persona
            person.save()  # Gurada los cambios
            request.session['pk'] = person.id  # inicia la seccion del usuario
        else:
            messages.error(request, 'Error al guardar los datos de la compañia')
            return HttpResponseRedirect(reverse('company:account_company'))
        return HttpResponseRedirect(reverse('person:home'))


class PersonHomeView(CreateView):
    template_name = 'profile/home.html'
    form_class = CompanyNDAForm
