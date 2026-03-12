from django.urls import path
from .views import RegisterView
from .views import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

from django.urls import path
from .views import RegisterView, LoginView, UsersListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UsersListView.as_view(), name='users-list'),  # new endpoint
]