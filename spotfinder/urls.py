from django.conf.urls import include, url
from django.contrib import admin

from spots import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'spotfinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^upload/", views.upload),
    url(r"^get_data/", views.get_data),
    url(r'^admin/', include(admin.site.urls)),
]
