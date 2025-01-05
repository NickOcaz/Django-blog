from django.shortcuts import render
from django.views import generic
from .models import Post
# from django.http import HttpResponse
# from .models import Post

class PostList(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'


# def post_list(request):
#    posts = Post.objects.filter(status=1).order_by('-created_on')
#    return render(request, 'blog/post_list.html', {'posts': posts})

#def my_blog(request):
#    return HttpResponse("Hello, Blog!")