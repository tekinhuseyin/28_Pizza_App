from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
# Create your views here.
def register(request):


    #form=UserCreationForm()
    form=UserForm()

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context={
        'form':form
    }
    return render(request, 'users/register.html', context)