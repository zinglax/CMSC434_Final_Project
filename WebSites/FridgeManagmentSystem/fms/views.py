from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict

import sys

# For Barcode Lookup
from xmlrpclib import ServerProxy, Error


# Dictionary to add objects passed to the through to the HTML
script_args = {}
script_args['theme'] = "a"
script_args['site_url'] = 'http%3A//10.109.246.11:8080'

# For Barcode Lookup
rpc_key = '267b49217902750ecbe58a0e122b7394ab81199b'
    
# ALL ITEMS
items = []

def home(request):
  script_args["range"] =  range(15)
  return render_to_response("fms/home.html", script_args)

def item(request):
  s = ServerProxy('http://www.upcdatabase.com/xmlrpc')
  
  # Gets the ean-code value    
  ean = request.GET.get('ean', '')
  print ean
  
  # Nothing Scanned
  if (ean == ''):
    return render_to_response("fms/home.html",script_args)  
  elif (len(ean) == 13 and ean[0]=='0'):
    # Scanned From Pic-2-Shop App From Mobile Device (Trims leading 0)
    ean = ean[1:]
  
  # elif """query for upc locally"""
  # Happens when there is a local entry already stored
  
  # Redirects to the items page
  params = { 'rpc_key': rpc_key, 'upc': ean }
  
  item_lookup_data = s.lookup(params) 
  print item_lookup_data
  i_l_d = []
  
  for key, value in item_lookup_data.iteritems():
    i_l_d.append((key,value))
    
    
  
  script_args['item_lookup_data']= i_l_d
  
  return render_to_response("fms/item.html", script_args)    
      
  
  return render_to_response("fms/item.html", script_args)