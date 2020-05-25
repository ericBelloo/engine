from django.contrib import messages
from django.core.mail import EmailMessage, send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import View, FormView
from apps.person.forms import PersonForm, PersonDocumentForm
from apps.company.forms import CompanyForm, CompanyAddressForm, CompanyDocumentForm, CompanyNDAForm
from apps.person.models import Person


class CompanyLoginView(View):
    context = dict()
    template_name = 'account/sign_up.html'

    def get(self, request, *data, **kwargs):
        self.context['personForm'] = PersonForm()
        self.context['personDocumentForm'] = PersonDocumentForm()
        self.context['companyForm'] = CompanyForm()
        self.context['companyAddressForm'] = CompanyAddressForm()
        self.context['CompanyDocumentForm'] = CompanyDocumentForm()
        return render(request, self.template_name, self.context)

    def post(self, request, *data, **kwargs):
        person_form = PersonForm(request.POST)
        person_document_form = PersonDocumentForm(request.POST, request.FILES)
        if person_document_form.is_valid() and person_form.is_valid():
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


class CompanyHomeView(FormView):
    template_name = 'profile/home.html'
    form_class = CompanyNDAForm
    success_url = '/company/home/'

    def form_valid(self, form):
        messages.success(self.request, 'La informacion se envio correctamente')
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(CompanyHomeView, self).get_context_data()
        if 'pk' in self.request.session:
            context['person'] = Person.objects.get(id=self.request.session['pk'])
        return context

