from django.contrib import admin
from .models import UserAsk,CoueseComments,UserFavorite,UserMessage,UserCourse
# Register your models here.
admin.site.register(UserAsk)
admin.site.register(CoueseComments)
admin.site.register(UserFavorite)
admin.site.register(UserMessage)
admin.site.register(UserCourse)