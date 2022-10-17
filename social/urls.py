from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post-detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post-edit/<slug:slug>/', PostEditView.as_view(), name='post-edit'),
    path('post-delete/<slug:slug>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/comment/delete/<int:pk>/ ', CommentDeleteView.as_view(), name='comment-delete'),
]

#humans-are-idiot