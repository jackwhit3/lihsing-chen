from django.shortcuts import render
from .models import Post
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')
	context = {'latest_post_list': latest_post_list}
	return render(request, 'blog/index.html', context)

def view_post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	context = {'post': post}
	return render(request, 'blog/view_post.html', context)