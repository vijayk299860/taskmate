from django.shortcuts import render
from django.http import HttpResponse
from auth_app.forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registration successful.')
            return redirect('todolist')  
    else:
        register_form = CustomUserCreationForm()
        
    return render(request, 'registration.html', {'register_form': register_form})