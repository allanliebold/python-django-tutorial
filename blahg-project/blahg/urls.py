"""blahg URL Configuration."""


from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
