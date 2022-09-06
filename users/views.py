from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .forms import CustomUser
from .forms import CreateUserForm
from .forms import CommentsBlogForm

from flightapp.utils import categWishlistHelper
from flightapp.models.cart import Cart

from .models import Post

from flightapp.utils import paginateProjects

# -------------------------  pages ------------------------- ------------------------- ---------------------


def profileView(request):

    context: dict = categWishlistHelper(request)

    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(
            user=request.user).prefetch_related("products").first()

        if cartProducts:
            context['blog'] = cartProducts.products.all()
            context["cardItems"] = context['blog']
            context["cartProductsCount"] = cartProducts.products.count()

    return render(request, 'pages/profiles.html')


def registerUser(request):
    page = 'register'
    forms = CreateUserForm()

    if request.method == 'POST':
        forms = CreateUserForm(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('profile')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'forms': forms}
    return render(request, 'registration/register.html', context)


def loginView(request):
    return render(request, 'pages/login.html')


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = CustomUser(instance=profile)

    if request.method == 'POST':
        form = CustomUser(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('uzgardi')

    context = {'form': form}
    return render(request, 'pages/profile.html', context)


def uzgarView(request):
    return render(request, 'registration/uzgardi.html')


def errorView(request):
    return render(request, 'pages/404.html')


def chekoutView(request):
    return render(request, 'pages/checkout/checkout.html')


def finishView(request):
    return render(request, 'pages/checkout/finish_shop.html')


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


def blogView(request):
    blogs = Post.objects.all()
    context = {'blogs': blogs}

    context: dict = categWishlistHelper(request)
    custom_range, blogs = paginateProjects(
        request,  blogs, 3)

    if request.user.is_staff:
        cartProducts: Cart = Cart.objects.filter(
            user=request.user).prefetch_related("products").first()

        if cartProducts:
            context['blog'] = cartProducts.products.all()
            context["cardItems"] = context['blog']
            context["cartProductsCount"] = cartProducts.products.count()

    context = {'blogs': blogs}

    return render(request, 'blog/blog.html', context)


def blogDetailView(request, id):
    blog = Post.objects.get(id=id)

    forming = CommentsBlogForm()

    if blog.commenting:
        counts = blog.commenting.count()
        
    if request.method == "POST":
        forming = CommentsBlogForm(request.POST)
        review = forming.save(commit=False)
        review.item = blog
        review.person = request.user
        review.save()

        return redirect('blogdetail', id=blog.id)

    context = {'blog': blog, 'counts': counts, 'blog': blog, 'forming': forming}

    return render(request, 'blog/detail.html', context)
