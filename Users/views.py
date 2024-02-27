from django.shortcuts import redirect, render
from django.contrib import messages
from Users.form import PassengerRegistrationForm
from django.contrib.auth import authenticate, login, logout

# Register a passenger

def register_passenger(request):
    if request.method == 'POST':
        form = PassengerRegistrationForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_passenger = True
            # print(form.errors)
            var.save()
            messages.info(request, 'Your account has been successfully created. Login to Continue')
            return redirect('user:login')
        else:
            messages.warning(request, 'something Went Wrong!!!! please check your input')
            return redirect('user:signin')
    else:
        form = PassengerRegistrationForm()
        context = {'form':form}
        return render(request, 'main/SignUp.html', context)
    

#User Login
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Login Successfull')
            return redirect('main:home')
        else:
            messages.warning(request, 'Something went wrong please check your inputs!!!')
            return redirect('user:login')
    else:
        return render(request, 'main/Login.html')

    # return render(request, 'Users/Login.html', context)

#Logout User
    
def user_logout(request):
    logout(request)
    messages.info(request, 'Logout successful....Login to continue')
    return redirect('main:home')
