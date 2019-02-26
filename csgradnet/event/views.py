from django.shortcuts import render

#these imports support the good ol way of loader and templates seen in def newname2 rendering events
from django.http import HttpResponse
from django.template import loader

from event.models import event

# Create your views here.
def eventview(request):
        all_events = event.objects.all()
        template = loader.get_template('eventpage/eventmanifest.html')
        context = { 'all_events' : all_events, }
        return HttpResponse(template.render(context, request))