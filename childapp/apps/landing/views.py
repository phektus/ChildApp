from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

