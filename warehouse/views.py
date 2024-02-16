from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from warehouse.models import Component, UserComponentPivot
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
            remember_me = request.POST.get("remember_me")
            print(remember_me)
            form = LoginForm(request.POST)
            if form.is_valid():
                print("print username", username, "kai to passs", password, "kai to mail", email)
                userSave = User.objects.create_user(username, email, password)
                userSave.save()
                if remember_me:
                    request.session.set_expiry(604800)
                    print('to remember me einai pathmeno')
                else:
                    request.session.set_expiry(0)
                    print('to remember me DEEEEEN einai pathmeno')

                return redirect('/login')
            else:
                print('lathos email')
        return render(request, 'warehouse/sing_up.html')

    def login_user(self, request):
        valuenext = request.POST.get('next')
        print('to next einai =', valuenext)
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            print("login username", username, "password", password)
            print("to onoma einai ", user)
            if user is not None:
                login(request, user)
                if valuenext == "":
                    return redirect("/components")
                else:
                    return redirect(valuenext)
            else:
                print("enter the correct password")
                return redirect("/login")
        return render(request, 'warehouse/login.html')

    @method_decorator(login_required)
    def show_component(self, request):

        user = request.user
        componentId = UserComponentPivot.objects.filter(user_id=user).values('component_id_id')
        print('ola ta  components einai ', componentId, '   kai oi users einai ', user)
        components = Component.objects.filter(id__in=componentId)
        print('ta epilegmena id ton components einai ', components)
        context = {
            'components': components,
            'user': user,
        }
        print(context)
        return render(request, 'warehouse/show_component.html', context)

    @method_decorator(login_required)
    def edit_component(self, request):
        user = request.user
        if request.method == 'POST':
            code = request.POST.get('code', False)
            types = request.POST.get('types', False)
            characteristics = request.POST.get('characteristics', False)
            typesId = request.POST.get('typesId', False)
            codeId = request.POST.get('codeId', False)
            characteristicsId = request.POST.get('characteristicsId', False)
            print(f'sssssssss {codeId} sssssssssss {typesId} ssssssssssssssssssss {characteristicsId} ssssssss', code,
                  types,
                  characteristics)
            if code is not False and code is not "":
                updateCode = Component.objects.get(id=codeId)
                updateCode.code = code
                updateCode.save()
            if types is not False and types is not "":
                updateTypes = Component.objects.get(id=typesId)
                updateTypes.types = types
                updateTypes.save()
            if characteristics is not False and characteristics is not "":
                characteristicsUpdate = Component.objects.get(id=characteristicsId)
                characteristicsUpdate.characteristics=characteristics
                characteristicsUpdate.save()

            return redirect("/edit_component")

        else:
            componentId = UserComponentPivot.objects.filter(user_id=user).values('component_id_id')
            components = Component.objects.filter(id__in=componentId)
            context = {
                'components': components

            }
            return render(request, "warehouse/edit_component.html", context)

        return render(request, "warehouse/edit_component.html")

    @method_decorator(login_required)
    def delete_components(self, request):
        user = request.user
        if request.method == 'POST':
            componentId = request.POST['component.id ']
            print('edw blepoume to component.id', componentId)
            deleteComponent = Component.objects.filter(id=componentId)
            deleteComponent.delete()
            return redirect('/delete_components')
        else:
            componentId = UserComponentPivot.objects.filter(user_id=user).values('component_id_id')
            components = Component.objects.filter(id__in=componentId)
            print('ta ComponentId einai ', componentId, 'kai ta components einai ', components)
            context = {
                'components': components,
                'user': user,
            }
            return render(request, 'warehouse/delete_components.html', context)
        return render(request, 'warehouse/delete_components.html', context)

    @method_decorator(login_required)
    def show_components(self, request):
        components = Component.objects.all()
        users = User.objects.all()
        context = {
            'components': components,
            "users": users,
        }
        print(context)
        return render(request, 'warehouse/show_components.html', context)

    @method_decorator(login_required)
    def componentMenu(self, request):
        if request.method == "POST":
            print("inside the component menu")
            code = request.POST.get("code", False)
            types = request.POST.get("types", False)
            characteristic = request.POST.get("characteristic", False)
            componentSave = Component(code=code, types=types, characteristics=characteristic)
            componentSave.save()
            current_user = request.user.id
            pivotSave = UserComponentPivot(component_id_id=componentSave.id, user_id=current_user)
            pivotSave.save()
            print('to user id einai ', current_user, 'kai to component id einai ', componentSave.id)
            print("print insert components code", code, " type ", types, "characteristic ", characteristic)
            return render(request, 'warehouse/component_menu.html')
        else:
            return render(request, 'warehouse/component_menu.html')

    def show_users(self, request):
        print("eimaste sto show users")
        users_print = User.objects.values()
        print(users_print)
        return render(request, 'warehouse/login.html')

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
                return redirect("/login")
        else:
            return render(request, "warehouse/change_password.html")
        return render(request, "warehouse/change_password.html")
