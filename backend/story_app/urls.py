from django.urls import path
from .views import A_Story, All_Stories, generate_story_from_words
from . import views

urlpatterns = [
    path('a_story/', A_Story.as_view(), name='a_story'),
    path('all_stories/', All_Stories.as_view(), name='all_stories'),
    path('generate_story/', views.generate_story_from_words, name='generate_story')
]