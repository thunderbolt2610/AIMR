from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add', views.add, name='add'),
    path('doctor', views.doctor, name='doctor'),
    path('details', views.details, name='details'),
    path('docview', views.docview, name='docview')
]
