from django.urls import path
from . import views
from .views import ImageUploadView, ImageListView, An_Image, process_image_to_base64, generate_images_from_text
from .image_generation import get_generated_images, save_image

urlpatterns = [
     
    path('all_images/', ImageListView.as_view(), name='image_list'),
    path('an_image/<int:id>/', An_Image.as_view(), name='an_image'),
    path('generate_image/', views.get_generated_images, name="generate_image"),
    # path('save_image/', ImageUploadView.as_view(), name='upload_image')
    # path('save_image/', views.get_generated_images, name='upload_image')
    
]
