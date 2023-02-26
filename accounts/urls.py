"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls import path , include
from .custom_views import (
    CustomLoginView,)

from .views import (SignUpView,dashboard,profile,logout_view)

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name = 'login.html',), name='login'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('dashboard/',dashboard, name='dashboard'),
    path('profile/',profile, name='dashboard'),
    path('logout/', logout_view, name='logout'),

]
