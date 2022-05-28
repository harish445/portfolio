from django.shortcuts import render
from .models import Profile, Skills
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    skill = Skills.objects.all()
    context = {'profile': profile, 'skill': skill}
    return render(request, 'index.html', context)

def sendEmail(request):
    
    if request.method == 'POST':
        template = render_to_string('email_template.html', {
            'lastname':request.POST['lastname'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['harishthakur4455@gmail.com']
        )
        
        email.fail_silently=False
        email.send()
        
    return render(request, 'email_sent.html')
