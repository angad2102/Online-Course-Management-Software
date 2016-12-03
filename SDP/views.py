from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, this is View: SDP.index")

def instructor(request,user_id):
	user =  Users.objects.get(pk=user_id)
	return HttpResponse("Hello, this is View: SDP.index")

