from django.shortcuts import render
from django.core.mail import send_mail
from .models import Blog, menu
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog_view(request):
    blog_list = Blog.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(blog_list, 3)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request,'Home/blog.html',{'blog':blogs})

def blog_detail(request,slug):
    context = {'blog':Blog.objects.get(slug=slug)
                }
    return render(request,'Home/detail.html',context)

def about_view(request):
    return render(request,'Home/about.html',{})

def menu_view(request):
    menu_list = menu.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(menu_list, 8)
    try:
        menus = paginator.page(page)
    except PageNotAnInteger:
        menus = paginator.page(1)
    except EmptyPage:
        menus = paginator.page(paginator.num_pages)

    return render(request,'Home/menu.html',{'menus':menus})