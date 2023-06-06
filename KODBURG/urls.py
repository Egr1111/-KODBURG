from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome.as_view(), name="welcome"),
    path('enter/', views.Enter.as_view(), name="enter"),
    path('profile/', views.update_profile, name="profile"),
    path('exit/', views.LogoutView.as_view(template_name="KODBURG/welcomeBack.html"), name="exit"),
    path('email_confirm/<str:email_hash>/<str:username>/', views.emailConfirm, name="email_confirm"),
    path('email_send_confirm/<str:email>/', views.email_send_confirm, name="email_send_confirm"),
    path('password_change/<str:password_hash>/<str:username>/', views.passwordChange, name="password_change"),
    path('password_change_confirm/<str:email>/', views.password_send_change, name="password_change_confirm"),
    path('lost_user/', views.search_lost_user, name="search_lost_user"),
    
    path('main_blog/', views.main_blog, name="main_blog"),
    path('main_project/', views.main_project, name="main_project"),
    path('main_blog/<int:id>/details/', views.blog_details, name = "blog_details"),
    path('main_project/<int:id>/details/', views.project_details, name = "project_details"),
    path('main/my_blog/', views.my_blog, name="my_blog"),
    path("main/friends", views.My_friends.as_view(), name="my_friends"),
    path("main/my_notice", views.My_notice.as_view(), name="my_notice"),
    path('main/my_blog/create_blog/', views.add_blog, name="add_blog"),
    path('main/my_blog/<str:username>/<int:pk>/update',
         views.Update_blog.as_view(), name="update_blog"),
    path('main/my_blog/<str:username>/<int:pk>/delete',
         views.Delete_blog.as_view(), name="delete_blog"),
    path('main/my_projects/', views.my_project, name="my_projects"),
    path('main/descriptions/', views.My_descriptions.as_view(), name="my_descriptions"),
    path('main/my_projects/create_project/',
         views.add_project, name="add_project"),
    path('main/my_projects/<str:username>/<int:pk>/update',
         views.Update_project.as_view(), name="update_project"),
    path('main/my_projects/<str:username>/<int:pk>/delete',
         views.Delete_project.as_view(), name="delete_project"),
    path('main/search', views.Search.as_view(), name="search"),
    path('main/<str:username>/<int:userID>/viewing/',
         views.other_user, name="other_user"),
    path('main/messager', views.messager, name="messager"),
    
    path("main/chat/create/<str:user_from>/<str:user_to>/", views.create_chat, name="create_chat"),
    path("main/chat/<int:user_from>/<int:user_to>/", views.chat , name="chat"),
]
