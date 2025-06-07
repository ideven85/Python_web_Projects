from django.contrib import admin

from backend.models import InternalMessage, PushTokens, Message, SentMessages, Visits

admin.site.register((Message, SentMessages, InternalMessage, PushTokens, Visits))
