from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.utils.translation import gettext as _, _trans as LANGUAGE_SESSION_KEY


class GuestMixin(AccessMixin):
    login_url = reverse_lazy("guest-login")
    permission_denied_message = _("Please login first")
    redirect_field_name = "next"

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("guest"):
            return self.handle_no_permission()
        user = User.objects.get(pk=request.session.get("guest"))
        user.profile.last_login = now()
        user.save()
        self.request.session[LANGUAGE_SESSION_KEY] = user.profile.language
        return super().dispatch(request, *args, **kwargs)
