from django.contrib import admin
from django.urls import path
from Home.views import blog_view, blog_detail,about_view,menu_view
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from Home.models import Blog, menu , home_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',blog_view,name='blog'),
    path('blog/<slug:slug>',blog_detail,name='detail'),
    path('about/',about_view,name='about'),
    path('menu/',menu_view,name='menu'),
    path('home/', TemplateView.as_view(template_name='Home/home.html', extra_context={
        "instagram_profile_name": "mr.foodie_nepal",
         "blog": Blog.objects.all().order_by('-id')[0:3],
         "menu": menu.objects.all().order_by('-id')[0:4],
         "active_home": home_image.objects.all()[0],
         "home_image": home_image.objects.all()[1:],
    }),name='home'),

    path('gallery/', TemplateView.as_view(template_name='Home/gallery.html', extra_context={
        "instagram_profile_name": "foods.nepal",
    }),name='gallery'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
