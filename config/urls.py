"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from custom_users.views import LoginView, logout_view, SignUpView, home_view, profile_view, CreateProfileView, follow, unfollow, all_users
# from uploads.views import upload_view
from uploads.views import AddPostView, AddComment, delete_comment, post_likes
from community.views import FeedView, DetailPostView, AddCComment, AddCPostView, delete_ccomment, cpost_likes
from notifs.views import notifs_view
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('', home_view, name='homepage'),
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logout_view),
    path('admin/', admin.site.urls),
    # Profile Views
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('profile/<int:user_id>/update/',
         CreateProfileView.as_view(), name='profile_update'),
    path('uploads/', AddPostView, name='uploads'),
    path('community/uploads/', AddCPostView, name='community_uploads'),
    path('community/', FeedView, name='community_feed'),
    path('community/post/<int:pk>/', DetailPostView),
    # all users
    path('users/', all_users, name='users'),
    # Comments
    path('comment/<int:pk>/add', AddComment),
    path('community/comment/<int:pk>/add', AddCComment),
    path('comment/<int:pk>/remove/', delete_comment),
    path('community/comment/<int:pk>/remove/', delete_ccomment),
    #  Likes
    path('uploads-like/<int:pk>/', post_likes),
    path('community/uploads-like/<int:pk>/',
         cpost_likes, name='community_likes'),
    # Follows
    path('follow/<int:user_id>/', follow, name='follow'),
    path('unfollow/<int:user_id>/', unfollow, name='unfollow'),
    # Notifications
    path('notification/', notifs_view, name='notifications')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
