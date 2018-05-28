from django.contrib import admin

# Register your models here.
from .models import UserProfile,EmailVerifyRecord,Banner

from .models import EmailVerifyRecord
class EmailVerifyRecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile)
class BannerAdmin(admin.ModelAdmin):
    pass
admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
admin.site.register(Banner,BannerAdmin)