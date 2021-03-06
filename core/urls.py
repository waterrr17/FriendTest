from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_start, name='test_start'),
    path('guess/', views.guess, name='guess'),
    path('test/end/<int:id>/', views.test_end, name='test_end'),
    path('new/test/', views.new_test, name='new_test')
]