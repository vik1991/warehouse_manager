from django.urls import path, include
from . import views
from warehouse.views import WarehouseView

objectHome = WarehouseView()
urlpatterns = [
    path("", objectHome.Index, name="index"),
    path("show_components/", objectHome.show_components, name="show_component"),
    path("sign_up/", objectHome.signUp, name="sign_up"),
    path("components/", objectHome.componentMenu, name="component_create"),
    path("components/<int:user_id>/", objectHome.componentMenu, name="component"),
    path("login/",objectHome.login,name="login")
]


