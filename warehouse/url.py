from django.urls import path, include
from . import views
from warehouse.views import WarehouseView

objectHome = WarehouseView()
urlpatterns = [
    path("", objectHome.Index, name="index"),
    path("show_components/", objectHome.show_components, name="show_components"),
    path("show_component/", objectHome.show_component, name="show_component"),
    path("delete_components/", objectHome.delete_components, name="delete_components"),
    path("sign_up/", objectHome.signUp, name="sign_up"),
    path("components/", objectHome.componentMenu, name="componentMenu"),
    path("login/",objectHome.login_user,name="login_user"),
    path("show_users/",objectHome.show_users, name="show_users"),
    path("logout_view/",objectHome.logout_view, name="logout_view"),
    path("change_pass/",objectHome.change_password, name ="change_password"),
    path("edit_component/",objectHome.edit_component, name="edit_copmponent"),
]


