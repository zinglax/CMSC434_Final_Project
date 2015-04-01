from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict

# Dictionary to add objects passed to the through to the HTML
script_args = {}
script_args['theme'] = "b"
    

def home(request):
  return render_to_response("fms/home.html", script_args)
