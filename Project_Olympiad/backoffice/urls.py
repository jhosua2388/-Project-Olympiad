from django.urls import path
from backoffice import views
from django.contrib.auth.views import LoginView, LogoutView
from homepage import urls

urlpatterns = [
    path('', views.homeback, name='homeback'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.logout_backoffice, name='logout'),
    path('create_user/', views.create_user, name='create_user'),
    path('indexback/', views.indexback, name='indexback'),
    path('homeback/', views.homeback, name='homeback'),
    path('registro2/', views.create_beneficiario, name='registro2'),
]
