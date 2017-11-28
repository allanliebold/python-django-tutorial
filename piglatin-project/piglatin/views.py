"""Create page views for url routes."""

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """View for home url."""
    return render(request, 'home.html')


def translate(request):
    """View for translate url."""
    input_text = request.GET['input_text'].lower()
    translation = ''

    for word in input_text.split():
        if word[:2] in ('sh', 'th', 'tr', 'pl', 'gr', 'bl', 'cr', 'cl',
                        'sl', 'ph', 'ch', 'dr', 'pr', 'br', 'fr'):
            translation += word[2:]
            translation += '-'
            translation += word[:2]
            translation += 'ay '
        elif word[0] in ('a', 'e', 'i', 'o', 'u'):
            translation += word
            translation += '-yay '
        else:
            translation += word[1:]
            translation += '-'
            translation += word[0]
            translation += 'ay '

    return render(request, 'translate.html')
