
from datetime import date

from django.http import HttpResponse


def index(request):
    template = """
    <html>
        <head>
            <title>My First Django App</title>
        </head>
        <body>
            <h1>This is your first view!</h1>
            <p>Welcome to my first Django application.</p>
            <p>Application: firstapp</p>
            <a href="/firstapp/date/">Show today's date</a>
        </body>
    </html>
    """

    return HttpResponse(content=template)


def get_date(request):
    today = date.today()

    template = """
    <html>
        <head>
            <title>Today's Date</title>
        </head>
        <body>
            <h1>Today's date is {}</h1>
            <a href="/firstapp/">Back to home</a>
        </body>
    </html>
    """.format(today)

    return HttpResponse(content=template)

