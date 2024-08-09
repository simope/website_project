import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Player, Game
from .common import createChart, createMap, extractIPandLocation

def play(request):
   template = loader.get_template('rockpaperscissors.html')  
   return HttpResponse(template.render())

def stats(request):
   chart, total = createChart()
   map = createMap()
   context = {'chart': chart, 'total': total, 'map': map}
   return render(request, 'stats.html', context)

@csrf_exempt
def save_to_DB(request):
   if request.method == 'POST':
      print(json.loads(request.body.decode()))
      result = json.loads(request.body.decode())['result']
      model = Game(result=result)
      model.save()
      return JsonResponse({'success': True})
   return JsonResponse({'success': False})