from django.urls import path
from .views import A_page, All_pages

urlpatterns = [
    path('a_page/<int:id>/', A_page.as_view(), name='a_page'),
    path('all_pages/', All_pages.as_view(), name='all_pages')
]