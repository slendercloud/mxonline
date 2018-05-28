from django.db import models

import datetime

from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200,verbose_name=u'问题详情')
    pub_date = models.DateTimeField('添加日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    class Meta:
        verbose_name=u'投票应用'
        verbose_name_plural=verbose_name
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,verbose_name=u'投票项详情')
    votes = models.IntegerField(default=0,verbose_name='投票数')

    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name=u'投票项'
        verbose_name_plural=verbose_name
