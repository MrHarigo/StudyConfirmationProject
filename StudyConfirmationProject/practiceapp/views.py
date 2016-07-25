from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic import FormView
from .models import Certificate, Question
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import authenticate
from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render


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
    template_name = 'practiceapp/detail.html'

class Results(generic.DetailView):
    template_name = 'practiceapp/results.html'


def vote(request, certificate_id):
    p = get_object_or_404(Certificate, pk=certificate_id)
    try:
        typed_answer = p.question_set.get(pk=request.POST['question'])
    except (KeyError, Certificate.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'practiceapp/detail.html', {
            'certificate': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        typed_answer.answer = typed_answer,
        typed_answer.save(),
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('practiceapp:results', args=(p.id,)))



