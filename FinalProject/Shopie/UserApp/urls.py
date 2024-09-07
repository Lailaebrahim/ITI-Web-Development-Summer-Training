from .views import *
from django.urls import path

urlpatterns = [
    path('signup/', SignUpView, name="signup"),
    path('logout/', LogOutView, name="logout"),
    path('<int:pk>/', UserAccountView.as_view(), name="userAccount"),
    path('update/<int:pk>/', UserUpdateView.as_view(), name="userUpdate"),
    path('delete/<int:pk>', DeleteUserView.as_view(), name="deleteUser"),
]
