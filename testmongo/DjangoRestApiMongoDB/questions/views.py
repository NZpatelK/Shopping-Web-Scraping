from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Question
from .serializers import questionSerializer

# Create your views here.
@csrf_exempt
def questApi (request, id=0):
    if request.method == 'GET':
        quests = Question.objects.all()
        quest_serial1 = questionSerializer(quests, many=True)
        return JsonResponse(quest_serial1.data, safe=False)
    elif request.method == 'POST':
        quest_data = JSONParser().parse(request)
        quest_serial2 = questionSerializer(data=quest_data)
        if quest_serial2.is_valid():
            quest_serial2.save()
            return JsonResponse(quest_serial2.data, safe=False)


