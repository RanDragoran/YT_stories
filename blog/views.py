from django.shortcuts import render

def blogs(request):
    blogs_dictionary = {'navBar': 'blog'}
    return render(request, 'blog/blogs.html', blogs_dictionary)
