from django.shortcuts import render, get_object_or_404
from .models import blogs

# Create your views here.
def blog(request):
    posts = blogs.objects.order_by('-date')
    return render(request, 'blog.html', {'posts': posts})

def post(request, blog_id):
    postview = get_object_or_404(blogs, pk=blog_id)
    return render(request, 'post_view.html',{'postview': postview})