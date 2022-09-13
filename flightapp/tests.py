
from django.test import Client
from django.test import TestCase

from flightapp.models.cart import Cart
from flightapp.models.category import Categories
from flightapp.models.products import Products
from flightapp.models.products import Comments
from flightapp.models.sendmessage import GetInfo
from flightapp.models.wishs import WishModel

from users.models import CustomUser



class ModelsTestCase(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(
            fullname = "Xalimov Abdulla",
            number = 940593733,
            password1 = "password",
            password2 = "password"
        )
        self.category = Categories.objects.create(
           name="KUN_TAKLIFLARI",
           tag = "Smart Device" 
        )
        self.product = Products.objects.create(
            name="Mini Arra",
            description="Mini Arra description",
            price_new=50,
            category= self.category,
            image = "static/images.png"          
        )
        
        self.comment = Comments.objects.create(
            item = self.product,
            person = self.user
        )
        self.message = GetInfo.objects.create(
            fullname = "Halimov Abdulla",
            phone = 940593733,
            message = "Salom Dunyo seni tog'angmas"
        )
        # self.cart = Cart.objects.product.set(
        #     user = self.user,
        #     products = self.product
        # )
        # self.wish = WishModel.objects.create(
        #     user = self.user,
        #     products = self.product
        # )
        self.client = Client()
        
    def test_user_instance(self):
        user = CustomUser.objects.get(fullname = "Xalimov Abdulla")
        self.assertEqual(user.fullname, "Xalimov Abdulla")
        self.assertEqual(user.number, 940593733)
        self.assertEqual(user.password1, "password")
        self.assertEqual(user.password2, "password")

    def test_category_instance(self):
        category = Categories.objects.get(name="KUN_TAKLIFLARI")
        self.assertEqual(category.name, "KUN_TAKLIFLARI")
        self.assertEqual(category.tag, "Smart Device")
        
    def test_product_instance(self):
        product = Products.objects.get(name="Mini Arra")
        self.assertEqual(product.name, "Mini Arra")
        self.assertEqual(product.description, "Mini Arra description")
        self.assertEqual(product.price_new, 50)
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.image, "static/images.png")
        
    def test_comments_instance(self):
        comment = Comments.objects.get(
            item = self.product,
            person = self.user
            )
        self.assertEqual(comment.item, self.product)
        self.assertEqual(comment.person, self.user)
        
    def test_messages_instance(self):
        message = GetInfo.objects.get(fullname = "Halimov Abdulla")
        self.assertEqual(message.fullname, "Halimov Abdulla")
        self.assertEqual(message.phone, 940593733)
        self.assertEqual(message.message, "Salom Dunyo seni tog'angmas")
        
    # def test_cart_instance(self):
    #     cart = Cart.objects.get(user = self.user,
    #         products = self.product)
    #     self.assertEqual(cart.user, self.user)
    #     self.assertEqual(cart.products, self.products)
    
    # def test_wish_instance(self):
    #     wish = WishModel.objects.get(user = self.user,
    #         products = self.product)
    #     self.assertEqual(wish.user, self.user)
    #     self.assertEqual(wish.products, self.products)