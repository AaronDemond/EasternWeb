from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



from django.contrib.auth.models import User
def index(request):
	context = { 'data' : 12345 }
	try:
		value= request.POST['email']
		user = User.objects.create_user(value, value, '12345')
		user.save()
	except:
		value = -1
	return render(request, 'index.html', context)

def about(request):
	context = { 'data' : 12345 }

	return render(request, 'about.html', context)
	return HttpResponse("about_page")

def shop(request):
	context = { 'data' : 12345 }

	return render(request, 'shop.html', context)
	return HttpResponse("shop")


def contact(request):
	context = { 'data' : 12345 }
	return render(request, 'contact.html', context)
	return HttpResponse("contact")

def account(request):
	context = { 'data' : 12345 }
	return render(request, 'account.html', context)
	return HttpResponse("account")

