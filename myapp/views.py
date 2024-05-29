from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random

@csrf_exempt 
def index(request):
    return render(request, 'index.html')

def hello(request):
    return HttpResponse('<div id="result">Hello, HTMX!</div>')

def generate(request):
    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
    ]

    random_number = random.randint(0, len(answers) - 1)
    phrase = answers[random_number]
    
    return HttpResponse(phrase)