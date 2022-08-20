from django.shortcuts import render



def homeView(request):
    return render(request, 'home/index.html')


def aboutView(request):
    return render(request, 'about/about.html')


def shopView(request):
    return render(request, 'shop/shop.html')


def blogView(request):
    return render(request, 'blog/blog.html')


def contactView(request):
    return render(request, 'contact/contact.html')