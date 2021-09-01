from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.views.generic import TemplateView
from .views import BlogHomeView
from . import views

urlpatterns = [
    url(r'^blog/', include(('blog.urls','blog'), namespace='artikel')),
    path('admin/', admin.site.urls),
    url(r'^$', BlogHomeView.as_view(), name='home'),
    path('signup/',views.signup, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout')
]
