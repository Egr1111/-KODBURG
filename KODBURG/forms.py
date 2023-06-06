from .models import *
from django.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserCreateForm(UserCreationForm):
    username = CharField(
        label="Введите свой nickname",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "input-class col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "placeholder": "nickname",
            }
        ),
    )

    email = CharField(
        label="Введите свою электронную почту",
        max_length=255,
        widget=(
            TextInput(
                attrs={
                    "class": "input-class col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                    "placeholder": "email",
                }
            )
        ),
    )

    password1 = CharField(
        label="Введите пароль",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "input-class col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "placeholder": "password",
                "type": "password",
            }
        ),
    )

    password2 = CharField(
        label="Повторите пароль",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "input-class col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "placeholder": "password",
                "type": "password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"autofocus": False})
        self.fields["password1"].widget.attrs.update({"autofocus": False})
        self.fields["password2"].widget.attrs.update({"autofocus": False})
        self.fields["email"].widget.attrs.update({"autofocus": False})

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        username = cleaned_data.get("username")
        num = [f"{i}" for i in range(9)]
        sim = ["@", "+", "-", "_"] + num
        for i in username:
            if not i.isalpha() and i not in sim:
                self.add_error(
                    "username",
                    "Введите правильное имя пользователя. Оно может содержать только буквы, цифры и знаки @/+/-/_.",
                )
                break
        return cleaned_data


class UserLoginForm(AuthenticationForm):
    username = CharField(
        label="Введите свой nickname",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "input-class col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "placeholder": "nickname",
            }
        ),
    )

    password = CharField(
        label="Введите пароль",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "input-class col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "placeholder": "password",
                "type": "password",
            }
        ),
    )

    class Meta:
        model = User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "image", "bio"]
        widgets = {
            "username": TextInput(
                attrs={"class": "input-class col-12", "placeholder": "nickname"}
            ),
            "email": TextInput(
                attrs={
                    "class": "input-class col-12 email",
                    "placeholder": "email",
                    "type": "email",
                }
            ),
            "first_name": TextInput(
                attrs={
                    "class": "input-class col-12",
                    "placeholder": "Как вас зовут?",
                }
            ),
            "last_name": TextInput(
                attrs={
                    "class": "input-class col-12",
                    "placeholder": "Можно узнать вашу фамилию?",
                }
            ),
            "image": FileInput(
                attrs={
                    "class": "input-class col-12",
                }
            ),
            "bio": Textarea(
                attrs={
                    "class": "input-class text col-12",
                    "style": "text-align: start!important, overflow: hidden;",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["bio"].required = False

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        username = cleaned_data.get("username")
        num = [f"{i}" for i in range(0, 10)]
        sim = ["@", "+", "-", "_"] + num
        for i in username:
            if not i.isalpha() and i not in sim:
                self.add_error(
                    "username",
                    "Введите правильное имя пользователя. Оно может содержать только буквы, цифры и знаки @/+/-/_.",
                )
                break
        return cleaned_data


class UserPasswordForm(ModelForm):
    class Meta:
        model = User
        fields = ["password"]
        widgets = {
            "password": PasswordInput(
                attrs={
                    "class": "input-class col-12",
                    "placeholder": "Введите новый пароль",
                }
            )
        }


class UserLostForm(ModelForm):
    username = CharField(
        label="Введите свой username",
        max_length=255,
        widget=TextInput(
            attrs={"class": "input-class col-12", "placeholder": "username"}
        ),
    )
    email = CharField(
        label="Введите свой email",
        max_length=255,
        widget=EmailInput(
            attrs={"class": "input-class col-12", "placeholder": "email"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].required = False
        self.fields["email"].required = False
    


class Blog_form(ModelForm):
    class Meta:
        model = Blog_list
        fields = ["title", "text", "img", "username"]
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "col-12 col-lg-7 h-100",
                    "placeholder": "Название поста",
                }
            ),
            "text": Textarea(
                attrs={
                    "class": "col-12",
                }
            ),
            "img": FileInput(attrs={"style": "color: black!important"}),
        }


class Project_form(ModelForm):
    class Meta:
        model = Project_list
        fields = ["title", "text", "img", "file", "username"]
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "col-12 col-lg-7 h-100",
                    "placeholder": "Название поста",
                }
            ),
            "text": Textarea(
                attrs={
                    "style": "overflow: hidden;",
                    "class": "col-12",
                }
            ),
            "img": FileInput(attrs={"style": "color: black!important"}),
            "file": FileInput(
                attrs={"style": "color: black!important", "accept": ".rar, .zip"}
            ),
        }


class Friend_form(ModelForm):
    class Meta:
        model = Notice
        fields = ["usernameFrom", "usernameTo", "image", "text"]


class Comments_to_blog(ModelForm):
    class Meta:
        model = Comment_blog
        fields = ["blog", "author", "text", "image"]
        widgets = {
            "text": Textarea(attrs={"class": "col-12", "style": "height: 5vh"}),
            "image": FileInput(
                attrs={
                    "class": "input-class col-12",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].required = False


class Comments_to_projects(ModelForm):
    class Meta:
        model = Comment_project
        fields = ["project", "author", "text", "image"]
        widgets = {
            "text": Textarea(attrs={"class": "col-12", "style": "height: 5vh"}),
            "image": FileInput(
                attrs={
                    "class": "input-class col-12",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].required = False
