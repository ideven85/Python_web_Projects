from django.contrib import admin

from core.models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "created", "status"]
    search_fields = ["title", "body"]
    list_filter = ["status", "created", "publish", "author"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post']
    search_fields = ['name','post__title']
    list_filter = ['active','created','updated']