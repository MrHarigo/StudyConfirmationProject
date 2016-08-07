from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic import FormView
from .models import Certificate, Question
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import authenticate
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.core.mail import send_mail
from practiceapp.forms import ContactForm

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "registration/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/index.html"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class IndexView(generic.ListView):
    template_name = 'practiceapp/index.html'
    context_object_name = 'latest_certificate_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Certificate.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Certificate
    template_name = 'practiceapp/contact_form.html'

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['group'],
                cd['surname'],
                cd['name'],
                cd['father_name'],
                cd['amount'],
                ['damir.serazetdinow@yandex.ru'],
            )
            return HttpResponseRedirect('/practiceapp/thanks/')
        else:
            form = ContactForm(
                initial={'name': request.user.first_name,
                         'surname': request.user.last_name,}
            )
        return render_to_response('practiceapp/contact_form.html', {'form': form})

def thanks(request):
    return render_to_response('practiceapp/thanks_form.html')