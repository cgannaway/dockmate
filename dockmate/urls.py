"""dockmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from dockmate.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import include, path
from users import views as userviews
from django.contrib.auth import views as authviews
from tickets import views as ticketviews
from django.conf import settings
from django.conf.urls.static import static

#list of urls. format: url path, view class/function from views.py file, name
urlpatterns = [
    path('', include('tickets.urls')), #extends this list to tickets/urls.py
    path('admin/', admin.site.urls),
    path('register/', userviews.register, name="register"),
    path('login/', authviews.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', authviews.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/', userviews.profile, name="profile"),
    path('employees/', userviews.ListEmployees.as_view(), name='list-employees'),
    path('company/', userviews.CompanyView.as_view(), name='company'),
    path('company/new/', userviews.CreateCompany.as_view(), name='create-company')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)