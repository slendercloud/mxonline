# _*_  coding:utf-8 _*_
from django.db import models
from  django.contrib.auth.models import AbstractUser
from datetime import  datetime
# Create your models here.


class UserProfile(AbstractUser):
    nick_name=models.CharField(verbose_name=u"昵称",max_length=30,default="")
    birday=models.DateField(verbose_name=u"生日",max_length=30,null=True,blank=True)
    gender=models.CharField(max_length=10,choices=(("male","男"),("famale","女")),default="famale")
    address=models.TextField(max_length=100,verbose_name=u"地址",default=u"")
    mobile=models.CharField(verbose_name=u"手机号",null=True,blank=True,max_length=11)
    image=models.ImageField(upload_to="image/%Y/%M",default=u"image/default.png",max_length=100)

    class Meta:
              verbose_name="用户信息"
              verbose_name_plural=verbose_name

    def __unicode__(self):
              return self.username


class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name=u"验证码")
    email=models.EmailField(verbose_name=u"邮箱")
    send_type=models.CharField(choices=(('register',u'注册'),('forget',u'找回')),max_length=10)
    send_time=models.DateTimeField(default=datetime.now,verbose_name=u'发送时间')

    class Meta:
        verbose_name=u"邮箱验证码"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.code

class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u'标题')
    image=models.ImageField(upload_to="banner/%Y/%M",verbose_name=u'轮播图')
    url=models.URLField(max_length=100,verbose_name=u"访问地址")
    index=models.IntegerField(default=100,verbose_name=u'顺序')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'轮播图'
        verbose_name_plural=verbose_name
