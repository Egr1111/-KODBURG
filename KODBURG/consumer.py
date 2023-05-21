from channels.consumer import AsyncConsumer, StopConsumer, SyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from asgiref.sync import sync_to_async, async_to_sync

from .models import *

import json, time

class MyWebConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def find_newNotice(self, user):
        return len(Notice.objects.filter(usernameTo=user, read=False))

    @database_sync_to_async
    def created1(self, from_user, to_user):
        return len(Friends_request.objects.filter(from_user=from_user, to_user=to_user))

    @database_sync_to_async
    def created2(self, to_user, from_user):
        return len(Friends_request.objects.filter(from_user=from_user, to_user=to_user))

    @database_sync_to_async
    def friendReq_delete(self, from_user, to_user):
        return (
            Friends_request.objects.get(from_user=from_user, to_user=to_user).delete(),
        )
    @database_sync_to_async
    def update_message_viewed(self, UserId, msg):
        return Messages.objects.filter(
            user_from=User.objects.get(id=UserId), message=msg, viewed=False
        ).update(viewed=True)

    @database_sync_to_async
    def room_message_add(self, message, room):
        return room.mes.add(message)
    
    @database_sync_to_async
    def user_new_messages_true(self, user):
        return user.update(new_messages = True)
    
    @database_sync_to_async
    def user_new_messages_false(self, user):
        return user.update(new_messages = False)
    
    @database_sync_to_async
    def get_message(self, user_from, message, room):
        return Messages.objects.filter(user_from=user_from, message=message, room=room)[len(Messages.objects.filter(user_from=user_from, message=message, room=room)) - 1]
    @database_sync_to_async
    def notice_last(self, from_user, to_user, text):
        return Notice.objects.filter(
            usernameFrom=from_user, usernameTo=to_user, text=text
        )[
            len(
                Notice.objects.filter(
                    usernameFrom=from_user, usernameTo=to_user, text=text
                )
            )
            - 1
        ]

    @database_sync_to_async
    def user_friend_add(self, from_user, to_user):
        return from_user.friends.add(to_user)

    @database_sync_to_async
    def user_friend_remove(self, from_user, to_user):
        return from_user.friends.remove(to_user)

    @database_sync_to_async
    def user_descriptions_add(self, from_user, to_user):
        return from_user.descriptions.add(to_user)

    @database_sync_to_async
    def user_descriptions_remove(self, from_user, to_user):
        return from_user.descriptions.remove(to_user)

    @database_sync_to_async
    def user_descriptions_len(self, to_user):
        return to_user.descriptions.all().count()

    @database_sync_to_async
    def user_friends_len(self, to_user):
        return to_user.friends.all().count()

    @database_sync_to_async
    def user_descriptions_get(self, to_user):
        return [
            to_user.descriptions.all()[2].username,
            to_user.descriptions.all()[2].id,
            to_user.descriptions.all()[2].image.url,
        ]

    @database_sync_to_async
    def user_friends_get(self, to_user):
        return [
            to_user.friends.all()[2].username,
            to_user.friends.all()[2].id,
            to_user.friends.all()[2].image.url,
        ]
    
    @database_sync_to_async
    def check_req(self, from_user, to_user):
        return len(Requests.objects.filter(user_from=from_user, user_to=to_user))


    @database_sync_to_async
    def user_connections_add(self, from_user, to_user, from_con, to_con):
        return from_user.connections.add(Requests.objects.get(user_from = from_con, user_to = to_con)), to_user.connections.add(Requests.objects.get(user_from = from_con, user_to = to_con))
    
    @database_sync_to_async
    def user_notice_add(self, from_user, notice):
        return from_user.notice.add(notice)
    
    
    @database_sync_to_async
    def blog_like_list(self, blog):
        return list(blog.like.all())
    
    @database_sync_to_async
    def blog_dislike_list(self, blog):
        return list(blog.dislike.all())
    
    @database_sync_to_async
    def blog_like_remove(self, form_user, blog):
        return blog.like.remove(form_user)
    
    @database_sync_to_async
    def blog_like_add(self, form_user, blog):
        return blog.like.add(form_user)
    
    @database_sync_to_async
    def blog_dislike_remove(self, form_user, blog):
        return blog.dislike.remove(form_user)
    
    @database_sync_to_async
    def blog_dislike_add(self, form_user, blog):
        return blog.dislike.add(form_user)
    
    
    @database_sync_to_async
    def project_like_list(self, project):
        return list(project.like.all())
    
    @database_sync_to_async
    def project_dislike_list(self, project):
        return list(project.dislike.all())
    
    @database_sync_to_async
    def project_like_add(self, form_user, project):
        return project.like.add(form_user)
    
    @database_sync_to_async
    def project_like_remove(self, form_user, project):
        return project.like.remove(form_user)
    
    @database_sync_to_async
    def project_dislike_add(self, form_user, project):
        return project.dislike.add(form_user)
    
    @database_sync_to_async
    def project_dislike_remove(self, form_user, project):
        return project.dislike.remove(form_user)


    @database_sync_to_async
    def user_all(self):
        return list(User.objects.all())
    
    
    async def connect(self):
        if self.scope["user"].is_authenticated:
            self.group_name = self.scope["url_route"]["kwargs"]["room_name"]
            await self.channel_layer.group_add(self.group_name, self.channel_name)

            print("New websocket connect...")
            await self.accept()
            if self.group_name == f"TotalConsumer-{self.scope['user'].id}" and "." not in self.group_name:
                if await self.find_newNotice(self.scope["user"]) > 0:
                    await self.channel_layer.group_send(
                        self.group_name,
                        (
                            {
                                "type": "new.notice",
                                "new_notice": True,
                                "msg_data": {"user_from": self.scope["user"].username},

                            }
                        ),
                    )
                else:
                    await self.channel_layer.group_send(
                        self.group_name,
                        (
                            {
                                "type": "new.notice",
                                "new_notice": False,
                                "msg_data": {"user_from": self.scope["user"].username},

                            }
                        ),
                    )
            
            elif self.group_name != f"TotalConsumer-{self.scope['user'].id}" and "." not in self.group_name:
                to_user = await database_sync_to_async(User.objects.get)(pk = self.group_name.split("-")[1])

    async def receive(self, text_data=None, bytes_data=None):
        if self.scope["user"].is_authenticated:
            if (
                "TotalConsumer" in self.group_name.split("-")
                and "." not in self.group_name
            ):
                type_notice = json.loads(text_data)["type"]
                print(type_notice)
                

                if type_notice == "request_notice":
                    await self.channel_layer.group_send(
                        self.group_name,
                        (
                            {
                                "type": "request.notice",
                                "request_id": self.scope["user"].id,
                            }
                        ),
                    )
                elif type_notice == "request_msg":
                    text = json.loads(text_data)
                    await self.channel_layer.group_send(
                        self.group_name,
                        ({"type": "request.connect", "message": json.loads(text_data)}),
                    )
                elif type_notice == "new_client":
                    from_user = await database_sync_to_async(User.objects.get)(id = json.loads(text_data)["id_from"])
                    to_user = self.scope["user"]
                    if await self.check_req(from_user, to_user) != 0:
                        await self.user_connections_add(from_user, to_user, from_user, to_user)
                        await self.user_connections_add(to_user, from_user, from_user, to_user)
                    elif await self.check_req(to_user, from_user) != 0:
                        await self.user_connections_add(from_user, to_user, to_user, from_user)
                        await self.user_connections_add(to_user, from_user, to_user, from_user)
                
                elif type_notice == "like":
                    text = json.loads(text_data)
                    user = self.scope["user"]
                    if text["type_post"] == "project":
                        project = await database_sync_to_async(Project_list.objects.get)(id = text["id"])
                        list = self.project_like_list(project)
                        print(list)
                        if user in await self.project_like_list(project):
                            await self.project_like_remove(user, project)

                        elif user in await self.project_dislike_list(project):
                            await self.project_dislike_remove(user, project)
                            await self.project_like_add(user, project)
                        
                        else:
                            await self.project_like_add(user, project)
                    elif text["type_post"] == "blog":
                        blog = await database_sync_to_async(Blog_list.objects.get)(id = text["id"])
                        if user in await self.blog_like_list(blog):
                            await self.blog_like_remove(user, blog)

                        elif user in await self.blog_dislike_list(blog):
                            await self.blog_dislike_remove(user, blog)
                            await self.blog_like_add(user, blog)
                        
                        else:
                            await self.blog_like_add(user, blog)
                elif type_notice == "dislike":
                    text = json.loads(text_data)
                    user = self.scope["user"]
                    if text["type_post"] == "project":
                        project = await database_sync_to_async(Project_list.objects.get)(id = text["id"])
                        
                        if user in await self.project_dislike_list(project):
                            
                            await self.project_dislike_remove(user, project)

                        elif user in await self.project_like_list(project):
                            await self.project_like_remove(user, project)
                            await self.project_dislike_add(user, project)
                        
                        else:
                            await self.project_dislike_add(user, project)
                            
                    elif text["type_post"] == "blog":
                        blog = await database_sync_to_async(Blog_list.objects.get)(id = text["id"])
                        if user in await self.blog_dislike_list(blog):
                            await self.blog_dislike_remove(user, blog)

                        elif user in await self.blog_like_list(blog):
                            await self.blog_like_remove(user, blog)
                            await self.blog_dislike_add(user, blog)
                        
                        else:
                            await self.blog_dislike_add(user, blog)
                elif type_notice == "search":
                    text = json.loads(text_data)["text"]
                    list = await self.user_all()
                    results = {}
                    print(text)
                    
                    for i in list:
                        if text in i.username and i.username != self.scope["user"].username:
                            print(text, i.username)
                            results[i.id] = [i.username, f"{i.image}"]

                    await self.channel_layer.group_send(
                        self.group_name,
                        (
                            {
                                "type": "return.search",
                                "message": results,
                            }
                        ),
                    )
                    
                    
                # elif type_notice == "chat_notice":
                #     from_user = await database_sync_to_async(User.objects.get)(id = json.loads(text_data)["id_from"])
                #     to_user = self.scope["user"]
                #     if 
                #     await self.user_chat_add(from_user, to_user, from_user, to_user)
                #     await self.user_chat_add(to_user, from_user, from_user, to_user)
                    
            elif self.scope["user"].username in self.group_name.split("."):
                if json.loads(text_data)["user_from"] != "":
                    room = await database_sync_to_async(Room.objects.get)(
                        title=self.group_name
                    )
                    user_from = await database_sync_to_async(User.objects.get)(
                        username=json.loads(text_data)["user_from"]
                    )
                    user_to = await database_sync_to_async(User.objects.get)(
                        username=json.loads(text_data)["user_to"]
                    )
                    
                    message = json.loads(text_data)["msg"]
                    await sync_to_async(Messages.objects.create)(
                        user_from=user_from, message=message, room=room
                    )
                    
                    await self.user_new_messages_true(user_from)
                    await self.user_new_messages_true(user_to)
                    
                    
                    # mes = await self.get_message(user_from=user_from, message=message, room=room)
                    # await self.room_message_add(mes, room)
                    
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        "type": "chat.message",
                        "message": json.loads(text_data),
                    },
                )
            elif ".web." in self.group_name:
                type_notice = json.loads(text_data)["type"]
                if type_notice == "Friend":
                    from_user = await database_sync_to_async(User.objects.get)(
                        pk=json.loads(text_data)["id_from"]
                    )
                    to_user = await database_sync_to_async(User.objects.get)(
                        pk=json.loads(text_data)["id_to"]
                    )
                    created1 = await self.created1(from_user, to_user)
                    created2 = await self.created2(from_user, to_user)

                    if created1 != 0 and created2 != 0:
                        await sync_to_async(Notice.objects.create)(
                            usernameFrom=from_user,
                            usernameTo=to_user,
                            text="удалил Вас из друзей!",
                        ),
                        await sync_to_async(Notice.objects.create)(
                            usernameFrom=to_user,
                            usernameTo=from_user,
                            text="удален из друзей!",
                            read=True,
                        ),

                        await self.friendReq_delete(from_user, to_user)

                        last_to = await self.notice_last(
                            from_user, to_user, "удалил Вас из друзей!"
                        )
                        last_from = await self.notice_last(
                            to_user, from_user, "удален из друзей!"
                        )

                        await self.user_notice_add(to_user, last_to)
                        await self.user_notice_add(from_user, last_from)
                        await self.user_friend_remove(from_user, to_user)
                        await self.user_friend_remove(to_user, from_user)
                        await self.user_descriptions_add(to_user, from_user)

                        friend_from = ""
                        friend_to = ""

                        if await self.user_friends_len(from_user) >= 3:
                            friend_from = await self.user_friends_get(from_user)
                            print(friend_from)
                        if await self.user_friends_len(to_user) >= 3:
                            friend_to = await self.user_friends_get(to_user)
                            print(friend_to)

                        await self.channel_layer.group_send(
                            self.group_name,
                            (
                                {
                                    "type": "notice.send",
                                    "notice_data": json.loads(text_data),
                                    "notice_from": f"{to_user.username} удален из друзей!",
                                    "notice_to": f"{self.scope['user'].username} удалил Вас из друзей!",
                                    "type_notice": "DelFriend",
                                    "last_description_from": "",
                                    "last_friend_from": friend_from,
                                    "last_description_to": "",
                                    "last_friend_to": friend_to,
                                }
                            ),
                        )

                    elif created1 != 0 and created2 == 0:
                        await sync_to_async(Notice.objects.create)(
                            usernameFrom=from_user,
                            usernameTo=to_user,
                            text="отписался от Вас!",
                        ),
                        await sync_to_async(Notice.objects.create)(
                            usernameFrom=to_user,
                            usernameTo=from_user,
                            text="больше не в Ваших подписках!",
                            read=True,
                        ),

                        await self.friendReq_delete(from_user, to_user)

                        last_to = await self.notice_last(
                            from_user, to_user, "отписался от Вас!"
                        )
                        last_from = await self.notice_last(
                            to_user, from_user, "больше не в Ваших подписках!"
                        )

                        await self.user_notice_add(to_user, last_to)
                        await self.user_notice_add(from_user, last_from)

                        await self.user_descriptions_remove(from_user, to_user)

                        desc_from = ""

                        if await self.user_descriptions_len(from_user) >= 3:
                            desc_from = await self.user_descriptions_get(from_user)
                            print(desc_from)
  
                        await self.channel_layer.group_send(
                            self.group_name,
                            (
                                {
                                    "type": "notice.send",
                                    "notice_data": json.loads(text_data),
                                    "notice_from": f"{to_user.username} больше не в Ваших подписках!",
                                    "notice_to": f"{self.scope['user'].username} отписался от Вас!",
                                    "type_notice": "DelDescription",
                                    "last_description_from": desc_from,
                                    "last_friend_from": "",
                                    "last_description_to": "",
                                    "last_friend_to": "",
                                }
                            ),
                        )
                    elif created1 == 0 and created2 != 0:
                        await sync_to_async(Notice.objects.create)(
                            usernameFrom=from_user,
                            usernameTo=to_user,
                            text="принял Вашу заявку!",
                        ),
                        await sync_to_async(Notice.objects.create)(
                            usernameFrom=to_user,
                            usernameTo=from_user,
                            text="добавлен в друзья!",
                            read=True,
                        ),
                        await sync_to_async(Friends_request.objects.create)(
                            from_user=from_user,
                            to_user=to_user,
                        ),

                        last_to = await self.notice_last(
                            from_user, to_user, "принял Вашу заявку!"
                        )
                        last_from = await self.notice_last(
                            to_user, from_user, "добавлен в друзья!"
                        )

                        await self.user_notice_add(to_user, last_to)
                        await self.user_notice_add(from_user, last_from)
                        await self.user_friend_add(from_user, to_user)
                        await self.user_friend_add(to_user, from_user)
                        await self.user_descriptions_remove(from_user, to_user)
                        await self.user_descriptions_remove(to_user, from_user)

                        desc_to = ""
                        if await self.user_descriptions_len(to_user) >= 3:
                            desc_to = await self.user_descriptions_get(to_user)
                            print(desc_to)

                        await self.channel_layer.group_send(
                            self.group_name,
                            (
                                {
                                    "type": "notice.send",
                                    "notice_data": json.loads(text_data),
                                    "notice_from": f"{to_user.username} добавлен в друзья!",
                                    "notice_to": f"{self.scope['user'].username} принял Вашу заявку!",
                                    "type_notice": "NewFriend",
                                    "last_description_from": "",
                                    "last_friend_from": "",
                                    "last_description_to": desc_to,
                                    "last_friend_to": "",
                                }
                            ),
                        )
                    else:
                        print(await self.user_descriptions_len(from_user))

                        await sync_to_async(Notice.objects.create)(
                            usernameFrom=from_user,
                            usernameTo=to_user,
                            text="подписался на Вас!",
                            read=True,
                        ),
                        await sync_to_async(Notice.objects.create)(
                            usernameFrom=to_user,
                            usernameTo=from_user,
                            text="теперь в ваших подписках!",
                        ),
                        await sync_to_async(Friends_request.objects.create)(
                            from_user=from_user,
                            to_user=to_user,
                        ),

                        last_to = await self.notice_last(
                            from_user, to_user, "подписался на Вас!"
                        )
                        last_from = await self.notice_last(
                            to_user, from_user, "теперь в ваших подписках!"
                        )

                        await self.user_notice_add(to_user, last_to)
                        await self.user_notice_add(from_user, last_from)
                        await self.user_descriptions_add(from_user, to_user)

                        await self.channel_layer.group_send(
                            self.group_name,
                            (
                                {
                                    "type": "notice.send",
                                    "notice_data": json.loads(text_data),
                                    "notice_from": f"{to_user.username} теперь в Ваших подписках!",
                                    "notice_to": f"{self.scope['user'].username} подписался на Вас!",
                                    "type_notice": "NewDescription",
                                    "last_description_from": "",
                                    "last_friend_from": "",
                                    "last_description_to": "",
                                    "last_friend_to": "",
                                }
                            ),
                        )

    async def return_search(self, event):
        await self.send(
            text_data=json.dumps({
                "results": event["message"],
                "type": "results_search"
            })
        )
    
    async def new_notice(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "new_notice": event["new_notice"],
                    "msg_data": event["msg_data"],
                    "type": "check_notice",
                }
            )
        )

    async def request_connect(self, event):
        await self.send(
            text_data=json.dumps({"request": event["message"], "type": "request_chat"})
        )

    async def chat_message(self, event):
        if event["message"]["user_from"] == "":
            await self.update_message_viewed(
                event["message"]["user_read"], event["message"]["msg_id"]
            )
        await self.send(
            text_data=json.dumps({"msg": event["message"], "type": "check_msg"})
        )

    async def notice_send(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "msg_data": event["notice_data"],
                    "msg_from": event["notice_from"],
                    "msg_to": event["notice_to"],
                    "type_notice": event["type_notice"],
                    "last_description_from": event["last_description_from"],
                    "last_description_to": event["last_description_to"],
                    "last_friend_from": event["last_friend_from"],
                    "last_friend_to": event["last_friend_to"],
                    "type": "Friend",
                }
            )
        )

    async def noticeReturn_send(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "msg_data": event["notice_data"],
                    "msg_from": event["notice_from"],
                    "type_notice": event["type_notice"],
                    "last_description_from": event["last_description_from"],
                    "last_friend_from": event["last_friend_from"],
                    "type": "Friend",
                }
            )
        )

    async def request_notice(self, event):
        await self.send(
            text_data=json.dumps(
                {"request_id": event["request_id"], "type": "new_client"}
            )
        )
    
    async def request_req(self, event):
        await self.send(text_data=json.dumps({
            "msg_data": event["msg_data"],
            "type": "request_req"
        }))


    async def disconnect(self, code):
        # if self.group_name != "TotalConsumer-" + f"{self.scope['user'].id}" and "." not in self.group_name:
        #     to_user = await database_sync_to_async(User.objects.get)(pk = self.group_name.split("-")[1])
        #     check_from = await self.check_req(self.scope["user"], to_user)
        #     check_to = await self.check_req(to_user, self.scope["user"])
        #     if check_from:
        #         request = await database_sync_to_async(Requests.objects.get)(user_from = self.scope["user"], user_to = to_user)
        #         if not request.onl_from and not request.onl_to:
        #             await self.connection_del(self.scope["user"], to_user)
        #     elif check_to:
        #         request = await database_sync_to_async(Requests.objects.get)(user_from = to_user, user_to = self.scope["user"])
        #         if not request.onl_from and not request.onl_to:
        #             await self.connection_del(to_user, self.scope["user"])
            
        print("New websocket disconnect...", code)
