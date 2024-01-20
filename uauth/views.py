from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def user_login(request):
    return render(request,'uauth/login.html')
    # return HttpResponse("okay ")

def auth(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            # Display an error message
            error_message = "Invalid username or password"
            # return render(request, 'uauth/login.html', {'error_message': error_message})
            return HttpResponseRedirect(reverse('login'))
    else:
        # Display the login form
        return render(request, 'uauth/login.html')
    
def user_logout(request):
    logout(request)
    return redirect('home')