from uuid import uuid4

from django.db.models import Sum
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from flightapp.models.cart import Cart
from flightapp.models.products import Brand, FeatureLeft
from flightapp.models.products import Banner
from flightapp.models.products import Products
from flightapp.models.products import BannerLefts
from flightapp.models.products import FeatureLeft
from flightapp.models.products import FeatureRights

from flightapp.models.category import Categories
from flightapp.models.order_history import OrderHistory

from .forms import GetInfoForm
from .bots.bot import telegram_bot_sendtext
from flightapp.utils import searchHelper
from flightapp.utils import categWishlistHelper
# from flightapp.libs.telegram import telebot


def homeView(request):
    day_recommends = Products.objects.filter(
        category=Categories.KUN_TAKLIFLARI)  # kunning eng yaxhi takliflari
    best_seller = Products.objects.filter(
        category=Categories.ENG_KOP_SOTILADIGAN)  # eng ko'p sotiladigan
    device = Products.objects.filter(
        category=Categories.SIZ_UCHUN_TAVFSIYA)  # eng mashhur mahsulotlar
    _all_products = Products.objects.all()
# (category__in=[
#         Categories.ENG_KOP_SOTILADIGAN,
#         Categories.KUN_TAKLIFLARI])
    dbctx: dict = {}
    myctx: dict = categWishlistHelper(request)
    dbctx["best_seller"] = best_seller
    dbctx["all_products"] = _all_products
    dbctx['day_recommends'] = day_recommends
    dbctx["device"] = device

    banners = Banner.objects.all()
    products = Products.objects.all()
    bannerleft = BannerLefts.objects.all()
    features = FeatureRights.objects.all()
    devices = FeatureLeft.objects.all()
    brand = Brand.objects.all()
    context: dict = {**dbctx, **myctx,'products': products, 'banners': banners,
                     'bannerleft': bannerleft, 'features': features, 'brand': brand, 'devices': devices}

    return render(request, 'home/index.html', context)

 
def aboutView(request):
    context: dict = categWishlistHelper(request)
    
    return render(request, 'about/about.html', context)


def shopView(request):
    context: dict = categWishlistHelper(request)
    
    return render(request, 'shop/shop.html', context)


def shopdetailView(request, id):
    context: dict = categWishlistHelper(request)
    
    context["items"]=Products.objects.get(id=id)

    return render(request, 'shop/detail.html', context)


def myWishlistView(request):
    context: dict = categWishlistHelper(request)
    if request.user.is_authenticated:
        cartHistory: OrderHistory = OrderHistory.objects.filter(user=request.user).prefetch_related("products").first()
        
        if cartHistory:
            context['items'] = cartHistory.products.all()
            context["cardItems"]=context['items']
            
    return render(request, 'pages/wishlist.html', context)


@login_required(login_url='profile')
def removeCartView(request, id: int) -> None:
    cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
    if cartProducts:
        cartItem = cartProducts.products.get(id=id)
        cartProducts.products.remove(cartItem)
        messages.add_message(request, messages.INFO, 'Savatchadan muofaqqiyatli o\'chirildi ✅')
    
    return redirect('home')


@login_required(login_url='my-account')
def removeOrderHistoryView(request, id: int) -> None:
    cartHistory: OrderHistory = OrderHistory.objects.filter(user=request.user).prefetch_related("products").first()
    if cartHistory:
        cartItem = cartHistory.products.get(id=id)
        cartHistory.products.remove(cartItem)
        messages.add_message(request, messages.INFO, 'Buyurtmalar tarixidan muofaqqiyatli o\'chirildi ✅')
    
    return redirect('home')


# @login_required(login_url='my-account')
def addCartView(request, id) -> None:
    messages.add_message(request, messages.INFO, 'Savatchaga muofaqqiyatli qo\'shildi ✅')
    
    product: Products = Products.objects.get(id=id)
    cart,_ = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    cart.save()
    if request.META['SERVER_NAME'] in settings.ALLOWED_HOSTS:
        return redirect('home')
    
    return redirect('home')


# def orderView(request):
#     if request.method == 'POST':
#         price: int = 0
#         text: str = ""
#         text += f"<b>ID</b>: {uuid4()}\n\n"
#         text += f"Haridor ismi: {request.user.first_name}\n"
#         text += f"Haridor Raqami: {request.user.phone}\n\n"
        
#         cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
#         order_history, _ = OrderHistory.objects.get_or_create(user=request.user)
        
#         for product in cartProducts.products.all():
#             price += product.price
#             order_history.products.add(product)
#             order_history.save()
#             text += f"{product.name} - {product.price} UZS\n"
        
#         cartProducts.delete()
#         text += F"Jami - {price} UZS"
#         telebot.send_message(text, telebot.TYPE_ORDERS)
        
#     return redirect('thanks')



def contactView(request):
    form = GetInfoForm()
    if request.POST:
        form = GetInfoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            text = f"Xabar yuborgan shaxs => {obj.fullname}\n  Nomeri: +{obj.nomer}\n  Email =>{obj.email}\n Xabar matni => {obj.message}"
            resp = telegram_bot_sendtext(text)
            if resp: 
                messages.success(
                    request, 'Xabaringiz muofaqqiyati yuborildi, tez oraqa sizga javob beramiz!')
            else:
                messages.success(
                    request, "Xabar yuborib  men biln bog'")

            return redirect('contact')

    else:
        form = GetInfoForm()

    context = {
        "form": form
    }

    return render(request, 'contact/contact.html', context)