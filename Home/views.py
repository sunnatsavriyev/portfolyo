from django.shortcuts import redirect, render
from .form import *
from .models import *

def IndexView(request):
    
    return render(request, 'index.html', {})


def ContactView(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contacts = ContactForm(name=name, email=email, message=message)
            contacts.save()
            return redirect("index")
        else :
            print('error')
            return redirect("index")
        
    ctx ={
        'form':form,
        'contacts':contacts,
    }
    return render (request, 'contact.html',ctx)


