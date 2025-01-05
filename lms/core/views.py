from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import CommentForm

# Create your views here.

from .models import Post


def post_list(request):
    post_list1 = Post.published.all()
    paginator = Paginator(post_list1, 3)
    page_number = request.GET.get("page", 1)  # Dictionary, get_or_default 1
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "posts/list.html", {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()

    return render(
        request, "posts/detail.html", {"post": post, "comments": comments, "form": form}
    )


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request, "posts/comment.html", {"post": post, "form": form, "comment": comment}
    )
