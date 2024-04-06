from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.main,name="Hello my Home"),
    path('about/',views.main1,name="Hello home"),
    path('servise/',views.main2,name="Lorem ipsum"),
]
