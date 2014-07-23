from django.shortcuts import render, get_object_or_404
from django.http import *
from polls.models import *
from django.template import RequestContext, loader
# Create your views here.

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = RequestContext(request, {
        'latest_poll_list' : latest_poll_list,
    })
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll' : poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s" % poll_id)
