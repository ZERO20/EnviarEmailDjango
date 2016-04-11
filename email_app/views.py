from django.shortcuts import render

# Create your views here.
from  django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string,get_template
from django.core.mail import EmailMessage
from django.conf import settings

def enviar_uno(request):
	asunto = 'Soy un email txt'
	para = ['destino@gmail.com']
	de = 'origen@gmail.com'

	ctx = {
		'usuario':'Edgar',
		'compra':'Libros'
	}

	message = render_to_string('email.txt',ctx)
	#Puede omitirse si se desea el campo from_email y en su lugar django
	#cojerá la constante definida en el settings.py de DEFAULT_FROM_EMAIL,
	#de esta forma se puede ahorrar configurar el remitente por defecto.
	EmailMessage(asunto,message,to=para,from_email=de).send()
	return HttpResponse('enviar_uno_txt')

def enviar_dos(request):
	asunto = 'Soy un correo html'
	para = ['destino@gmail.com']
	de = settings.EMAIL_HOST_USER

	ctx = {
		'usuario':'Edgar',
		'compra': 'Libros'
	}

	message = get_template('email.html').render(Context(ctx))
	msg = EmailMessage(asunto,message,to=para,from_email=de,reply_to=['otro@ejemplo.com'])
	msg.content_subtype = 'html'
	msg.send()
	return HttpResponse('email_dos_html')
