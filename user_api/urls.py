from django.urls import path
from user_api import views

urlpatterns = [
    path('user/', views.UserApiView.as_view()),
]
