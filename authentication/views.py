from multiprocessing import context
from pyexpat import model
from re import template
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from . form import UserUpdateForm, ProfileUpdateForm, ContactsForm, BankCardForm
from django.views.generic.edit import CreateView
from django.views.generic import  ListView

from .models import BankCard, Category


# Create your views here.

def home(request):
    return render(request, "authentication/baseFront.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        f_name = request.POST['f_name']
        s_name = request.POST['s_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email address already exist")
            return redirect('signup')

        if password != c_password:
            messages.error(request, "Passwords didn't match")

        else:
            myUser = User.objects.create_user(username, email, password)
            myUser.first_name = f_name
            myUser.last_name = s_name
            myUser.email = email
            myUser.save()
            messages.success(request, "Your account has been successfully created")
            return redirect('signin')
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            f_name = user.first_name
            return render(request, "authentication/profile.html", {'f_name': f_name})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('signin')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')


def features(request):
    return render(request, "authentication/features.html")


def contacts(request):
    error=' '
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            error = 'form is incorrect'

    form = ContactsForm()    
    contacts = {
        'form': form,
        'error': error
    }
    return render(request, "authentication/contactuspage.html", contacts)


def why(request):
    return render(request, "authentication/whycashflow.html")


def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "authentication/profile.html", context)



# class AddNewBankCard(CreateView):
#     model = BankCard
#     form_class = BankCardForm
#     template_name = 'authentication/addnewbankcard.html'

def addNewBankCard(request):
    if request.method == "POST":
        form = BankCardForm(request.POST)
        if form.is_valid():
            card_name = form.cleaned_data.get('cardName')
            card_balance = form.cleaned_data.get('cardBalance')

            model = BankCard.objects.filter(cardName = card_name)
            new_balance = model[0].cardBalance + card_balance
            model.update(cardBalance=new_balance)

            return redirect('account')

    else:
        form = BankCardForm()

    context = {
        'form': form
    }
    return render(request, "authentication/addnewbankcard.html", context)
    

# class AddBankName(CreateView):
#     model = Category  
#     template_name = 'authentication/addbankname.html'
#     fields = '__all__'

def addBankName(request):
    if request.method == "POST":
        card_name = request.POST["name"]
        
        model = BankCard(cardName=card_name, cardBalance=0)
        model.save()
        return redirect('bankcard')
    return render(request, "authentication/addbankname.html")

class AccountListView(ListView):
    model = BankCard
    context_object_name = 'account_list'  
    template_name = 'authentication/account.html'  


@login_required
def edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, "authentication/edit.html", context)
