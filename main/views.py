from django.shortcuts import render, redirect
from .models import Category, Product, Profile
from .forms import ProductForm, CategoryForm, UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def IndexView(request):
    return render(request, 'main/index.html')


def ProductView(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main/product.html', context=context)


def AddProductView(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Добавление продукта прошла успенно!")  
        else:          
            messages.error(request, form.errors)
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }

    return render(request, 'main/addproduct.html', context=context)


def CategoryView(request):
    return render(request, 'main/category.html')


def LogoutUserView(request):
    logout(request)
    return redirect('/')

def SingUpUserView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.password != request.POST.get('password2'):
                messages.error(request, "Пароли не совпадают!")
                return redirect('/signup')
            else:
                user.set_password(user.password)
                form.save()
                messages.success(request, "Резистрация прошла успенно!")
                return redirect("/")
    else:
        form = UserForm()
    return render(request, "AuthenticateUser/signup.html", {"form": form})


def SignInUserView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')
                    return redirect("/")
                else:
                    messages.error(request, 'Неверное имя пользователя или пароль.')
            except Exception:
                messages.error(request, 'Произошла ошибка при аутентификации. Пожалуйста, попробуйте снова.')
        else:
            messages.error(request, 'Пожалуйста, введите имя пользователя и пароль.')
    
    return render(request, "AuthenticateUser/signin.html")


def UserProfileView(request):
    if request.user.is_authenticated:
        profile = Profile.objects.all()
        return render(request, 'Profile/profile.html', {'profile': profile})
    else:
        return redirect('/signin')

def UserEditProfileView(request):
    if request.user.is_authenticated:
        user = request.user.profile
        if request.method == 'POST':
            new_email = request.POST.get('email')
            if new_email:
                user_email = request.user
                user_email.email = new_email
                user_email.save()
            
            form = ProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Редактирование профиля прошло успешно!")
                return redirect('/profile')
        else:
            form = ProfileForm(instance=user)

        context = {
            'form': form,
        }

        return render(request, 'Profile/editprofile.html', context=context)
    else:
        return redirect('/signin')

def SettingsView(request):
    if request.user.is_authenticated:
        return render(request, 'settings/settings.html')