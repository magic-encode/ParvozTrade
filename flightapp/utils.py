from django.db.models import Q
from django.db.models import Sum

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from flightapp.libs.telegram import telebot

from flightapp.models.cart import Cart
from flightapp.models.wishlist import Wishlist

from flightapp.models.products import Products
from flightapp.models.category import Categories
from flightapp.models.customer import CustomerModel
from flightapp.models.order_history import OrderHistory



def paginateProjects(request, products, results):

    page = request.GET.get('page')
    paginator = Paginator(products, results)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, products




def getCategoryid(mystr: str) -> int:
    """
        This function returns the category identifier id
    """
    id = ""
    for item in mystr:
        if item.isdigit():
            id += item

    return id


def send_message(mydict: dict, _type: str = telebot.TYPE_ZAKAS) -> None:
    """
        This function sends a message to telegram channel
    """
    if mydict is not None:
        text: str = ""
        # Select name ...
        product = Products.objects.only(
            "name").get(id=mydict.get('product_id'))

        obj = CustomerModel.objects.create(
            name=mydict.get('name'),
            phone=mydict.get('phone'),
        )
        text += f"<b>Order ID: {obj.id}</b>\n\n"
        text += f"<b>Customer Name: {obj.name}</b>\n"
        text += f"<b>Customer Phone: {obj.phone}</b>\n"
        text += f"<b>Product Name: {product.name}</b>\n"

        context: dict = {
            "text": text,
            "_type": _type
        }

        telebot.send_message(**context)



def searchHelper(request) -> dict:
    """Returns a list of products"""
    search_query: str = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    category: str = Categories.objects.filter(
        name__icontains=search_query
    )

    products: list = Products.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(price_new__icontains=search_query) |
        Q(category__in=category)
    )

    return products, search_query


def categWishlistHelper(request) -> dict:
    categories = Categories.objects.all()

    """This function returns a list of wishlists and cart for each user"""
    myctx: dict = {}
    myctx["order_history"] = 0
    myctx["cartProductsCount"] = 0
    myctx['categories'] = categories

    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(
            user=request.user).prefetch_related("products").first()

        cartHistory: OrderHistory = OrderHistory.objects.filter(
            user=request.user).prefetch_related("products").first()

        if cartHistory:
            myctx["order_history"] = cartHistory.products.count()

        if cartProducts:
            myctx['sum'] = cartProducts.products.aggregate(
                Sum('price_new')).get('price_new__sum')
            myctx["cardItems"] = cartProducts.products.all()
            myctx["cartProductsCount"] = cartProducts.products.count()

    return myctx


def wishList(request):
    myctx: dict = {}
    myctx["cartProductsCount"] = 0

    if request.user.is_authenticated:
        wishProduct: Wishlist = Wishlist.objects.filter(
            user=request.user).prefetch_related("products").first()

        if wishProduct:
            myctx["cardItems"] = wishProduct.products.all()
            myctx["cartProductsCount"] = wishProduct.products.count()

    return myctx
