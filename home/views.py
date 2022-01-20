from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm
from home.models import contact

# Create your views here.
def funhome(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            res=contact(from_email=email,subject=subject,message=message)  #for database save
            res.save()
            messages.info(request,'message send successfully')
            #try:
             #   send_mail(subject, message, email, ['narayanmore2525@gmail.com'])
            #except BadHeaderError:
            #    return HttpResponse('Invalid header found.')
            #return redirect('http://localhost:8000/home/')

    res= render(request, 'home/home.html', {'form': form})
    return res

    #form = ContactForm()


    #res=render(request,'home/home.html',{'form':form})
   # return res

