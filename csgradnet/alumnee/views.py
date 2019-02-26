# Create your views here.
#these imports support the shortcut approach whic uses render compacted with template pull and HttpResponse
from django.shortcuts import render
from django.http import Http404

#these imports support the good ol way of loader and templates seen in def newname2 rendering events
from django.http import HttpResponse
from django.template import loader

from alumnee.models import alumnee
from event.models import event


# Create your views here.
#this view has got bugs
def home(request):
    return render(request, 'home.html')

def alumnees(request):

    all_alumnees = alumnee.objects.all()
    context = { 'all_alumnees' : all_alumnees, }
    return render(request, 'alumnee/alumnee_manifest.html',context )

def alumnee_details(request, alumnee_id):
    try:
        alumnee_object = alumnee.objects.get(id=alumnee_id)

    except Exception as e:
        raise Http404("That Graduator does not exist")
    return render(request, 'alumnee/alumnee_details.html', { 'alumnee_object': alumnee_object })


def eventview(request):
        all_events = event.objects.all()
        template = loader.get_template('eventpage/eventmanifest.html')
        context = { 'all_events' : all_events, }
        return HttpResponse(template.render(context, request))
