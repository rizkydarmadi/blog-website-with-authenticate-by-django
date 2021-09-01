from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from blog.views import ArtikelPerkategori

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'account was created for '+ username)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    context = {}
    return render(request,'home.html',context)




class BlogHomeView(TemplateView, ArtikelPerkategori):
    template_name = 'home.html'

    def get_context_data(self):
        QuerySets = self.get_latest_artikel_each_kategori()
        context = {
            'latest_artikel_list': QuerySets,
        }
        
        return context