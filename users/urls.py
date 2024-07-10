from django.urls import path
from .views import (
    user_list,
    user_create,
    user_detail,
    user_update,
    user_delete,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/', user_list, name='user-list'),
    path('users/create/', user_create, name='user-create'),
    path('users/<uuid:pk>/', user_detail, name='user-detail'),
    path('users/<uuid:pk>/update/', user_update, name='user-update'),
    path('users/<uuid:pk>/delete/', user_delete, name='user-delete'),
]
