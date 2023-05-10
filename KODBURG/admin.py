from .models import *
from django.contrib import admin
from .models import *

# Register your models here.


# class Admin(admin.ModelAdmin):
#     list_display = ["id", "title", "counter"]
#     def counter(self, obj):
#         return obj.counter.all().count()


admin.site.register(Post)
admin.site.register(User)

admin.site.register(Blog_list)
admin.site.register(Project_list)

admin.site.register(Comment_blog)
admin.site.register(Comment_project)

admin.site.register(Notice)
admin.site.register(Friends_request)

admin.site.register(Room)
admin.site.register(Messages)

admin.site.register(Requests)

