from django.urls import path
from gallery.views import ImageListCreateView, ImageDeleteView

urlpatterns = [
    path('images/', ImageListCreateView.as_view(), name='image-list-create'),
    path('images/<int:pk>/', ImageDeleteView.as_view(), name='image-delete'),
]