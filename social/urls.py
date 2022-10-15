from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post-detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post-edit/<slug:slug>/', PostEditView.as_view(), name='post-edit'),
    path('post-delete/<slug:slug>/', PostDeleteView.as_view(), name='post-delete'),
]

#humans-are-idiot