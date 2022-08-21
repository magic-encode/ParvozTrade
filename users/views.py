from django.shortcuts import render


# -------------------------  pages ------------------------- ------------------------- ---------------------


def profileView(request):
    return render(request, 'pages/myaccount.html')


def loginView(request):
    return render(request, 'pages/login.html')


def cartView(request):
    return render(request, 'pages/cart.html')


def errorView(request):
    return render(request, 'pages/404.html')


def chekoutView(request):
    return render(request, 'pages/checkout.html')


def comingView(request):
    return render(request, 'pages/coming-soon.html')


def emptyView(request):
    return render(request, 'pages/empty-cart.html')


def faqView(request):
    return render(request, 'pages/faq.html')


def thanksView(request):
    return render(request, 'pages/thank-you-page.html')


def wishlistView(request):
    return render(request, 'pages/wishlist.html')
