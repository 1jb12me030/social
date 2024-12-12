from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

def index(request):
    posts = Post.objects.all()
    return render(request, 'dashboard/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'dashboard/post_detail.html', {'post': post, 'comments': comments})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes.add(request.user)
    return redirect('dashboard:post_detail', post_id=post_id)

# @login_required
# def add_comment(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         if content:
#             Comment.objects.create(post=post, author=request.user, content=content)
#     return redirect('dashboard:post_detail', post_id=post_id)


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post, Comment  # Replace with the actual names of your models
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Optional if you want to handle CSRF tokens manually
@login_required
def add_comment(request, post_id):
    # Retrieve the post using the provided post_id
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        # Get the comment content from the request
        content = request.POST.get('content')

        if content:
            # Create and save a new comment
            comment = Comment.objects.create(
                post=post,
                author=request.user,  # Automatically set the logged-in user as the author
                content=content
            )
            comment.save()

            # Redirect to the post detail page or another desired location
            return redirect('dashboard:post_detail', post_id=post.id)
        else:
            # If no content is provided, return an error or handle it gracefully
            return HttpResponseForbidden("Comment content cannot be empty.")

    # If not POST, redirect back to the post detail page
    return redirect('dashboard:post_detail', post_id=post.id)
