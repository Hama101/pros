from django.urls import path
from . import views as v

urlpatterns = [
    path('<str:CIN>/', v.index, name='index'),
]
