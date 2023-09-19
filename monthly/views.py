from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import random

month_dict = {"jan": "The beginning of the year.", "feb": "Winter is almost gone.", 
                  "mar": "Spring is coming", "apr": "It becomes warmer."}
def home(request):
    return render(request, "monthly/home.html", {"title":"monthly", "months":list(month_dict.keys())})

def no_html_home(request):
    months = list(month_dict.keys())
    # create a hyperlink for each month
    items = ''
    for month in months:
        item_path = reverse("month-direct", args=[month]) # href path: 
        items += f"<li><a href=\"{item_path}\">{month.capitalize()}</a></li>"
    month_lists = f'<ul>{items}</ul>'
    return HttpResponse(month_lists)

def static_response_home(request):
    """random generates a number, showing content on the page."""
    val = random.randrange(0,4)
    months = list(month_dict.keys())
    if val > len(month_dict):
        text = "Not Found."
    else:
        text = month_dict[months[val]]
    return render(request, "monthly/home.html", {"title":"Monthly Challenges", "text":text})

# Create your views here.
def index(request, month):
    try:
        content = month_dict[month]
    except:
        return HttpResponseNotFound("This month is not supported.")
    return render(request, "monthly/index.html", {"specific":content})
    #return HttpResponse(month)


def monthly_digits(request, month): # redirect to string month --> index
    months = list(month_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Not found!")
    redirect = months[month - 1] # the name of the month.
    redirect_path = reverse("month-direct", args=[redirect])
    return HttpResponseRedirect(redirect_path)
    #return HttpResponseNotFound(f"This month {{month}}.")