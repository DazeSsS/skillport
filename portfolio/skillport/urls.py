from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('create/', CreateProject.as_view(), name='create'),
    path('favorites/', favorites_page, name='favorites'),
    path('like/', set_like, name='like_project'),
]