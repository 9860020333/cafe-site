from django.contrib import admin
from django.urls import path
from Home.views import blog_view, blog_detail,about_view
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from Home.models import Blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',blog_view,name='blog'),
    path('blog/<slug:slug>',blog_detail,name='detail'),
    path('about/',about_view,name='about'),

    path('home/', TemplateView.as_view(template_name='Home/home.html', extra_context={
        "instagram_profile_name": "Stage27.co",
         "blog": Blog.objects.all().order_by('-id')[0:3],
    }),name='home'),

    path('gallery/', TemplateView.as_view(template_name='Home/gallery.html', extra_context={
        "instagram_profile_name": "Stage27.co",
    }),name='gallery'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
