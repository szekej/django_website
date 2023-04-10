from django.shortcuts import render
from first_app.models import Webpage, Topic, AccessRecord, UserAll
from . import forms
from django.http import HttpResponse
from first_app.forms import NewUserForm, UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    return render(request, 'first_app/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("Validation successed!")
            print("NAME: ", form.cleaned_data['name'])
            print("EMAIL: ", form.cleaned_data['email'])
            print("TEXT: ", form.cleaned_data['text'])

    return render(request, 'first_app/formpage.html', {'form': form})


def myextension(request):
    my_dict = {'insert_me': "Im coming from views.py"}
    return render(request, 'first_app/myextension.html', context=my_dict)


def mtv(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/mtv.html', context=date_dict)


def users(request):
    users_list = UserAll.objects.order_by('last_name')
    users_dict = {'users': users_list}
    return render(request, 'first_app/users.html', context=users_dict)


def new_user(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'first_app/new_user.html', {'form': form})


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            print(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You're logged in, niceee!")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))   # redirected to index page
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to logi in and failed")
            print(f"Username: {username} Password: {password}")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'first_app/login.html', {})


def relative(request):
    return render(request, 'first_app/relative.html')
