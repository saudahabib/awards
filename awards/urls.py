from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^project/(\d+)/',views.project,name ='project'),
    url(r'^new/article/$', views.new_project, name='new-project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
