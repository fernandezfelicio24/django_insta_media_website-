from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, ProfileView, ProfileEditView, AddFollower, RemoveFollower, AddLike, AddDisLike, UserSearch

urlpatterns = [

    path('', PostListView.as_view(), name='post-list'),
    path('post-detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post-edit/<slug:slug>/', PostEditView.as_view(), name='post-edit'),
    path('post-delete/<slug:slug>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/comment/delete/<int:pk>/ ', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDisLike.as_view(), name='dislike'),

    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile-edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('search/', UserSearch.as_view(), name='profile-search'),
]

