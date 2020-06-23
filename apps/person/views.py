from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.views import View
from django.views.generic import ListView, CreateView

from apps.company.forms import CompanyForm, CompanyAddressForm, CompanyDocumentForm
from apps.person.forms import UserLoginForm, PersonForm, PersonDocumentForm, UserForm, PersonPetitionNDAForm
from apps.person.models import Person, PetitionNDA


class PersonLoginView(CreateView):
    template_name = 'account/login.html'
    form_class = UserLoginForm

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('person:home'))
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
            user.last_name = user_form.cleaned_data['last_name'] + ' ' + user_form.cleaned_data['second_last_name'] # Guarda el apellido completo
            user.set_password(user_form.cleaned_data['password'])  # establece la contraseña
            user.save()  # actualiza el nombre
            person = person_form.save()  # Guarda una persona
            person.document = document  # Asigna los documentos a una persona
            person.user = user  # Asigna un usuario a una persona
            person.save()  # Guarda los cambios
        else:
            messages.error(request, 'El correo ya fue registrado')
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
        else:
            messages.error(request, 'Error al guardar los datos de la empresa')
            return HttpResponseRedirect(reverse('person:sign_up'))
        # Logea al usuario si se guardo correctamente
        if user is not None:
            login(request, user)
        return HttpResponseRedirect(reverse('person:home'))


class PersonHomeView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'profile/home.html'

    def get_queryset(self):
        person = Person.objects.get(user=self.request.user)
        return PetitionNDA.objects.filter(person=person)

    def get_context_data(self, **kwargs):
        context = super(PersonHomeView, self).get_context_data()
        person = Person.objects.get(user=self.request.user)
        context['person'] = person
        return context


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('person:login'))


class PersonNewPetitionView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'profile/new_petition.html'
    form_class = PersonPetitionNDAForm

    def post(self, request, *args, **kwargs):
        if 'cmg' in self.request.FILES:
            PetitionNDA.objects.create(petition_type='cmg', file=self.request.FILES['cmg'], user=self.request.user)
        if 'dgj' in self.request.FILES:
            PetitionNDA.objects.create(petition_type='dgj', file=self.request.FILES['dgj'], user=self.request.user)
        if 'gnp' in self.request.FILES:
            PetitionNDA.objects.create(petition_type='gnp', file=self.request.FILES['gnp'], user=self.request.user)
        if 'dgq' in self.request.FILES:
            PetitionNDA.objects.create(petition_type='dgq', file=self.request.FILES['dgq'], user=self.request.user)
        if 'tmg' in self.request.FILES:
            PetitionNDA.objects.create(petition_type='tmg', file=self.request.FILES['tmg'], user=self.request.user)
        if 'ngm' in self.request.FILES:
            PetitionNDA.objects.create(petition_type='ngm', file=self.request.FILES['ngm'], user=self.request.user)

        messages.success(request, 'Envio exitoso')
        return HttpResponseRedirect(reverse('person:new_petition'))
