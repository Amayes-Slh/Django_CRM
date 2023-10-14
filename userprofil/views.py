from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile  # Assurez-vous que le nom du modèle est correctement importé

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)  # Utilisez le nom correct du modèle

            return redirect('/log-in/')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })
