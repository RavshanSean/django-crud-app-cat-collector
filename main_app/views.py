from django.shortcuts import render

from django.http import HttpResponse

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of Cat instances
cats = [
    Cat('Lolo', 'tabby', 'Kinda rude.', 3),
    Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]



def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')

def cat_index(request):
    return render(request, 'cats/index.html', {'cats': cats})