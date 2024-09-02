from .views import *
from django.urls import path

urlpatterns = [
    path('signup/', SignUpView, name="signup"),
    path('logout/', LogOutView, name="logout"),
    path('account/<int:pk>/', AccountView.as_view(), name="account"),
    path('account/delete/', AccountDeleteView, name="account_delete"),
    path('account/update/', UserProfileUpdateView.as_view(), name="accountUpdate"),
    path('projects/', UserProjectsView.as_view(), name="userprojects"),
    path('contributers/', UserContributersView.as_view(), name="usercontributers"),
    path('technologies/', UserTechnologiesView.as_view(), name='usertechnologies')
]
