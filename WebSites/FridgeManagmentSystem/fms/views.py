from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.db.models import Q

import sys
from models import Item
from models import Hanger

# For Barcode Lookup
from xmlrpclib import ServerProxy, Error


# Dictionary to add objects passed to the through to the HTML
script_args = {}
script_args['theme'] = "a"
script_args['site_url'] = 'http%3A//10.109.85.237:8081'

#script_args['site_url'] = 'http%3A//192.168.1.25:8081'


# For Barcode Lookup
rpc_key = '267b49217902750ecbe58a0e122b7394ab81199b'
    
# ALL ITEMS
items = []

def home(request):
  script_args["items"] = Item.objects.all()
  
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
    
  i_l_d = []
  local_upc = Item.objects.all().filter(Q(upc__iexact=ean))
   
  if (local_upc.exists()):
  
    # Happens when there is a local entry already stored
    i_l_d = [("Local data", "Found")]
    
    print "found you locally"
      
    #for key, value in local_upc[0]:
      #i_l_d.append((key,value))  

  else:
    # Redirects to the items page
    params = { 'rpc_key': rpc_key, 'upc': ean }
    
    item_lookup_data = s.lookup(params) 
    print item_lookup_data
    
    
    # Creating Hanger for New UPC
    #new_upc = Hanger(name=ean,hung_on=local_upc)
    #new_upc.save()
    
    new_item = Item(upc=ean)
    
    new_item._meta.get_all_field_names()
    
    for key, value in item_lookup_data.iteritems():
      i_l_d.append((key,value))
      setattr(new_item,key,value)
      new_item.save()
    
  script_args['item_lookup_data']= i_l_d
  
  return render_to_response("fms/item.html", script_args)    
