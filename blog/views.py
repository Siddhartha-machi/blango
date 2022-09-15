from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from blog.models import Post
# Create your views here.
def index(request):
  posts = Post.objects.all()
  return render(request, 'blog/index.html',{'posts':posts})
  

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})