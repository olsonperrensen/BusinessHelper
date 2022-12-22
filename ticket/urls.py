from . import views
from django.urls import path

urlpatterns = [
    path('', views.CreateView.as_view(), name='homepage'),
    path('ty', views.ty.as_view(), name='ty'),
    path('list', views.ListView.as_view(), name='list'),
    path('<int:pk>', views.DetailView.as_view(), name='one'),
    path('team', views.TemplateView.as_view(), name='team'),
]
