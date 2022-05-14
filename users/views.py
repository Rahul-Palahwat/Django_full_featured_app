from django.shortcuts import render,redirect



# to restrict the page to loged in users only 
from django.contrib.auth.decorators import login_required




# # for form validations
# from django.contrib.auth.forms import UserCreationForm


# for alert(flash one time) we are importing this 
from django.contrib import messages
# types of messages 
# messages.debug
# messages.info 
# messages.success 
# messages.warning 
# messages.error 


# here we are importing the inherited form 
from .forms import UserRegisterForm



# Create your views here.
def register(request):
    # for handling the post request 
    if request.method=='POST':
        form=UserRegisterForm(request.POST)

        # now we will validate the data 
        if form.is_valid():
            # for saving data to backend 
            form.save()


            username=form.cleaned_data.get('username')
            # here we are using f string 
            messages.success(request,f'Your account has been created! You are now able to login {username}!')

            # now we will redirect the user to another page 
            return redirect('login')

    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{
        'form':form
    })


# this is a decorator to restrict page 
@login_required
def profile(request):
    return render(request,'users/profile.html')