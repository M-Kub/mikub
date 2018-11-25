from django.shortcuts import render


def cover_page(request):
    return render(request, 'webblog/cover.html')
