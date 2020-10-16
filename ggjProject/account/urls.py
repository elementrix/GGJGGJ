from django.urls import path
from .views import signup, login, logout
urlpatterns = [
    path('back_signup/', signup, name='back_signup'),
    path('back_login/', login, name='back_login'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]