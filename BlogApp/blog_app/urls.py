from django.urls import path, re_path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/delete/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
]

