from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('feed/', views.feed_page, name='feed'),
    path('project/<str:pk>/', views.project, name='project'),
]