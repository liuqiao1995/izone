# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import Toolview,BD_pushview,bd_api_view,BD_pushview_site,bd_api_site,Link_testview,Link_test_api
from .views import regexview,regex_api


urlpatterns = [
    url(r'^$', Toolview, name='total'),  # 工具汇总页
    url(r'^baidu-linksubmit/$',BD_pushview,name='baidu_push'), # 百度主动推送
    url(r'^baidu-linksubmit/ajax/$',bd_api_view,name='baidu_push_api'), # 百度推送ajax
    url(r'^baidu-linksubmit-for-sitemap/$',BD_pushview_site,name='baidu_push_site'), # 百度主动推送sitemap
    url(r'^baidu-linksubmit-for-sitemap/ajax/$',bd_api_site,name='baidu_push_api_site'),
    url(r'^link-test/$',Link_testview,name='link_test'),  # 友链检测
    url(r'^link-test/ajax/$',Link_test_api,name='link_test_api'),
    url(r'^regex/$',regexview,name='regex'), # 正则表达式在线
    url(r'^regex/ajax/$',regex_api,name='regex_api'),
]
