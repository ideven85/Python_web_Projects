from django.contrib import admin

from .models import Profile, Group, Anecdote, MessageFromGuest, Guest

admin.site.register((Profile, Group, Anecdote, MessageFromGuest, Guest))
