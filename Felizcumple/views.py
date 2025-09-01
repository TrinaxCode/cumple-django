from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    today = datetime.date.today()
    birthday = datetime.date(today.year, 10, 14)
    is_birthday = (today.month == birthday.month and today.day == birthday.day)
    return render(request, "Felizcumple/index.html", {"is_birthday": is_birthday})