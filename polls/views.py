from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def main_page(request):
    return HttpResponse('Welcome To Django Main Page')
