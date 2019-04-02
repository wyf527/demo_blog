from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class Category(models.Model):
    cname=models.CharField(max_length=100,unique=True,verbose_name='类别')

    class Meta:
        db_table='t_category'
        verbose_name='类别信息'

    def __str__(self):
        return self.cname

class Tag(models.Model):
    tname = models.CharField(max_length=100, unique=True,verbose_name='标签')

    class Meta:
        db_table = 't_tag'
        verbose_name = '标签信息'

    def __str__(self):
        return self.tname

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc=models.TextField()

    #使用富文本应用修改该字段
    content=RichTextUploadingField()

    publish_time=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category)
    tag=models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name = '博客信息'

    def __str__(self):
        return self.title