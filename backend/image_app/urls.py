from django.urls import path
from .views import ImageUploadView, ImageListView, An_Image

urlpatterns = [
    path('upload_image/', ImageUploadView.as_view(), name='upload_image'),
    path('all_images/', ImageListView.as_view(), name='image_list'),
    path('an_image/<int:id>/', An_Image.as_view(), name='an_image')
]