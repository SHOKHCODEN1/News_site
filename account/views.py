from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login , authenticate
from django.http import HttpResponse
from django.urls import reverse


def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request , 
                                username = data['username'] , 
                                password = data['password'])
            if user is not None:      
                if user.is_active:
                    login(request , user)
                    return render(request, 'registration/login_success.html')
                else:
                    return HttpResponse('username yoki parol xato!')
            else: 
                HttpResponse('Login xato')
        else:
            return HttpResponse('Formaga tugri malumot kiriting!')
    else:
        form = LoginForm()
        context = {'form':form}
        return render(request, 'registration/login.html', context)