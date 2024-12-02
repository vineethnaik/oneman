from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('pagedividecall/', views.pagedividecall, name='pagedividecall'),
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/', views.excpetionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/', views.exceptionapagelogic, name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    path('log_out/', views.log_out, name='log_out'),
    path('user_login/', views.user_login, name='user_login'),
    path('get_time_details/', views.get_time_details, name='get_time_details'),
    path('calculate_future_date/', views.calculate_future_date, name='calculate_future_date'),
    path('AddStudent/', views.add_student, name='AddStudent'),
    path('student_list/', views.student_list, name='student_list'),
    path('generate/', views.upload_file, name='upload_file'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('search_contacts/', views.search_contacts, name='search_contacts'),

]