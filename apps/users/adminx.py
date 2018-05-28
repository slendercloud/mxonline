
from .models import UserProfile
from .models import EmailVerifyRecord,Banner
import xadmin
# class UserProfileAdmin(object):
#     pass
#
# xadmin.site.register(UserProfile,UserProfileAdmin)

xadmin.site.register(EmailVerifyRecord)
xadmin.site.register(Banner)