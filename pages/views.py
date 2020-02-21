from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "title": "This is about us",
        "my_number": 3,
        "my_list": {123, 321, 1435},
        "this_is_true": True,
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, "contact.html", my_context)