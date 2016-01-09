from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def home(request):
	return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'lanigouws@gmail.com'),
                ['lanigouws@gmail.com'], #email address where message is sent.
            )
            return HttpResponseRedirect('/thanks/')
    return render(request, 'contact.html',
        {'errors': errors})

def thanks(request):
    return render_to_response('thanks.html')

def custom_404(request):
    return render(request,'404.html',status=404)
	 
def custom_500(request):
    return render(request,'500.html',status=500)

