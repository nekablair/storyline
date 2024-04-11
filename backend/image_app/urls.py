from django.urls import path
from . import views
from .views import ImageUploadView, ImageListView, An_Image
from .image_generation import get_generated_images

urlpatterns = [
    path('upload_image/', ImageUploadView.as_view(), name='upload_image'),
    path('all_images/', ImageListView.as_view(), name='image_list'),
    path('an_image/<int:id>/', An_Image.as_view(), name='an_image'),
    path('generate_image/', views.get_generated_images, name="generate_image")
    
]
