from uuid import uuid4

from django.db.models import Sum
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from flightapp.models.cart import Cart
from flightapp.models.wishlist import Wishlist

from flightapp.models.products import Brand, FeatureLeft
from flightapp.models.products import Banner
from flightapp.models.products import Products
from flightapp.models.products import Comments
from flightapp.models.products import BannerLefts
from flightapp.models.products import FeatureLeft
from flightapp.models.products import FeatureRights

from flightapp.models.category import Categories
from flightapp.models.order_history import OrderHistory

from flightapp.forms import GetInfoForm
from flightapp.forms import CommentsForm

from flightapp.utils import searchHelper, wishList
from flightapp.utils import categWishlistHelper, send_message
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
    mywish = wishList(request)
    dbctx["best_seller"] = best_seller

    dbctx['day_recommends'] = day_recommends
    dbctx["device"] = device

    banners = Banner.objects.all()
    products = Products.objects.all()
    bannerleft = BannerLefts.objects.all()
    features = FeatureRights.objects.all()
    devices = FeatureLeft.objects.all()
    brand = Brand.objects.all()

    context: dict = {**dbctx, **myctx, 'products': products, 'banners': banners,
                     'bannerleft': bannerleft, 'features': features, 'brand': brand, 'devices': devices, 'mywish': mywish}

    return render(request, 'home/index.html', context)


def aboutView(request):
      
    context: dict = categWishlistHelper(request)

    return render(request, 'about/about.html', context)


def shopView(request):

    _all_products = Products.objects.all()
    dbctx: dict = {}
    myctx: dict = categWishlistHelper(request)
    dbctx["all_products"] = _all_products
    context = {**dbctx, **myctx}
    custom_range, product = paginateProjects(request,  product, 3)
    return render(request, 'shop/shop.html', context)


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

    
    context = {**dbctx, **myctx, 'items': items, 'forms': forms, 'counts': counts,}

    return render(request, 'shop/detail.html', context)


def commentRemove(request, id):
    commentr = Comments.objects.get(id=id)
    profile = request.user.is_staff
    comment = profile.commentr_set.get(id=commentr.id)
    comment.delete()

    return redirect('shopdetail', id)


@login_required(login_url='login')
def cartView(request):
    context: dict = categWishlistHelper(request)

    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(
            user=request.user).prefetch_related("products").first()

        if cartProducts:
            context['items'] = cartProducts.products.all()
            context["cardItems"] = context['items']
            context["cartProductsCount"] = cartProducts.products.count()

            context['sum'] = cartProducts.products.aggregate(
                Sum('price_new')).get('price_new__sum')

    return render(request, 'pages/cart/cart.html', context)


@login_required(login_url='login')
def wishlistView(request):
    context: dict = wishList(request)

    if request.user.is_authenticated:
        wishProduct: Wishlist = Wishlist.objects.filter(
            user=request.user).prefetch_related("products").first()

        if wishProduct:
            context["items"] = wishProduct.products.all()
            context["cardItem"] = context['items']
            context["cartProductsCount"] = wishProduct.products.count()

    return render(request, 'pages/wishlist.html', context)


@login_required(login_url='login')
def addWishlistView(request, id) -> None:

    product: Products = Products.objects.get(id=id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    wishlist.save()
    if request.META['SERVER_NAME'] in settings.ALLOWED_HOSTS:
        return redirect(request.GET['next'] if 'next' in request.GET else 'wishlist')

    return redirect(request.GET['next'] if 'next' in request.GET else 'wishlist')


@login_required(login_url='login')
def removeWishlistView(request, id: int) -> None:
    wishProducts: Wishlist = Wishlist.objects.filter(
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


def orderView(request):
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
            text += f"{product.name} - {product.price} UZS\n"

        cartProducts.delete()
        text += F"Jami - {price} UZS"
        telebot.send_message(text, telebot.TYPE_ZAKAS)

    return redirect('thanks')


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

    context: dict = categWishlistHelper(request)

    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(
            user=request.user).prefetch_related("products").first()

        if cartProducts:
            context['items'] = cartProducts.products.all()
            context["cardItems"] = context['items']
            context["form"] = form
            context["cartProductsCount"] = cartProducts.products.count()

    return render(request, 'contact/contact.html', context)
