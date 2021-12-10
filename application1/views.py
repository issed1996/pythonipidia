from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from .models import Guest, Movie, Reservation, Post
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer, PostSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins, viewsets

from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#from .permissions import IsAuthorOrReadOnly
import json

def index(request):
    return render(request,'index.html')




def ws(request):
    paths={
        'topics':'http://127.0.0.1:8000/ws/topics',
        'le_topic':'http://127.0.0.1:8000/ws/topics/le_topic',
        'annuaire':'http://127.0.0.1:8000/ws/annuaire'   
    }
    return JsonResponse(paths,safe=False)



#1 without REST and no model query FBV
def topics(request):
    with open('data.json', 'r') as file:
        data = json.load(file)
    topics=list(data['topics'].keys())    
    return JsonResponse (topics, safe=False)


def annuaire(request):
    with open('data.json', 'r') as file:
        data = json.load(file)
    annuaire=data['annuaire']    
    return JsonResponse (annuaire, safe=False)



def le_topic(request,topic):
    with open('data.json', 'r') as file:
        data = json.load(file)

    try: 
        return JsonResponse (data['topics'][str(topic)], safe=False)
    except :#topic.DoesNotExists:
        return JsonResponse ([], safe=False)


@api_view(['GET','POST'])
def le_topic(request,topic):
    
    if request.method=='GET':
        with open('data.json', 'r') as file:
            data = json.load(file)

        try: 
            return Response (data['topics'][str(topic)])
        except :#topic.DoesNotExists:
            return Response ([])

""" if request.method=='POST': 
        with open('data.json', 'r') as file:
            data = json.load(file)
        if request.data.
        data['topics'][str(topic)]  
"""



@api_view(['GET'])
def topics(request):
    with open('data.json', 'r') as file:
        data = json.load(file)
    # GET
    if request.method == 'GET':
        topics=list(data['topics'].keys()) 
        return Response(topics)