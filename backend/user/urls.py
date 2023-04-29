from django.urls import path
from user.views import UserListCreateAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user_list_create'),
]
