from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader




def index(request):
	context = { 'data' : 12345 }
	return render(request, 'index.html', context)
    #return HttpResponse("helloworld")


