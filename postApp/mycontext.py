from django.db.models import Count
from django.db import connection
from postApp.models import Post

#固定格式
def getRightInfo(request):
    #获取【分类】信息(从【多】的关系那一边查询)
    r_categoryInfo=Post.objects.values('category','category__cname').annotate(c=Count('*'))

    #获取【归档】信息
    #使用原生sql语句，使用游标执行
    cursor = connection.cursor()
    cursor.execute("SELECT publish_time,COUNT(*) as c FROM t_post GROUP BY DATE_FORMAT(publish_time,'%Y-%b') ORDER BY c DESC ")
    r_archive = cursor.fetchall()
    # 元组嵌套元组，第一个是datetime格式对象，使用过滤器转化。整体截取对象时，采用( .1、.0)方式
    # print(r_archive)#((datetime.datetime(2019, 1, 1, 8, 0, 38), 3),)

    #获取【最近文章】
    r_recent_post=Post.objects.order_by('-publish_time')[:3]
    #r_recent_post是列表，可以使用切片，切片是限制显示数量
    # print(r_recent_post)

    #固定返回格式
    return {'r_categoryInfo':r_categoryInfo,'r_archive':r_archive,'r_recent_post':r_recent_post}