from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return "<h1>Hello World</<h1>" # string of html code not exactly html
    print(request.user)
    # return HttpResponse("<h1>Hello World</<h1>")
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_boolean": True,
        "my_list": [123, 'lkjh', 456],
        "my_html": "<h1>Hello World</h1>",
        "title": "this is a title"
    }
    return render(request, "home.html", my_context)

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact view</h1>")
    return render(request, "contact.html", {})