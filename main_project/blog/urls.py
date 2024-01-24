
from django.urls import path , include 
from .views import   (  BlogPostListApiView, BlogPostDetailApiView)


urlpatterns = [
    path('blog/', BlogPostListApiView.as_view()),
    path('blog/<int:id>/', BlogPostDetailApiView.as_view())
    
]
