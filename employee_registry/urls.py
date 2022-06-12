from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='list'),
    path('update/<int:id>/', views.update_employee, name='update'),
    path('form/', views.employeeAdd, name='form'),
    path('employee/<int:id>/', views.employeeView, name='view'),
    path('delete/<int:id>/', views.employeeDelete, name='delete'),
    path('search_employee/ ', views.search_Employee, name='search_employee'),
]
