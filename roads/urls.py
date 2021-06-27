from django.urls import path
from . import views as road_views

app_name = "roads"

urlpatterns = [
    path("", road_views.road_page, name="road_page"),
]