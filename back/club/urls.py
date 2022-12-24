"""back URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    # user
    path('login_user', views.loginUser),
    path('register_user', views.registerUser),
    path('update_user_information', views.updateUserInformation),
    path('get_user_information', views.getUserInformation),
    path('modify_password', views.modifyPassword),
    path('update_avatar', views.updateAvatar),
    # club
    path('create_club', views.createClub),
    path('handle_create_club', views.handleCreateClub),
    path('get_unhandled_clubs', views.getUnhandledClubs),
    path('get_all_clubs', views.getAllClubs),
    path('change_position', views.changePosition),
    path('find_club', views.findClub),
    path('get_club_list', views.getClubList),
    path('get_one_club', views.getOneClub),
    path('get_master_club_list', views.getMasterClubList),
    path('get_club_members', views.getClubMembers),
    path('get_club_events', views.getClubEvents),
    path('get_club_notices', views.getClubNotices),
    path('get_club_requests', views.getClubRequests),
    path('handle_joining_club', views.handleJoiningClub),
    path('join_club', views.joinClub),
    path('join_club_bulk', views.joinClubBulk),
    path('quit_club', views.quitClub),
    path('rate_club_star', views.rateClubStar),
    path('modify_club_info', views.modifyClubInfo),
    # event
    path('create_event', views.createEvent),
    path('handle_create_event', views.handleCreateEvent),
    path('get_unhandled_events', views.getUnhandledEvents),
    path('participate_event', views.participateEvent),
    path('like_event', views.likeEvent),
    # message
    path('delete_message', views.deleteMessage),
    path('delete_all_messages', views.deleteAllMessages),
    path('get_messages', views.getMessages),
    # post
    path('get_club_posts', views.getClubPosts),
    path('publish_post', views.publishPost),
    path('like_post', views.likePost),
    path('like_reply', views.likeReply),
    path('delete_post', views.deletePost),
    path('delete_reply', views.deleteReply),
    path('reply_post', views.replyPost),
    path('get_post_replied', views.getPostReplies),
    path('get_one_post', views.getOnePost),
    # others
    path('handle_following', views.handleFollowing),
    path('handle_unfollowing', views.handleUnfollowing),
    path('publish_notice', views.publishNotice),
    path('delete_notice', views.deleteNotice),
    path('get_logs', views.getLogs)
]
