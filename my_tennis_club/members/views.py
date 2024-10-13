from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  template = loader.get_template('indescribable.html')
  return HttpResponse(template.render())

