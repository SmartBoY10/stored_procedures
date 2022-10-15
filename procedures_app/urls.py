from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('create-page/', CreatePageView.as_view(), name='create_page'),
    path('create/', CreateView.as_view(), name='create'),
    path('update-page/<int:pk>/', UpdatePageView.as_view(), name='update_page'),
    path('update/', UpdateView.as_view(), name='update'),
    path('delete-page/<int:pk>/', DeletePageView.as_view(), name='delete_page'),
    path('delete/', DeleteView.as_view(), name='delete'),
]