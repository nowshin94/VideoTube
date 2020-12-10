from django.urls import path
from App_Video import views

app_name = 'App_Video'

urlpatterns = [
    path('', views.CategoryList.as_view(), name='video_list'),
    path('search/', views.search, name='search'),
    path('upload/', views.CreateVideo.as_view(), name='create_video'),
    path('details/<slug:slug>', views.video_details, name='video_details'),
    path('liked/<pk>/', views.liked, name='liked_video'),
    path('unliked/<pk>/', views.unliked, name='unliked_video'),
    path('my-videos/', views.MyVideos.as_view(), name='my_videos'),
    path('edit/<pk>/', views.UpdateVideo.as_view(), name='edit_video'),
]