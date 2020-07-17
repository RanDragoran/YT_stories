from django.shortcuts import render
from .models import blog

def blogs(request):
    blogs = blog.objects.all()
    latestDate = blog.objects.latest('blogDate')
    blogs_dictionary = {'blogs': blogs, 'navBar': 'blog', 'date' : latestDate}

    return render(request, 'blog/blogs.html', blogs_dictionary)
