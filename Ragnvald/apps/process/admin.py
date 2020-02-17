from django.contrib import admin
from .models import Tag, Task, Taskboard, Perm
# Register your models here.

admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(Taskboard)
admin.site.register(Perm)