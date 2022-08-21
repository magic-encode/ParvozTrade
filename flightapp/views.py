from multiprocessing import context
from django.shortcuts import render
from flightapp.models.catagory import Banner



def homeView(request):
    catagory = Banner.objects.all()
    context = {'catagory': catagory}
    return render(request, 'home/index.html', context)


def aboutView(request):
    return render(request, 'about/about.html')


def shopView(request):
    return render(request, 'shop/shop.html')


def shopdetailView(request):
    return render(request, 'shop/detail.html')


def blogView(request):
    return render(request, 'blog/blog.html')


def blogdetailView(request):
    return render(request, 'blog/detail.html')


def contactView(request):
    return render(request, 'contact/contact.html')


def profileView(request):
    return render(request, 'pages/myaccount.html')


def loginView(request):
    return render(request, 'pages/login.html')


def cartView(request):
    return render(request, 'pages/cart.html')
