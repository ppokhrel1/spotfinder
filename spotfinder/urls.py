from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from spots import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'spotfinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^upload/", views.upload),
    url(r"^/$", views.get_data),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
