from django.conf.urls import url, include

from postApp import views

urlpatterns = [
    url(r'^blog/$', views.BlogView.as_view()),
    url(r'^page/(\d+)$',views.BlogView.as_view()),
    url(r'^post/(\d+)$',views.DetailView.as_view()),
    url(r'^category/(\d+)$',views.CategoryView.as_view()),
    url(r'^archive/$',views.ArchiveListView.as_view()),
    url(r'^archive/(\d+)/(\d+)$',views.ArchiveView.as_view()),

]