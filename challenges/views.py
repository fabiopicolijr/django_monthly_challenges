from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Walk for at least 21 minutes every day!",
    "april": "Walk for at least 22 minutes every day!",
    "may": "Walk for at least 23 minutes every day!",
    "june": "Walk for at least 24 minutes every day!",
    "july": "Walk for at least 25 minutes every day!",
    "august": "Walk for at least 26 minutes every day!",
    "september": "Walk for at least 27 minutes every day!",
    "october": "Walk for at least 28 minutes every day!",
    "november": "Walk for at least 29 minutes every day!",
    "december": "Walk for at least 30 minutes every day!",
}


def test():
    if 1+1 == 2:
        pass


def index(request):
    list_items = ""

    months = list(monthly_challenges.keys())

    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("This month is not supported.")
