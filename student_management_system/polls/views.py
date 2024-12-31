from django.db.models import F
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
from .models import Question, Choices


def questions(request):
    question_list = Question.objects.all().order_by("-pub_date")
    if not question_list:
        return render(request, "errors.html")
    return render(request, "home.html", {"question_list": question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "detail.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.Question.get(pk=request.POST["choice"])
    except (KeyError, Choices.DoesNotExist):
        return render(
            request,
            "detail.html",
            {"question": question, "error_message": "You did not select a choice"},
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("results", args=(question.id,)))


def results(request, question_id):
    result = get_object_or_404(Question, pk=question_id)
    return render(request, "result.html", {"result": result})


"""

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

"""
