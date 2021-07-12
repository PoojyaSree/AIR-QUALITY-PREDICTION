from django.urls import path,include
from AQ import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('predict', views.predict, name='predict'),
    
]