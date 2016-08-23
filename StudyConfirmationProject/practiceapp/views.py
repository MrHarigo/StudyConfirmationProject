from datetime import timezone

from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic import FormView
from .models import Certificate, Request
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import authenticate
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.core.mail import send_mail
from practiceapp.forms import ContactForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/account/invalid/")

@login_required
def index(request):
    if request.user.groups.filter(name='Students'):
        latest_certificate_list = Certificate.objects.order_by('-pub_date')[:100]
        context = {'latest_certificate_list': latest_certificate_list}
        return render(request, 'practiceapp/index.html', context)
    else:
        return render(request, 'registration/login.html')

@login_required
def detail(request, certificate_id):
    if request.user.groups.filter(name='Students'):
        certificate = get_object_or_404(Certificate, pk=certificate_id)
        return render(request, 'practiceapp/contact_form.html', {'certificate': certificate})
    else:
        return render(request, 'registration/login.html')

@login_required
def contact(request):
    if request.user.groups.filter(name='Students'):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                request = Request.objects.create_request(request.certificate_id , request.user.mysiteprofile.group, request.user.last_name, request.user.first_name, request.user.mysiteprofile.father_name, cd, timezone.now())
                request.save()
            return HttpResponseRedirect('/practiceapp/thanks/')
            #return render_to_response('practiceapp/contact_form.html', {'form': form})
        else:
            form = ContactForm(
            )
        return render_to_response('practiceapp/contact_form.html', {'form': form})
    else:
        return render(request, 'registration/login.html')

@login_required
def thanks(request):
    if request.user.groups.filter(name='Students'):
        return render_to_response('practiceapp/thanks_form.html')
    else:
        return render(request, 'registration/login.html')

def logout(request):
    if request.user.groups.filter(name='Students'):
        auth.logout(request)
        return render_to_response('registration/logout.html')
    else:
        return render(request, 'registration/login.html')

@login_required
def requests(request):
    if request.user.groups.filter(name='Deanery'):
        latest_requests_list = Request.objects.order_by('-pub_date')[:5]
        context = {'latest_requests_list': latest_requests_list}
        return render(request, 'practiceapp/requests.html', context)
    else:
        return render(request, 'registration/login.html')