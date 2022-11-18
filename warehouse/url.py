from django.urls import path
from . import views
from warehouse.views import WarehouseView

objectHome = WarehouseView()
urlpatterns = [
    path("", objectHome.Index, name="index"),
    path("show_components/", objectHome.Show_components, name="show_component"),
    path("sign_up/", objectHome.SignUp, name="sign_up"),
    path("components/", objectHome.ComponentMenu, name="components"),
    path("login/",objectHome.Login,name="login")
]


