from django.urls import path

from . import views

urlpatterns = [
    path('', views.test_ok, name='root-path'),
    path('login/', views.test_ok, name='login-path'),
    path('signup/', views.test_ok, name='signup-path'),
    path('question/<int:id>/', views.test_ok, name='question-id-path'),
    path('ask/', views.test_ok, name='ask-path'),
    path('popular/', views.test_ok, name='popular-path'),
    path('new/', views.test_ok, name='new-path'),
]
