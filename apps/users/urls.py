from django.contrib.auth import get_user_model
from django.urls import path
from django.urls.conf import include

from apps.users import views

User = get_user_model()

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('captcha/', include('captcha.urls')),
    path('users_admin/', views.users_admin, name='admin'),
]
