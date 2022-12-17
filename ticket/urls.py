from . import views
from django.urls import path

urlpatterns = [
    path('',views.OView.as_view(),name='index'),
    path('ty',views.ty,name='ty')
]
