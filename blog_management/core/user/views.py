from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm, UserRegistration, UserEditForm, ProfileEditForm
from .models import Profile


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) # Doubt
        if form.is_valid():
            cd = form.cleaned_data
            #print(cd['username'],cd['password'])
            user = authenticate(request,username=cd['username'],password=cd['password'])
            #print(user)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
                else:
                    return HttpResponse("Disabled registration")
            else:
                return HttpResponse("Invalid Credentials")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section': dashboard})

def register(request):
    user_form = None
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user':new_user})
        else:
            user_form = UserRegistration()
    return render(request,'account/register.html',{'user_form':user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        #is allowing only for super users...No idea how
        #fixme
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{
        'user_form':user_form,
        'profile_form': profile_form
    })
