from django.conf.urls import include, url
from django.contrib import admin
from mysite import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^(\d+)/(\w+)/$',views.index),
    url(r'^list/$',views.listing),
    url(r'^post/$',views.posting),
    url(r'^post2db/$',views.post2db),
    url(r'^contact/$',views.contact),
]
