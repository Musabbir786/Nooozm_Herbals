from django.urls import path
from Home import views


urlpatterns = [
    path('',views.index,name='Home'),
    path('shop',views.shop,name='shop'),
    ]