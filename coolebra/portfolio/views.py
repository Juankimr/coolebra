from django.shortcuts import render


def index(request):
    context = {
        'name': 'Juan Carlos',
        'last_name': 'Muñoz Ramos',
        'description': 'Full stack developer',
    }
    return render(request, 'portfolio/portfolio.html', context)
