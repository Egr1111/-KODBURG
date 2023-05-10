from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe 
from django.dispatch import receiver
from django.core.validators import RegexValidator


class User(AbstractUser):
    image = models.ImageField(upload_to="User/photo", default="kodburg/enter.png")
    bio = models.TextField(verbose_name="Биография")
    friends = models.ManyToManyField("User", blank=True)
    notice = models.ManyToManyField("Notice", blank=True)
    descriptions = models.ManyToManyField("User", blank=True, related_name="Descriptions")
    chats = models.ManyToManyField("Room", blank=True)
    connections = models.ManyToManyField("Requests", blank=True, related_name="connections")

    

class Blog_list(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="User/blog",
                            default="User/blog/enter.png")
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, blank=True, related_name="like_blog")
    dislike = models.ManyToManyField(User, blank=True, related_name="dislike_blog")
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Project_list(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="User/projects/img",
                            default="User/blog/enter.png")
    file = models.FileField(upload_to="User/projects/files")
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, blank=True, related_name="like_project")
    dislike = models.ManyToManyField(User, blank=True, related_name="dislike_project")
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Notice(models.Model):
    usernameFrom = models.ForeignKey(
        User, related_name="usernameFrom", on_delete=models.PROTECT, null=True, blank=True)
    usernameTo = models.ForeignKey(
        User, related_name="usernameTo", on_delete=models.PROTECT, null=True, blank=True)
    image = models.ImageField(upload_to="User/photo", default="img/enter.png")
    text = models.TextField()
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usernameFrom.username}_{self.usernameTo.username}"




class Friends_request(models.Model):
    from_user = models.ForeignKey(
        User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name="to_user", on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.from_user.username}_{self.to_user.username}"
    

class Comment_blog(models.Model):
    blog = models.ForeignKey(Blog_list, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="other_img", default="img/enter.png")
    text = models.TextField()
    publishing = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    

class Comment_project(models.Model):
    project = models.ForeignKey(Project_list, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="other_img", default="img/enter.png")
    text = models.TextField()
    publishing = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

class Room(models.Model):
    title = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now=True)
    mes = models.ManyToManyField("Messages", related_name="mes", blank=True)
    def __str__(self) -> str:
        return self.title

class Messages(models.Model):
    user_from = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, related_name="user_from")
    message = models.CharField(max_length=255)
    viewed = models.BooleanField(default=False)
    time_send = models.DateTimeField(auto_now=True)
    room = models.ForeignKey("Room", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.message
    

class Requests(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_fromReq")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_toReq")
    
    def __str__(self):
        return f"{self.user_from.username}.web.{self.user_to.username}"
    



class Post(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to="kodburg/")
    
    def __str__(self) -> str:
        return self.title
    


