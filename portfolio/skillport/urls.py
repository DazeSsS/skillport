from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('feed/', feed_page, name='feed'),
    path('project/<str:pk>/', project, name='project'),
]