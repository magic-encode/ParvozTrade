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
        self.cart = Cart.objects.create(
            user = self.user,
            products = self.product
        )
        self.wish = WishModel.objects.create(
            user = self.user,
            products = self.product
        )
        self.client = Client()
        
    def test_user_instance(self):
        user = CustomUser.objects.get(fullname = "Xalimov Abdulla")
        self.assertEqual(user.fullname, "Xalimov Abdulla")
        self.assertEqual(user.number, 940593733)
        self.assertEqual(user.password1, "password")
        self.assertEqual(user.password2, "password")

        
        
        
        