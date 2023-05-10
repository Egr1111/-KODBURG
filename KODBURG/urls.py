from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome.as_view(), name="welcome"),
    path('main_blog/', views.main_blog, name="main_blog"),
    path('main_project/', views.main_project, name="main_project"),
    path('enter/', views.Enter.as_view(), name="enter"),
    path('profile/', views.update_profile, name="profile"),
    path('exit/', views.LogoutView.as_view(template_name="KODBURG/welcomeBack.html"), name="exit"),
    path('main/my_blog/', views.my_blog, name="my_blog"),
    path("main/friends", views.My_friends.as_view(), name="my_friends"),
    path("main/my_notice", views.My_notice.as_view(), name="my_notice"),
    path('main/my_blog/create_blog/', views.add_blog, name="add_blog"),
    path('main/my_blog/<str:username>/<int:pk>/update',
         views.Update_blog.as_view(), name="update_blog"),
    path('main/my_blog/<str:username>/<int:pk>/delete',
         views.Delete_blog.as_view(), name="delete_blog"),
    path('main/my_projects/', views.my_project, name="my_projects"),
    path('main/my_projects/create_project/',
         views.add_project, name="add_project"),
    path('main/my_projects/<str:username>/<int:pk>/update',
         views.Update_project.as_view(), name="update_project"),
    path('main/my_projects/<str:username>/<int:pk>/delete',
         views.Delete_project.as_view(), name="delete_project"),
    path('main/reach', views.Reach.as_view(), name="reach"),
    path('main/<str:username>/<int:userID>/viewing/',
         views.other_user, name="other_user"),
    path('main/messager', views.messager, name="messager"),
    
    path("main/chat/create/<str:user_from>/<str:user_to>/", views.create_chat, name="create_chat"),
    path("main/chat/<int:user_from><int:user_to>/", views.chat , name="chat"),
    
    path('increase_counterBlog/<int:pk>/',
         views.IncreaseCounterBlog, name='likeIncBlog'),
     path('down_counterBlog/<int:pk>', views.DownCounterBlog, name="likeDelBlog"),
     path('increase_discounterBlog/<int:pk>', views.IncreaseCounterDisBlog, name='dislikeIncBlog'),
    path('down_discounterBlog/<int:pk>', views.DownCounterDisBlog, name='dislikeDelBlog'),
    
    path('increase_counterProject/<int:pk>/',
         views.IncreaseCounterProject, name='likeIncProject'),
    path('down_counterProject/<int:pk>', views.DownCounterProject, name="likeDelProject"),
    path('increase_discounterProject/<int:pk>',
         views.IncreaseCounterDisProject, name='dislikeIncProject'),
    path('down_discounterProject/<int:pk>',
         views.DownCounterDisProject, name='dislikeDelProject')
    
    

]
