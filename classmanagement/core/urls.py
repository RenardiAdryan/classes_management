from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib import admin
from . import views

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='main'),
    path('<uuid:id>/', views.home, name='main'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('class/<uuid:id>/', views.class_manage, name='class_manage'),
    
    path('student/', views.student, name='student'),
    path('student/manage/<uuid:id>/', views.student_manage, name='student_manage'),

    path('teacher/', views.teacher, name='teacher'),
    path('teacher/manage/<uuid:id>/', views.teacher_manage, name='teacher_manage'),

    path('api/download_classes/', views.download_classes, name='download_classes')
]
