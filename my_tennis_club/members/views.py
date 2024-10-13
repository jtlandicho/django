from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def members2(request):
  template = loader.get_template('indescribibable.html')
  return HttpResponse(template.render())