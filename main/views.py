from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Rakabima Ghaniendra Rusdianto',
        'class': 'PBP E',
        'appName' : 'beanScape'
    }

    return render(request, "main.html", context)