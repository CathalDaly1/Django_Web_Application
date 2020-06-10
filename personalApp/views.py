from django.shortcuts import render


# Create your views here.
def index(request):
    # render is going to look in a templates directory
    # to stop conflicts create folder inside templates
    return render(request, 'personalApp/home.html')


def contact(request):
    return render(request, 'personalApp/basic.html', {'content': ['If you would like to contact me', 'cathald96@gmail.com']})
