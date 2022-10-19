from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import  PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, ProfileView, ProfileEditView

urlpatterns = [

    path('', PostListView.as_view(), name='post-list'),
    path('post-detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post-edit/<slug:slug>/', PostEditView.as_view(), name='post-edit'),
    path('post-delete/<slug:slug>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/comment/delete/<int:pk>/ ', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile-edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
]

