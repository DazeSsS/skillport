from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('profile/<int:user_id>', another_profile_page, name='another_profile'),
    path('create/', CreateProject.as_view(), name='create'),
    path('favorites/', favorites_page, name='favorites'),
    path('project/<uuid:project_id>', project_page, name='project'),
    path('like/', set_like, name='like_project'),
    path('subscribe/<uuid:project_id>', subscribe_from_project, name='subscribe_from_project'),
    path('subscribe/', subscribe, name='subscribe'),
    path('subscriptions/', subscriptions_page, name='subscriptions'),
]