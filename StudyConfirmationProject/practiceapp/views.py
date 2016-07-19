from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic

from .models import Certificate, Question
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse


class IndexView(generic.ListView):
    template_name = 'practiceapp/index.html'
    context_object_name = 'latest_certificate_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Certificate.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Certificate
    template_name = 'practiceapp/detail.html'

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
        typed_answer.answer += 1
        typed_answer.save(),
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('practiceapp:results', args=(p.id,)))


from django.shortcuts import render

# Create your views here.
