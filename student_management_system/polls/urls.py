from django.urls import path
from .views import questions, detail, vote, results

urlpatterns = [
    path("", questions, name="question_list"),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/results/", results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", vote, name="vote"),
]
