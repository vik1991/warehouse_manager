from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from warehouse.models import Component, User
from warehouse.forms import LoginForm
from django.contrib.auth.hashers import make_password, check_password


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
                hashedPassword = make_password(password)

                print("print username", username, "kai to passs", hashedPassword, "kai to mail", email)
                context = {
                    'user': username,
                    'password': hashedPassword,
                    'email': email,
                }
                userSave = User(username=username, password=hashedPassword, email=email)
                userSave.save()
                id = "1"
                print("to id ienia auto", type(id), id)

                return redirect('/components/' + id + "/")
            else:
                print('lathos email')
        return render(request, 'warehouse/sing_up.html')

    def login(self, request):
        if request.method == "POST":
            username = request.POST.get("username", False)
            email = request.POST.get("email", False)
            password = request.POST.get("password", False)
            hashedPassword = User.odjects.filter(username)
            print("to onoma einai ", hashedPassword)
            checkPassword = check_password(hashedPassword, password)
            print("login username", username, "email", email, "password", password)
            if checkPassword:
                return redirect("/components/")
            else:
                print("enter the correct password")
                return render(request, 'warehouse/login.html')
        return render(request, 'warehouse/login.html')

    # def call_user

    def show_components(self, request):
        components = Component.objects.all()

        context = {
            'components': components,
        }
        return render(request, 'warehouse/select.html', context)

    def componentMenu(self, request,user_id=None):
        print("userid",user_id)
        print(request.user)

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


