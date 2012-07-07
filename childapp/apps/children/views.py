from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from childapp.apps.children.models import Child
from childapp.apps.children.forms import ChildForm

@login_required
def index(request):
    children = Child.objects.all().filter(parent=request.user)
    c = RequestContext(request, {
        "children": children,
    })
    return render_to_response('children/index.html', context_instance=c)

@login_required
def view(request, id=None):
    child = Child.objects.get(id=int(id))
    c = RequestContext(request, {
        "child": child,
    })
    return render_to_response('children/view.html', context_instance=c)

@login_required
def edit(request, id=None):
    if id is not None:
        child = Child.objects.get(id=id)
    else:
        child = None
    form = ChildForm(request.POST or None, instance=child)

    if form.is_valid():
        child = form.save(commit=False)
        child.parent = request.user
        child.save()
        if id:
            return HttpResponseRedirect(reverse(view, kwargs={"id": id}))
        else:
            return HttpResponseRedirect(reverse(index, kwargs={}))

    c = RequestContext(request, {
        'form': form,
        'child': child,
        "is_new": child is None})

    return render_to_response('children/edit.html', context_instance=c)

@login_required
def delete(request, id=None):
    if id:
        child = Child.objects.get(id=id)
        child.delete()
    return HttpResponseRedirect(reverse(index, kwargs={}))
