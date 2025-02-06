from django import template
from django.utils.safestring import mark_safe
import markdown
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


# form to upload content should support markdown in html/react...
# todo implement own markdown in templates..


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
