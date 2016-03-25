from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('index page of the webservice for cs4720 final project.')