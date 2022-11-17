from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from warehouse.models import Component, User
from warehouse.validator import *


class WarehouseView:
    def __init__(self,*args,**kwargs):
        self.validation = Validator()

    def Index(self, request):

        return render(request, 'warehouse/index.html')

    def SignUp(self, request):
        if request.method == "POST":
            username = request.POST.get("uname", False)
            password = request.POST.get("psw", False)
            email = request.POST.get("email", False)
            validation = self.validation.EmailValidation(email)
            print("print username", username, "kai to passs", password, "kai to mail", email)
            context = {
                'user': username,
                'password': password,
                'email': email,
            }
            userSave = User(username=username, password=password, email=email)
            userSave.save()
            return redirect("/components/")
        return render(request, 'warehouse/sing_up.html')

    def Login(self, request):
        if request.method == "POST":
            username = request.POST.get("username", False)
            email = request.POST.get("email", False)
            password = request.POST.get("password", False)
            print("login username", username, "email", email, "password", password)
            return redirect("/components/")

        return render(request, 'warehouse/login.html')

    def Show_components(self, request):
        components = Component.objects.all()
        context = {
            'components': components,
        }
        return render(request, 'warehouse/select.html', context)

    def ComponentMenu(self, request):
        if request.method == "POST":
            print("inside the component menu")
            code = request.POST.get("code", False)
            types = request.POST.get("types", False)
            characteristic = request.POST.get("characteristic", False)
            componentSave = Component(code=code, types=types, characteristics=characteristic)
            componentSave.save()
            print("print insert components code", code, " type ", types, "characteristic ", characteristic)
            return render(request, 'warehouse/Component_menu.html')
        return render(request, 'warehouse/Component_menu.html')
