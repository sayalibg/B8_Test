from django.shortcuts import HttpResponse, redirect, render

 

# Create your views here.

from .forms import AddressForm
# def simple_better(request):
#     return render(request, 'simple_better.html', {'form' : AddressForm()})

def crpy(request):
    return render(request, 'crpy.html', {'form' : AddressForm()})


# User creation form: -----------------------------------------------------------------
# Django UserCreationForm is used for creating a new user that can use our web application. 
# It has three fields: username, password1, and password2(which is basically used for password confirmation).
#  To use the UserCreationForm, we need to import it from django. contrib.


from django.contrib.auth.forms import UserCreationForm 
def user_creation(request):  
    form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'blank.html', context)  


def address_form(request):
    form = AddressForm()
    if request.method == 'POST':
        print(request.POST)
        form = AddressForm(data=request.POST)
        if form.is_valid():
            form.save()  # database save
            return HttpResponse("Successfully Registered!!!")
    else:
        context = {'form': form}
        return render(request, "simple_better.html",context=context)


# multiple views and .pyc file--- how to read and create--- pending