from django.urls import path

from .views import HomeView, ArticleDetailView, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', AddPostView.as_view(), name='create_post'),
    path('edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete_post')

]
