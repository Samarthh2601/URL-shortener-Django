from django.urls import path

from . import views

urlpatterns = [
    path('', views.gen_url, name='generate-url'),
    path('api/', views.api_shortener, name='api-shortener'),
    path('docs/', views.api_docs, name='docs'),
    path('about/', views.about, name='about'),
    path('<short_url>/', views.redirect_url, name='redirect-url'),
]
