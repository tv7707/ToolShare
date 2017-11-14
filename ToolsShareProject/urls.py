"""ToolsShareProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.conf import settings

from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()
# remove "Auth" menu's from admin
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = 'Tools Share Project - Administration Management Portal'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'website.views.login.index', name='index'),
    url(r'^index/$','website.views.login.index',name='index2'),
    url(r'^login/$','website.views.login.login',name='login'),
    url(r'^logout/$','website.views.login.logout',name='logout'),
    url(r'^register/$','website.views.registration.register',name='register'),
    url(r'^dashboard/$','website.views.dashboard.dashboard',name='dashboard'),
    url(r'^personalmanagemnet/$', 'website.views.users.personalmanagemnet', name='personalmanagemnet'),
    url(r'^changepassword/$', 'website.views.users.changepassword', name='changepassword'),
    url(r'^recoverpassword/$', 'website.views.users.recoverpassword', name='recoverpassword'),
    url(r'^statistics/$','website.views.statistics.toolstatistics',name='toolstatistics'),
    url(r'^registertool/$','website.views.community.registertool',name='registertool'),
    url(r'^listtool/$','website.views.community.listtool',name='listtool'),
    url(r'^borrow/$','website.views.community.borrow',name='borrow'),
    url(r'^mytools/$','website.views.community.mytools',name='mytools'),
    url(r'^borroweditems/$','website.views.community.borroweditems',name='borroweditems'),
    url(r'^communitycreate/$','website.views.communityshed.communitycreate',name='communitycreate'),
    url(r'^choice/$','website.views.communityshed.choice',name='choice'),
    url(r'^share/$','website.views.communityshed.share',name='share'),
    url(r'^sharechange/$','website.views.communityshed.sharechange',name='sharechange'),
    url(r'^notification/$','website.views.community.notification',name='notify'),
    url(r'^approve/$', 'website.views.community.approve', name='approve'),
    url(r'^othersheds/$', 'website.views.community.othersheds', name='othersheds'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
