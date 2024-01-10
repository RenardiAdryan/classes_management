from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('home/<uuid:id>/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('class/<uuid:id>/', views.class_manage, name='class_manage'),
    
    path('student/', views.student, name='student'),
    path('student/manage/<uuid:id>/', views.student_manage, name='student_manage'),

    path('teacher/', views.teacher, name='teacher'),
    path('teacher/manage/<uuid:id>/', views.teacher_manage, name='teacher_manage')
]
