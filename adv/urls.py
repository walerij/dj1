from django.urls import path
from .import views


urlpatterns=[
    path("",views.adv_list, name='adv_list')

]