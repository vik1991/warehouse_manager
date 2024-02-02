from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from warehouse.models import Component
from warehouse.forms import LoginForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class WarehouseView:
    def __init__(self, *args, **kwargs):
        pass

    def Index(self, request):

        return render(request, 'warehouse/index.html')

    def signUp(self, request):
        if request.method == "POST":
            username = request.POST.get("uname", False)
            password = request.POST.get("psw", False)
            email = request.POST.get("email", False)
            form = LoginForm(request.POST)

            if form.is_valid():
                print("print username", username, "kai to passs", password, "kai to mail", email)
                userSave = User.objects.create_user(username, email, password)
                userSave.save()

                return redirect('/login')
            else:
                print('lathos email')
        return render(request, 'warehouse/sing_up.html')

    def login_user(self, request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            print("login username", username, "password", password)
            print("to onoma einai ", user)
            if user is not None:
                login(request, user)
                return redirect("/components")
            else:
                print("enter the correct password")
                return redirect("/login")
        return render(request, 'warehouse/login.html')

    def show_components(self, request):
        components = Component.objects.all()

        context = {
            'components': components,
        }
        return render(request, 'warehouse/select.html', context)

    def componentMenu(self, request):
        if not request.user.is_authenticated:
            print("user is not authenticated", request.user)
            return redirect("/login")
        if request.method == "POST":
            print("inside the component menu")
            code = request.POST.get("code", False)
            types = request.POST.get("types", False)
            characteristic = request.POST.get("characteristic", False)
            componentSave = Component(code=code, types=types, characteristics=characteristic)
            componentSave.save()
            print("print insert components code", code, " type ", types, "characteristic ", characteristic)
            return render(request, 'warehouse/component_menu.html')
        else:
            return render(request, 'warehouse/component_menu.html')
        return render(request, 'warehouse/login.html')


    def show_users(self, request):
        print("eimaste sto show users")
        pass

    def logout_view(self, request):
        print("kaname logout")
        logout(request)
        return redirect('/login')

    def change_password(self, request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            new_password = request.POST['new_password']
            user = authenticate(username=username, password=password)
            print("o user einai", user)
            if user is not None:
                u = User.objects.get(username__exact=username)
                password_check = u.check_password(password)
                print(" password_checker  is", password_check)
                user.set_password(new_password)
                user.save()
                print("password changet to ", new_password)
                print("to user pass einai", user)
                print("to username", username, "to password", password, "to new password ", new_password)
                # check = check_password(password,)

                return redirect("/login")

        else:
            return render(request, "warehouse/change_password.html")
        return render(request, "warehouse/change_password.html")
