from django.urls import path
from .import views

urlpatterns=[
    path('',views.loginaction,name='loginaction'),
    path('templates/student_rege',views.StudentRege,name='StudentRege'),
    path('templates/dashboard',views.dash,name='dash'),
    path('templates/admin',views.admin,name='admin'),
    path('templates/totalStudents',views.totalStudents,name='totalStudents'),
    path('templates/Presentees',views.Presentees,name='Presentees'),
    path('templates/Absentees',views.Absentees,name='Absentees'),
    path('templates/Attendence',views.Attendence,name='Attendence'),
]