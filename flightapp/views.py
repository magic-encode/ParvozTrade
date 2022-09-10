from uuid import uuid4

from django.db.models import Sum
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from flightapp.models.cart import Cart
from flightapp.models.wishs import WishModel

from flightapp.models.products import Products
from flightapp.models.products import Comments

from flightapp.models.category import Categories
from flightapp.models.order_history import OrderHistory

from flightapp.forms import GetInfoForm
from flightapp.forms import CommentsForm

from flightapp.utils import wishList
from flightapp.utils import searchHelper
from flightapp.utils import wishViewHelper
from flightapp.utils import categWishlistHelper


from flightapp.libs.telegram import telebot

from .utils import paginateProjects


def homeView(request):

    day_recommends = Products.objects.filter(
        category=Categories.KUN_TAKLIFLARI)  # kunning eng yaxhi takliflari
    best_seller = Products.objects.filter(
        category=Categories.ENG_KOP_SOTILADIGAN)  # eng ko'p sotiladigan
    device = Products.objects.filter(
        category=Categories.SIZ_UCHUN_TAVFSIYA)  # eng mashhur mahsulotlar

    dbctx: dict = {}
    myctx: dict = categWishlistHelper(request)
    qyctx: dict = wishViewHelper(request)
    mywish = wishList(request)
    dbctx["best_seller"] = best_seller

    dbctx['day_recommends'] = day_recommends
    dbctx["device"] = device

    products = Products.objects.all()
   

    context: dict = {**dbctx, **myctx, **qyctx, 'products': products,  'mywish': mywish}

    return render(request, 'home/index.html', context)


def aboutView(request):
    qyctx: dict = wishViewHelper(request)
    myctx: dict = categWishlistHelper(request)
    context = {**qyctx, **myctx}
    return render(request, 'about/about.html', context)


def shopView(request):

    _all_products = Products.objects.all()
    dbctx: dict = {}
    myctx: dict = categWishlistHelper(request)
    dbctx["all_products"] = _all_products
    count = dbctx["all_products"].count()

    custom_range, dbctx["all_products"] = paginateProjects(
        request,  dbctx["all_products"], 9)

    context = {**dbctx, **myctx,  'custom_range': custom_range, 'count': count}
    return render(request, 'shop/shop.html', context)


def searchView(request) -> list:
    products, search_query = searchHelper(request)
    context: dict = categWishlistHelper(request)

    if len(products) > 0:
        context['products'] = products

    context = {'products': products, 'search_query': search_query}
    return render(request, 'shop/search.html', context)


def shopdetailView(request, id):
    myctx: dict = categWishlistHelper(request)
    _all_products = Products.objects.all()
    dbctx: dict = {}
    dbctx["all_products"] = _all_products

    items = Products.objects.get(id=id)
    if items.comment:
        counts = items.comment.count()

    forms = CommentsForm()

    if request.method == "POST":
        forms = CommentsForm(request.POST)
        review = forms.save(commit=False)
        review.item = items
        review.person = request.user
        review.save()

        # messages.success(request, 'Your review was successfully submitted!')
        return redirect('shopdetail', id=items.id)

    context = {**dbctx, **myctx, 'items': items,
               'forms': forms, 'counts': counts, }

    return render(request, 'shop/detail.html', context)


@login_required(login_url='login')
def commentRemove(request, id):
    commentr = Comments.objects.get(id=id)
    profile = request.user.is_staff
    comment = profile.commentr_set.get(id=commentr.id)
    comment.delete()

    return redirect('shopdetail', id)


@login_required(login_url='login')
def cartView(request):
    myctx: dict = categWishlistHelper(request)
    qyctx: dict = wishViewHelper(request)
    

    context = {**qyctx, **myctx}
    
    return render(request, 'pages/cart/cart.html', context)


@login_required(login_url='login')
def wishlistView(request):
    myctx: dict = categWishlistHelper(request)
    qyctx: dict = wishViewHelper(request)
    dbctx: dict = wishList(request)
    
    context = { **myctx, **dbctx, **qyctx}
    
    return render(request, 'pages/wishlist.html', context)


@login_required(login_url='login')
def addWishlistView(request, id) -> None:

    product: Products = Products.objects.get(id=id)
    wishlist, _ = WishModel.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    wishlist.save()
    if request.META['SERVER_NAME'] in settings.ALLOWED_HOSTS:
        return redirect(request.GET['next'] if 'next' in request.GET else 'wishlist')

    return redirect(request.GET['next'] if 'next' in request.GET else 'wishlist')


@login_required(login_url='login')
def removeWishlistView(request, id: int) -> None:
    wishProducts: WishModel = WishModel.objects.filter(
        user=request.user).prefetch_related("products").first()
    if wishProducts: 
        wishItem = wishProducts.products.get(id=id)
        wishProducts.products.remove(wishItem)

    return redirect('wishlist')


@login_required(login_url='login')
def removeCartView(request, id: int) -> None:
    cartProducts: Cart = Cart.objects.filter(
        user=request.user).prefetch_related("products").first()
    if cartProducts:
        cartItem = cartProducts.products.get(id=id)
        cartProducts.products.remove(cartItem)
        messages.add_message(request, messages.INFO,
                             'Savatchadan muofaqqiyatli o\'chirildi ✅')

    return redirect('cart')


@login_required(login_url='login')
def removeOrderHistoryView(request, id: int) -> None:
    cartHistory: OrderHistory = OrderHistory.objects.filter(
        user=request.user).prefetch_related("products").first()
    if cartHistory:
        cartItem = cartHistory.products.get(id=id)
        cartHistory.products.remove(cartItem)
        messages.add_message(request, messages.INFO,
                             'Buyurtmalar tarixidan muofaqqiyatli o\'chirildi ✅')

    return redirect('profile')


@login_required(login_url='login')
def addCartView(request, id) -> None:

    product: Products = Products.objects.get(id=id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    cart.save()
    if request.META['SERVER_NAME'] in settings.ALLOWED_HOSTS:
        return redirect('cart')

    return redirect('cart')


@login_required(login_url='login')
def orderView(request, _type: str = telebot.TYPE_ZAKAS):
    if request.method == 'POST':
        price: int = 0
        text: str = ""
        text += f"<b>ID</b>: {uuid4()}\n\n"
        text += f"Haridor ismi: {request.user.first_name}\n"
        text += f"Haridor Raqami: {request.user.phone}\n\n"

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
        text += F"Jami - {price} UZS"
        telebot.send_message(text, _type)

    tarix = order_history
    context = {'tarix': tarix}
    return redirect('thanks', context)


def contactView(request, _type: str = telebot.TYPE_SAVOL):
    form = GetInfoForm()

    if request.POST:
        form = GetInfoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            text = f"<b>Order ID: {obj.id}</b>\n\n <b>Customer Name: {obj.fullname}</b>\n <b>Customer Phone: {obj.phone}</b>\n <b>Xabar matni: {obj.message}</b>"

            telebot.send_message(text, _type)

            return redirect('contact')

    qyctx: dict = wishViewHelper(request)
    myctx: dict = categWishlistHelper(request)
    context = {**myctx, **qyctx, 'form': form}
    return render(request, 'contact/contact.html', context)
