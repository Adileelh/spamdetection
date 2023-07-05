
from django.urls import path

from . import views

urlpatterns = [

    path('single_predict/', views.single_predict, name='single_predict'),
    path('bulk_predict/', views.bulk_predict, name='bulk_predict'),
]