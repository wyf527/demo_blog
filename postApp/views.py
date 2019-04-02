import math
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from postApp.models import Post


class BlogView(View):
    # 【健壮性】：初始化num=1，代表每次刷新都打开第一页
    def get(self,request,num=1):
        num=int(num)
        #查询全部博客内容
        # 注意：如果要分页显示，总的内容就不要传给前端
        # 而是将分页后的每一页数据传给前端
        pList=Post.objects.all().order_by('-publish_time')
        print(pList)
        #创建分页器对象
        page_obj=Paginator(pList,1)
        print(page_obj)
        #获取每一页数据
        per_pag_obj=page_obj.page(num)
        print(per_pag_obj)

        #获取将要展示的页码(注意，要和num产生关系)
        #页码的判断环环相扣，首先明确，num要处在页码列表的中间(前5后4)
        # 所以才有根据num计算start的公式
        start=num-math.ceil(10/2)

        #判断start是否越界在，并根据此次的start得出end
        if start<1:
            start=1
        end=start+9

        #再判断end，与总页数的关系
        if end>page_obj.num_pages:
            end=page_obj.num_pages

        #按照得出的end与10比较，并根据此次的end得出start
        if end<10:
            start=1
        else:
            start=end-9

        pageList=range(start,end+1)

        return render(request,'index.html',{'pageList':pageList,'per_pag_obj':per_pag_obj})


class DetailView(View):
    # 健壮性：初始化postid= -1，代表传递参数不成功时，就不会返回查询结果
    def get(self,request,postid=-1):
        #html页面传来的是字符串
        postid=int(postid)
        #查询content
        pObj=Post.objects.filter(id=postid)

        return render(request,'detail.html',{'pObj':pObj})


class CategoryView(View):
    def get(self,request,categoryid):
        #转换为int
        categoryid=int(categoryid)
        #查询分类下面的文章
        postList=Post.objects.filter(category=categoryid)

        return render(request,'categoryList.html',{'postList':postList})


class ArchiveView(View):
    def get(self,request,year,month):
        year=int(year)
        month=int(month)

        postList=Post.objects.filter(publish_time__year=year,publish_time__month=month)

        # 【归档】和【分类】底下的所有文章渲染的页面是一样的，都是展现详细文章的
        return render(request, 'categoryList.html', {'postList': postList})


class ArchiveListView(View):
    def get(self,request):
        return render(request,'ArchiveList.html')
