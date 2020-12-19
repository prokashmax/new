from django.urls import path
from . import views

# app_name = portfolio

urlpatterns =[
    path('', views.index , name='home'),
    path('<int:pot_id>/', views.pot_view, name='pot'),
    path('base/', views.base , name='base'),
]