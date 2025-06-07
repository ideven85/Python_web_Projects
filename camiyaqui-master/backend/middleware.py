from django.contrib.auth.models import User

from backend.models import Visits


class PageViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.session.get("guest"):
            Visits.objects.create(
                guest=User.objects.get(pk=request.session.get("guest")),
                page=request.path,
            )

        return response
