# from .models import *

def friend_button(from_user, to_user):
        friends_request, created = Friends_request.objects.get_or_create(
            from_user=from_user, to_user=to_user
        )
        friends_request, created2 = Friends_request.objects.get_or_create(
            from_user=to_user, to_user=from_user
        )
        print(created)
        print(created2)
        print(1)
        if created and created2:
            Notice.objects.create(usernameFrom=from_user,
                                  usernameTo=to_user, text="подписался на ваши уведомления!")
            Notice.objects.create(usernameFrom=to_user,
                                  usernameTo=from_user, text="теперь в ваших подписках!")
            from_user.notice.add(Notice.objects.filter(usernameFrom=from_user,
                                  usernameTo=to_user, text="подписался на ваши уведомления!")[0])
            to_user.notice.add(Notice.objects.filter(usernameFrom=to_user,
                                  usernameTo=from_user, text="теперь в ваших подписках!")[0])
            Friends_request.objects.get(
                from_user=to_user, to_user=from_user).delete()
            print(1)
            
            return "NewDescription"
        elif created is False and created2:
            Friends_request.objects.get(
                from_user=from_user, to_user=to_user
            ).delete()
            Friends_request.objects.get(
                from_user=to_user, to_user=from_user).delete()
            Notice.objects.create(usernameFrom=from_user,
                                  usernameTo=to_user, text="отписался от Ваc!")
            Notice.objects.create(usernameFrom=to_user,
                                  usernameTo=from_user, text="больше не в Ваших подписках!")
            from_user.notice.add(Notice.objects.filter(usernameFrom=from_user,
                                  usernameTo=to_user, text="отписался от Ваc!")[0])
            to_user.notice.add(Notice.objects.filter(usernameFrom=to_user,
                                  usernameTo=from_user, text="больше не в Ваших подписках!")[0])
            print(1)
            
            return "DelDescription"

        elif created and created2 is False:
            to_user.friends.add(friends_request.from_user)
            from_user.friends.add(friends_request.to_user)
            Notice.objects.create(usernameFrom=from_user,
                                  usernameTo=to_user, text="принял Вашу заявку!")
            Notice.objects.create(usernameFrom=to_user,
                                  usernameTo=from_user, text="добавлен в друзья!")
            from_user.notice.add(Notice.objects.filter(usernameFrom=from_user,
                                  usernameTo=to_user, text="принял Вашу заявку!")[0])
            to_user.notice.add(Notice.objects.filter(usernameFrom=to_user,
                                  usernameTo=from_user, text="добавлен в друзья!")[0])
            print(1)
            
            return "NewFriend"
        else:
            to_user.friends.remove(friends_request.from_user)
            from_user.friends.remove(friends_request.to_user)
            Friends_request.objects.get(
                from_user=from_user, to_user=to_user
            ).delete()
            Friends_request.objects.get(
                from_user=to_user, to_user=from_user).delete()
            Notice.objects.create(usernameFrom=from_user,
                                  usernameTo=to_user, text="удалил Вас из друзей!")
            Notice.objects.create(usernameFrom=to_user,
                                  usernameTo=from_user, text="удален из друзей!")
            from_user.notice.add(Notice.objects.filter(usernameFrom=from_user,
                                  usernameTo=to_user, text="удалил Вас из друзей!")[0])
            to_user.notice.add(Notice.objects.filter(usernameFrom=to_user,
                                  usernameTo=from_user, text="удален из друзей!")[0])
            print(1)
            
            return "DelFriend"
        


    