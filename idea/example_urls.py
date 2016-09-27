from django.conf.urls import include, url
from django.contrib import admin
import allauth.urls

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('idea.urls', namespace="idea")),
    url(r'^accounts/', include(allauth.urls))
]
