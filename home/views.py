from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portofolio
from django.core.mail import send_mail
from django.contrib import messages



def home(request):
	portofolios = Portofolio.objects.all()
	# for portofolio in portofolios:
	# 	image_url = "{% static \'" + portofolio.image + "\' %}"
	context = {
		'portofolios': portofolios,
		# 'image_url': image_url
	}
	return render(request, 'home/index.html', context)

def mail(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']

		message_to_sent = 'A persone called ' + name + ' wants to contact you. His email is ' + email + ' and his phone number is ' + phone + '. His message is: (' + message + ').'

		send_mail('Someone contacted you', message_to_sent ,'redian1marku@example.com',['redian1marku@gmail.com'], fail_silently=False,)
		messages.success(request, f'Contact infos sent successfuly.')
		return redirect('home:home')
		
	return redirect('home:home')
