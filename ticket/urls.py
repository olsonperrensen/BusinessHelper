from . import views
from django.urls import path

urlpatterns = [
    # MAKE TICKETS 
    path('', views.CreateView.as_view(), name='homepage'),
    # SUCCESS MESSAGE
    path('ty', views.ty.as_view(), name='ty'),
    # VIEW ALL TICKETS YOU ARE CAPABLE OF SEEING 
    path('list', views.ListView.as_view(), name='list'),
    # VIEW INDIVIDUAL TICKET
    path('<int:pk>', views.DetailView.as_view(), name='one'),
    # UPDATE TICKET
    path('u<int:pk>', views.UpdateView.as_view(), name='update'),
    # DELETE TICKET
    path('d<int:pk>', views.DeleteView.as_view(), name='delete'),
    # SEE ORGANIZATIONAL INFORMATION / HIERARCHY
    path('team', views.TemplateView.as_view(), name='team'),
]
