from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserCreationForm        
    return render(request, 'users/registr.html', {'title':'Сторінка реєстрації', 'form': form })
    
