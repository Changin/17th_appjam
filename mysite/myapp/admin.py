from django.contrib import admin
from .models import Post, Schedule, Board, MyUser

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(Schedule)
admin.site.register(Board)