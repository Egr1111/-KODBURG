import random
import socket
import string
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
    TemplateView,
    ListView,
    CreateView,
)

from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import check_password, make_password





class Welcome(CreateView):
    form_class = UserCreateForm
    template_name = "KODBURG/welcome.html"
    success_url = reverse_lazy("enter")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Post.objects.all()
        return context


class Enter(LoginView):
    template_name = "KODBURG/enter.html"
    form_class = UserLoginForm
    success_url = "/main_blog"


def main_blog(request):
    form_blog = Comments_to_blog()
    if request.method == "POST":
        form_blog = Comments_to_blog(request.POST, request.FILES)
        if form_blog.is_valid():
            form_blog = form_blog.save(commit=False)
            form_blog.author = request.user
            form_blog.save()
            return redirect("main_blog")
    return render(
        request,
        "KODBURG/main_blog.html",
        {
            "blog": Blog_list.objects.order_by("-date"),
            "comments_blog": Comment_blog.objects.order_by("-date"),
            "form_blog": form_blog,
        },
    )


def main_project(request):
    form_project = Comments_to_projects()

    if request.method == "POST":
        form_project = Comments_to_projects(request.POST, request.FILES)
        if form_project.is_valid():
            form_project = form_project.save(commit=False)
            form_project.author = request.user
            form_project.save()
            return redirect("main_project")

    return render(
        request,
        "KODBURG/main_project.html",
        {
            "projects": Project_list.objects.order_by("-date"),
            "comments_project": Comment_project.objects.order_by("-date"),
            "form_project": form_project,
        },
    )


def blog_details(request, id):
    if len(Blog_list.objects.filter(id=id)) == 0:
        return redirect(request.META.get("HTTP_REFERER"))
    blog = Blog_list.objects.get(id=id)
    comments = Comment_blog.objects.filter(blog=blog)
    print(comments)
    comments_form = Comments_to_blog()

    if request.method == "POST":
        comments_form = Comments_to_blog(request.POST, request.FILES)
        if comments_form.is_valid():
            comments_form = comments_form.save(commit=False)
            comments_form.author = request.user
            comments_form.save()
            return redirect("blog_details", id)
    return render(
        request,
        "KODBURG/blog_details.html",
        {"i": blog, "comments_blog": comments, "form_blog": comments_form},
    )


def project_details(request, id):
    if len(Project_list.objects.filter(id=id)) == 0:
        return redirect(request.META.get("HTTP_REFERER"))
    project = Project_list.objects.get(id=id)
    comments = Comment_project.objects.filter(project=project)
    comments_form = Comments_to_projects()
    if request.method == "POST":
        comments_form = Comments_to_projects(request.POST, request.FILES)
        if comments_form.is_valid():
            comments_form = comments_form.save(commit=False)
            comments_form.author = request.user
            comments_form.save()
            return redirect("project_details", id)
    return render(
        request,
        "KODBURG/project_details.html",
        {"i": project, "comments_project": comments, "form_project": comments_form},
    )


class My_friends(TemplateView):
    template_name = "KODBURG/my_friends.html"


class My_notice(TemplateView):
    template_name = "KODBURG/my_notice.html"


class My_descriptions(TemplateView):
    template_name = "KODBURG/my_descriptions.html"


@login_required
def update_profile(request):
    error = ""
    email_now = request.user.email
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            print(email_now, user_form.data["email"])
            user_form.save()
            if user_form.data["email"] != email_now:
                User.objects.filter(id=request.user.id).update(email_confirm=False)
                print(email_now, user_form.data["email"])
            return redirect("main_blog")
        else:
            error = "Ошибка в заполнении формы"
    else:
        user_form = UserForm(instance=request.user)

    return render(
        request,
        "KODBURG/edit_profile.html",
        {
            "user_form": user_form,
            "error": error,
        },
    )


@login_required
def email_send_confirm(request, email):
    email_hash = make_password(email)
    while "/" in email_hash:
        email_hash = make_password(email)
    print(email_hash)
    User.objects.filter(id=request.user.id).update(email_hash=email_hash)
    try:
        email = EmailMessage(
            "Подтверждение email",
            f"""
                            <html>
                                <div style='display: flex; justify-content: center; text-align: center'>
                                    <h1>Привет, {request.user.username}!</h1>
                                </div>
                                <div style='display: flex; justify-content: center; text-align: center'>
                                    <h3>Перейди по ссылке ниже, чтобы подтвердить, что это ваша почта или проигнорировать это письмо, если понятия не имеете, почему тебе пришло это письмо.</h3>
                                </div>
                                <div style='display: flex; justify-content: center; text-align: center'>
                                    <a href='http://{request.META['HTTP_HOST']}/email_confirm/{email_hash}/{request.user.username}'>Вот по этой ссылке</a>
                                </div>""",
            to=[email],
        )
        email.content_subtype = "html"
        email.send()
        return render(request, "KODBURG/email_send_confirm.html", {"error": False})
    except:
        return render(request, "KODBURG/email_send_confirm.html", {"error": True})



def emailConfirm(request, email_hash, username):
    if not request.user.is_authenticated:
        user = authenticate(username=username)
        if user is not None:
            login(request, user)
            
    if request.user.email_hash == email_hash and request.user.email_hash != "":
            User.objects.filter(id=request.user.id).update(email_confirm=True)
            User.objects.filter(id=request.user.id).update(email_hash="")
            return render(request, "KODBURG/email_confirm.html")


@login_required
def password_send_change(request, email):
    password_hash = make_password(email)
    while "/" in password_hash:
        password_hash = make_password(email)
    print(password_hash)
    User.objects.filter(id=request.user.id).update(password_hash=password_hash)
    try:
        email = EmailMessage(
            "Подтверждение email",
            f"""
                            <html>
                                <div style='display: flex; justify-content: center; text-align: center'>
                                    <h1>Привет, {request.user.username}!</h1>
                                </div>
                                <div style='display: flex; justify-content: center; text-align: center'>
                                    <h3>Перейди по ссылке ниже, чтобы подтвердить, что это твоя почта или проигнорировать это письмо, если понятия не имеете, почему тебе пришло это письмо.</h3>
                                </div>
                                <div style='display: flex; justify-content: center; text-align: center'>
                                    <a href='http://{request.META['HTTP_HOST']}/password_change/{password_hash}/{request.user.username}'>Вот по этой ссылке</a>
                                </div>""",
            to=[email],
        )
        email.content_subtype = "html"
        email.send()
        return render(request, "KODBURG/password_change_confirm.html", {"error": False})
    except:
        return render(request, "KODBURG/password_change_confirm.html", {"error": True})



def passwordChange(request, password_hash, username):
    if not request.user.is_authenticated:
        
        user = User.objects.filter(username = username)
        print(len(user))
        if len(user) != 0:
            print(2)
            login(request, user[0])
    print(3)

    if request.user.password_hash == password_hash and request.user.password_hash != "":
        error = ""
        form = UserPasswordForm()
        if request.method == "POST":
            form = UserPasswordForm(request.POST)
            if form.is_valid():
                # form.save()
                user = User.objects.get(id=request.user.id)
                user.set_password(form.cleaned_data["password"])
                user.save()
                User.objects.filter(id=request.user.id).update(password_hash="")
                return redirect("/profile/")
            else:
                error = "Поле не может быть пустым!"
                return render(
                    request,
                    "KODBURG/password_change.html",
                    {"form": form, "error": error},
                )

        return render(
            request, "KODBURG/password_change.html", {"form": form, "error": error}
        )


def search_lost_user(request):
    error = ""
    user = ""
    form = UserLostForm()
    if request.method == "POST":
        form = UserLostForm(request.POST)

        username = form.data["username"]
        email = form.data["email"]

        if username != "" and email != "":
            user = User.objects.filter(username=username, email=email)
        elif username != "" and email == "":
            user = User.objects.filter(username=username)
        elif email != "" and username == "":
            user = User.objects.filter(email=email)
        else:

            form = UserLostForm()
            error = "Минимум одно поле должно быть заполнено"
            return render(
                request,
                "KODBURG/search_lost_user.html",
                {"form": form, "find_user": user, "error": error},
            )

        if len(user) != 0:
            if user[0].email_confirm:
                password_hash = make_password(user[0].email)
                while "/" in password_hash:
                    password_hash = make_password(user[0].email)
                    
                user.update(password_hash = password_hash)
                email = EmailMessage(
                    "Изменение пароля",
                    f"""<html>
                                <div style='display: flex; justify-content: center; text-align: center'>
                                    <h1>Привет, {user[0].username}!</h1>
                                </div>
                                <div style='display: flex; justify-content: center; text-align: center'>
                                    <h3>Перейди по ссылке ниже, чтобы подтвердить, что это ваша почта или проигнорировать это письмо, если понятия не
                                        имеете, почему тебе пришло это письмо.</h3>
                                </div>
                                <div style='display: flex; justify-content: center; text-align: center'>
                                    <a href='http://{request.META['HTTP_HOST']}/password_change/{password_hash}/{user[0].username}'>Вот по этой ссылке</a>
                                </div>
                            </html>""",
                    to=[user[0].email],
                )
                email.content_subtype = "html"
                email.send()
                return render(
                    request,
                    "KODBURG/search_lost_user.html",
                    {"form": form, "find_user": user[0], "error": error},
                )

            else:
                error = (
                    "У этого ползователя неподтвержден email. Смена пароля невозможна!"
                )
                return render(
                    request,
                    "KODBURG/search_lost_user.html",
                    {"form": form, "find_user": user, "error": error},
                )

        else:
            error = "Такого пользователя нет!"
            return render(
                request,
                "KODBURG/search_lost_user.html",
                {"form": form, "find_user": user, "error": error},
            )

    return render(
        request,
        "KODBURG/search_lost_user.html",
        {"form": form, "find_user": user, "error": error},
    )


def my_blog(request):
    form = Comments_to_blog()
    if request.method == "POST":
        form = Comments_to_blog(request.POST, request.FILES)
        if form.is_valid:
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect("my_blog")

    return render(
        request,
        "KODBURG/my_blog.html",
        {
            "object_list": Blog_list.objects.filter(username=request.user).order_by(
                "-date"
            ),
            "form": form,
            "comments": Comment_blog.objects.order_by("-date"),
        },
    )


def add_blog(request):
    error = ""
    form = Blog_form()
    if request.method == "POST":
        form = Blog_form(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = request.user
            form.save()
            return redirect("my_blog")
        else:
            error = "Форма заполнена неверно!"

    return render(
        request,
        "KODBURG/create_blog.html",
        {
            "form": form,
            "error": error,
        },
    )


class Update_blog(UpdateView):
    model = Blog_list
    form_class = Blog_form
    template_name = "KODBURG/change_blog.html"
    success_url = reverse_lazy("my_blog")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notice"] = Notice.objects.filter(
            usernameTo=self.request.user
        ).order_by("-date")[:3]
        context["Users"] = User.objects.all()
        context["new_notice"] = Notice.objects.filter(
            usernameTo=self.request.user, read=False
        ).order_by("-date")
        return context


class Delete_blog(DeleteView):
    model = Blog_list
    context_object_name = "Blog_list"
    template_name = "KODBURG/delete_blog.html"
    success_url = reverse_lazy("my_blog")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notice"] = Notice.objects.filter(
            usernameTo=self.request.user
        ).order_by("-date")[:3]
        context["Users"] = User.objects.all()
        context["new_notice"] = Notice.objects.filter(
            usernameTo=self.request.user, read=False
        ).order_by("-date")
        return context


def my_project(request):
    form = Comments_to_projects()
    if request.method == "POST":
        form = Comments_to_projects(request.POST, request.FILES)
        if form.is_valid:
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect("my_projects")

    return render(
        request,
        "KODBURG/my_project.html",
        {
            "object_list": Project_list.objects.filter(username=request.user).order_by(
                "-date"
            ),
            "form": form,
            "comments": Comment_project.objects.order_by("-date"),
        },
    )


def add_project(request):
    error = ""
    form = Project_form()
    if request.method == "POST":
        form = Project_form(request.POST, request.FILES)
        if form.is_valid:
            form = form.save(commit=False)
            form.username = request.user
            form.save()
            return redirect("my_projects")
        else:
            error = "Форма заполнена неверно!"

    return render(
        request,
        "KODBURG/create_project.html",
        {
            "form": form,
            "error": error,
        },
    )


class Update_project(UpdateView):
    model = Project_list
    form_class = Project_form
    template_name = "KODBURG/change_project.html"
    success_url = reverse_lazy("my_projects")

    def get_context_data(self, **kwargs):
        error = ""
        context = super().get_context_data(**kwargs)
        context["notice"] = Notice.objects.filter(
            usernameTo=self.request.user
        ).order_by("-date")[:3]
        context["Users"] = User.objects.all()
        context["error"] = error
        context["new_notice"] = Notice.objects.filter(
            usernameTo=self.request.user, read=False
        ).order_by("-date")
        return context


class Delete_project(DeleteView):
    model = Project_list
    context_object_name = "Project_list"
    template_name = "KODBURG/delete_project.html"
    success_url = "/main/my_projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notice"] = Notice.objects.filter(
            usernameTo=self.request.user
        ).order_by("date")[:3]
        context["Users"] = User.objects.all()
        context["new_notice"] = Notice.objects.filter(
            usernameTo=self.request.user, read=False
        ).order_by("-date")
        return context


class Search(ListView):
    model = User
    template_name = "KODBURG/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notice"] = Notice.objects.filter(
            usernameTo=self.request.user
        ).order_by("-date")[:3]
        context["Users"] = User.objects.all()
        context["friends"] = self.request.user.friends
        context["new_notice"] = Notice.objects.filter(
            usernameTo=self.request.user, read=False
        ).order_by("-date")
        return context


@login_required
def other_user(request, username, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    object = Notice.objects.filter(usernameFrom=to_user, usernameTo=from_user)
    connection_from = Requests.objects.filter(user_from=from_user, user_to=to_user)
    connections_to = Requests.objects.filter(user_from=to_user, user_to=from_user)

    # smptObj = smtplib.SMTP('localhost')
    # smptObj.starttls()
    # smptObj.sendmail("egorkultinn@mail.ru", "yegor.kultin@bk.ru", "Hello, world!")
    # smptObj.quit()

    if object:
        if len(object) > 1:
            for i in range(len(object)):
                object_get = Notice.objects.filter(
                    usernameFrom=to_user, usernameTo=from_user
                )[i]
                object_get.read = True
                object_get.save()

        else:
            object_get = Notice.objects.get(usernameFrom=to_user, usernameTo=from_user)
            object_get.read = True
            object_get.save()

    if connection_from:
        connection = {"user_from": from_user.id, "user_to": userID}
    elif connections_to:
        connection = {"user_from": userID, "user_to": from_user.id}
    else:
        Requests.objects.create(user_from=from_user, user_to=to_user)
        new_connect = Requests.objects.get(user_from=from_user, user_to=to_user)
        from_user.connections.add(new_connect)
        to_user.connections.add(new_connect)
        connection = {"user_from": from_user.id, "user_to": userID}

    return render(
        request,
        "KODBURG/other_user.html",
        {
            "notices": Notice.objects.filter(usernameTo=request.user).order_by("-date")[
                :3
            ],
            "projects": Project_list.objects.filter(username=to_user).order_by("-date"),
            "blog": Blog_list.objects.filter(username=to_user).order_by("-date"),
            "fri_reqFrom": Friends_request.objects.filter(
                from_user=from_user, to_user=to_user
            ),
            "fri_reqTo": Friends_request.objects.filter(
                from_user=to_user, to_user=from_user
            ),
            "friends": request.user.friends,
            "room_to": Room.objects.filter(
                title=f"{from_user.username}.{to_user.username}"
            ),
            "room_from": Room.objects.filter(
                title=f"{to_user.username}.{from_user.username}"
            ),
            "other_user": to_user,
            "connection": connection,
        },
    )


def chat(request, user_from, user_to):
    my_id = request.user.pk
    print(user_from, user_to)
    user1 = User.objects.get(pk=user_from)
    user2 = User.objects.get(pk=user_to)
    print(f"{user1.username}.{user2.username}")

    if Messages.objects.filter(
        room=Room.objects.get(title=f"{user1.username}.{user2.username}"), viewed=False
    ).first:
        non_viewed = Messages.objects.filter(
            room=Room.objects.get(title=f"{user1.username}.{user2.username}"),
            viewed=False,
        ).first
        print(non_viewed, "Все работает!")
    else:
        non_viewed = ""
        print(user1.pk)
    if Messages.objects.filter(
        room=Room.objects.get(title=f"{user1.username}.{user2.username}")
    ):
        list = {}
        item = ""
        for i in Messages.objects.filter(
            room=Room.objects.get(title=f"{user1.username}.{user2.username}")
        ).order_by("time_send"):
            if item != i.time_send.date():
                item = i.time_send.date()
                print(item)
                list[item] = Messages.objects.filter(
                    room=Room.objects.get(title=f"{user1.username}.{user2.username}"),
                    time_send=i.time_send,
                ).first
        print(list)
    else:
        list = {}

    return render(
        request,
        "KODBURG/chat.html",
        {
            "room_name": f"{user1.username}.{user2.username}",
            "room_id": Room.objects.get(title=f"{user1.username}.{user2.username}").pk,
            "messages": Messages.objects.filter(
                room=Room.objects.get(title=f"{user1.username}.{user2.username}")
            ),
            "User": user1,
            "friends": request.user.friends,
            "non_viewed": non_viewed,
            "User1": user1,
            "User2": user2,
            "date": list,
        },
    )


def create_chat(request, user_from, user_to):
    user1 = User.objects.get(pk=user_from)
    user2 = User.objects.get(pk=user_to)
    if Room.objects.filter(title=f"{user1.username}.{user2.username}"):
        return redirect(f"/main/chat/{user_from}{user_to}/")
    elif Room.objects.filter(title=f"{user2.username}.{user1.username}"):
        return redirect(f"/main/chat/{user_to}{user_from}/")
    else:
        Room.objects.create(title=f"{user1.username}.{user2.username}")
        new_room = Room.objects.get(title=f"{user1.username}.{user2.username}")

        user1.chats.add(new_room)
        user2.chats.add(new_room)

        return redirect(f"/main/chat/{user_from}/{user_to}/")


def messager(request):
    Users = User.objects.all()
    rooms = Room.objects.all().order_by("time_create")
    notice = Notice.objects.filter(usernameTo=request.user).order_by("-date")[:3]

    list = {}
    for i in rooms:
        if request.user.username in i.title:
            print(i.title)
            if len(Messages.objects.filter(room=i)) > 0:
                print(">0")
                for item in User.objects.all():
                    if (
                        item != request.user
                        and item.username in i.title
                        and len(Messages.objects.filter(room=i)) > 1
                    ):
                        print(i.title, ">1")
                        if request.user.username + "." + item.username == i.title:
                            print(">1.1")
                            list[i.title] = {
                                "user_from": request.user,
                                "user_to": item,
                                "last_message": Messages.objects.filter(room=i)[
                                    len(Messages.objects.filter(room=i)) - 1
                                ],
                                "viewed": Messages.objects.filter(room=i)[
                                    len(Messages.objects.filter(room=i)) - 1
                                ].viewed,
                                "time_send": Messages.objects.filter(room=i)[
                                    len(Messages.objects.filter(room=i)) - 1
                                ].time_send,
                            }
                        elif item.username + "." + request.user.username == i.title:
                            print(">1.2")
                            list[i.title] = {
                                "user_from": item,
                                "user_to": request.user,
                                "last_message": Messages.objects.filter(room=i)[
                                    len(Messages.objects.filter(room=i)) - 1
                                ],
                                "viewed": Messages.objects.filter(room=i)[
                                    len(Messages.objects.filter(room=i)) - 1
                                ].viewed,
                                "time_send": Messages.objects.filter(room=i)[
                                    len(Messages.objects.filter(room=i)) - 1
                                ].time_send,
                            }
                    elif (
                        item != request.user
                        and item.username in i.title
                        and len(Messages.objects.filter(room=i)) == 1
                    ):
                        print(i.title, "=1")
                        if request.user.username + "." + item.username == i.title:
                            print("=1.1")
                            list[i.title] = {
                                "user_from": request.user,
                                "user_to": item,
                                "last_message": Messages.objects.get(room=i),
                                "viewed": Messages.objects.get(room=i).viewed,
                                "time_send": Messages.objects.get(room=i).time_send,
                            }
                        elif item.username + "." + request.user.username == i.title:
                            print("=1.2")
                            list[i.title] = {
                                "user_from": item,
                                "user_to": request.user,
                                "last_message": Messages.objects.get(room=i),
                                "viewed": Messages.objects.get(room=i).viewed,
                                "time_send": Messages.objects.get(room=i).time_send,
                            }
            else:
                print("=0")
                for item in User.objects.all():
                    if item != request.user and item.username in i.title:
                        if request.user.username + "." + item.username == i.title:
                            print("=0.1")
                            list[i.title] = {
                                "user_from": request.user,
                                "user_to": item,
                                "last_message": "Напишите свое первое сообщение!",
                                "viewed": True,
                                "time_send": Room.objects.get(title=i).time_create,
                            }
                        elif item.username + "." + request.user.username == i.title:
                            print("=0.2")
                            list[i.title] = {
                                "user_from": item,
                                "user_to": request.user,
                                "last_message": "Напишите свое первое сообщение!",
                                "viewed": True,
                                "time_send": Room.objects.get(title=i).time_create,
                            }

    return render(
        request,
        "KODBURG/messager.html",
        {
            "chats": list,
            "Users": Users,
            "notice": notice,
        },
    )
