from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .forms import CustomUser
from .forms import CreateUserForm

from .models import Post


# -------------------------  pages ------------------------- ------------------------- ---------------------


def profileView(request):
    
    return render(request, 'pages/profiles.html')


# def loginUser(request):
    
#     if request.user.is_authenticated:
#         return redirect('home')

#     # if request.method == 'POST':
#     #     username = request.POST['username'].lower()
#     #     password = request.POST['password']

#     #     try:
#     #         user = CustomUser.objects.get(username=username)
#     #     except:
#     #         messages.error(request, 'Username does not exist')
#     #     print("Salom Dunyo")
#     #     user = authenticate(request, username=username, password=password)
        
#     #     if user is not None:
#     #         login(request, user)
#     #         request.GET['next'] if 'next' in request.GET else 'profile'
#     #         return redirect('profile')
            
#     #     else:
#     #         messages.error(request, 'Username OR password is incorrect')

#     return render(request, 'pages/login.html')


# def logoutUser(request):
#     logout(request)
#     messages.info(request, 'User was logged out!')
#     return redirect('login')


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

# @unauthenticated_user
# def registerUser(request):

#     forms = CreateUserForm()
#     if request.method == 'POST':
#         forms = CreateUserForm(request.POST)
#         if forms.is_valid():
#             user = forms.save()
#             username = forms.cleaned_data.get('username')

#             messages.success(request, 'Account was created for ' + username)
#             login(request, user)
#             return redirect('login')

#     context = {'forms': forms}
#     return render(request, 'pages/login.html', context)


def loginView(request):
    return render(request, 'pages/login.html')


# @login_required(login_url='login')
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


def cartView(request):
    return render(request, 'pages/cart/cart.html')


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


def blogView(request):
    blogs = Post.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/blog.html', context)


def blogDetailView(request, id):
    blog = Post.objects.get(id=id)


    return render(request, 'blog/detail.html', {'blog': blog})


def blogDetailView(request, id):
    blog = Post.objects.get(id=id)
    
    return render(request, 'blog/detail.html', {'blog': blog})
