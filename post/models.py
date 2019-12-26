from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=3000)
    regist_date = models.DateTimeField(blank=True, null=True)
    delete_data = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = 'post'


class PostInfo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    hanja = models.CharField(max_length=255)
    hiragana = models.CharField(max_length=255)
    hangul = models.CharField(max_length=255)
    regist_date = models.DateTimeField(blank=True, null=True)
    delete_data = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = 'post_info'
