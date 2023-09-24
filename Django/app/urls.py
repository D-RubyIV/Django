from django.urls import path
from app import views
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from app import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

# router = DefaultRouter()
# router.register(r'products', Product)



urlpatterns = [
    path('', views.redirectPage, name='home'),
    path('home/', views.homeView, name='home'),
    path('document/', views.documentView, name='document'),
    path('signin/', views.signinView, name='signin'),
    path('signup/', views.signupView, name='signup'),
    path('logout/', views.logoutView, name='logout'),
    path('captcha/', views.captchaView, name='captcha'),
    path('is_authenticated/', views.check_authenticated, name='logout'),
    path('ajax/get_data/', views.get_data, name='get_data'),
    path('fetchtest/', views.test_fetch, name='fetchtest'),

]

if not settings.DEBUG: 
    urlpatterns += [
        re_path(r'^images/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)