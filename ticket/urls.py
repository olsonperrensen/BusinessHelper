from . import views
from django.urls import path

urlpatterns = [
    path('', views.CreateView.as_view(), name='homepage'),
    path('ty', views.ty, name='ty'),
    path('list',views.ListView.as_view(),name='list')
]
