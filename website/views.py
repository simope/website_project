from django.http import HttpResponse
from django.template import loader
from main.common import extractIPandLocation

def home(request):
  template = loader.get_template('home.html')
  ip = request.META.get('HTTP_X_FORWARDED_FOR')
  extractIPandLocation(ip)
  return HttpResponse(template.render())