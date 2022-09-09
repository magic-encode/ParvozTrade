from uuid import uuid4

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

from .forms import CustomUser
from .forms import CreateUserForm
from .forms import CommentsBlogForm

from flightapp.utils import send_message
from flightapp.utils import wishViewHelper
from flightapp.utils import categWishlistHelper

from flightapp.models.cart import Cart
from flightapp.models.order_history import OrderHistory

from .models import Post

from flightapp.libs.telegram import telebot

from flightapp.utils import paginateProjects

from flightapp.models.products import Products

# -------------------------  pages ------------------------- ------------------------- ---------------------


def profileView(request):
    myctx: dict = categWishlistHelper(request)
    tarix = OrderHistory.objects.filter(
        user=request.user).prefetch_related("products").first()
   
    print(tarix)
    context = {**myctx, 'tarix': tarix}

    return render(request, 'pages/profiles.html', context)


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


def chekoutView(request, id):
    cheks = Products.objects.get(id=id)
    myctx: dict = categWishlistHelper(request)
    qyctx: dict = wishViewHelper(request)

    context = {'cheks': cheks, **myctx, **qyctx}
    return render(request, 'pages/checkout/checkout.html', context)


def finishView(request):
    myctx: dict = categWishlistHelper(request)
    
    context = {**myctx,}
    return render(request, 'pages/checkout/finish_shop.html', context)


@login_required(login_url='login')
def orderView(request, _type: str = telebot.TYPE_ZAKAS):
    if request.method == 'POST':
        price: int = 0
        text: str = ""
        text += f"<b>ID</b>: {uuid4()}\n\n"
        text += f"Haridor ismi: {request.user.fullname}\n"
        text += f"Haridor Raqami: {request.user.number}\n\n"

        cartProducts: Cart = Cart.objects.filter(
            user=request.user).prefetch_related("products").first()
        order_history, _ = OrderHistory.objects.get_or_create(
            user=request.user)

        for product in cartProducts.products.all():
            price += product.price_new
            order_history.products.add(product)
            order_history.save()
            text += f"{product.name} - {product.price_new} UZS\n"

        cartProducts.delete()
        text += F"Jami - {price} $"
        telebot.send_message(text, _type)

    return redirect('thanks')


def sendMessageView(request, id: str) -> None:
    if request.user.is_authenticated:
        order_history, _ = OrderHistory.objects.get_or_create(user=request.user)
        product = Products.objects.get(id=id)
        order_history.products.add(product)
        order_history.save()
            
    if request.method == 'POST':
        mydict: dict = {}
        mydict.update({
            "name": request.POST.get('name'),
            "phone": request.POST.get('phone'),
            
            "product_id": id
        })
        send_message(mydict)
        return redirect('thanks')


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
    myctx: dict = categWishlistHelper(request)
    context: dict = categWishlistHelper(request)
    custom_range, blogs = paginateProjects(
        request,  blogs, 3)

    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(
            user=request.user).prefetch_related("products").first()

        if cartProducts:
            context['blog'] = cartProducts.products.all()
            context["cardItems"] = context['blog']
            context["cartProductsCount"] = cartProducts.products.count()

    context = {**myctx,'blogs': blogs, 'custom_range': custom_range}

    return render(request, 'blog/blog.html', context)


def blogDetailView(request, id):
    blog = Post.objects.get(id=id)
    myctx: dict = categWishlistHelper(request)
    
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

    context = {**myctx, 'blog': blog, 'counts': counts, 'blog': blog, 'forming': forming}

    return render(request, 'blog/detail.html', context)
