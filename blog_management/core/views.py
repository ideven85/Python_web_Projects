from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST
from taggit.models import Tag
from .forms import CommentForm, SearchForm

# Create your views here.

from .models import Post


def index(request):
    response = HttpResponse()
    response.cookies["my_cookie"] = "Deven"
    response.cookies["admin"] = "Admin"
    return response


class MyView(View):
    def dispatch(self, request, *args, **kwargs):
        # Always call this view first
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        response = HttpResponse()
        response.cookies["my_cookie"] = "Deven"
        response.cookies["admin"] = "Admin"
        return response


def post_list(request, tag_slug=None):
    post_lists = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_lists = post_lists.filter(tags__in=[tag])
    paginator = Paginator(post_lists, 3)
    page_number = request.GET.get("page", 1)  # Dictionary, get_or_default 1
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "posts/list.html", {"posts": posts, "tag": tag})

@login_required(redirect_field_name='/account/login/')
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    post_tag_ids = post.tags.values_list(
        "id", flat=True
    )  # flat indicates single values instead of tuples which queryset returns
    similar_posts = Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
    # todo redo with proper algorithm
    similar_posts = similar_posts.annotate(
        same_tags=Count("tags")
    ).order_by(  # Descending Order
        "same_tags", "publish"
    )[
        :4
    ]  # temporary
    return render(
        request,
        "posts/detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form,
            "similar_posts": similar_posts,
        },
    )


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post  # Registering comment foreign key to post?
        comment.save()
    return render(
        request, "posts/comment.html", {"post": post, "form": form, "comment": comment}
    )


# todo Implementing full text search using postgres or after learning nlp


def post_search(request):
    form = SearchForm()
    query = None  # Given if query...? Way too complex dependencies...
    results = []

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            search_vector = SearchVector("title", "body")
            search_query = SearchQuery(query)
            results = (
                Post.published.annotate(
                    search=SearchVector("title", "body"),
                    rank=SearchRank(search_vector, search_query),
                )
                .filter(search=query)
                .order_by("-rank")
            )
        return render(
            request,
            "posts/search.html",
            {"form": form, "query": query, "results": results},
        )
