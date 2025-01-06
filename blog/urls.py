from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),  # Route for the homepage
]

#urlpatterns = [
#    path('posts/', views.PostList.as_view(), name='home'),
#]