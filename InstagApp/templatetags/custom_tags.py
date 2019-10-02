import re
from django import template
from django.urls import NoReverseMatch
from InstagApp.models import Like

register = template.Library()


@register.simple_tag
def has_user_liked_post(post, user):
    try:
        like = Like.objects.get(post=post, user=user)
        return "fas"
    except:
        return "far"
