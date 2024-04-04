from os import getenv
from requests import get
from .pars import ParsAnimeDemo
from dotenv import load_dotenv
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm, UserForm, ContactForm, CategoryForm
from .models import Post, Category, HomeImage, ContactSlider, Contact, HomeRowText, Anime

load_dotenv()
# Create your views here.
def index(request):
    obj_text = HomeRowText.objects.all()
    image_obg = HomeImage.objects.all()
    data = get(getenv("API_WEATHER").format("Almaty")).json()
    context = {
        'city': data['name'],
        'desc': data['weather'][0]['description'],
        'temp': data['main']['temp'],
        'icon': data['weather'][0]['icon'],
    }
    return render(request, "main/index.html", {"images": image_obg, "weather":context,"texts": obj_text})


def posts(request):
    Obj_All_Post = Post.objects.all()
    return render(request, "posts/post.html", {"context": Obj_All_Post})


def Add_Post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Добавление публикацииа прошла успенно!")
            return redirect("/posts")
    else:
        form = PostForm()

    return render(request, "insert/index.html", {"form": form})


def AddCategory(request):
    obj_category = Category.objects.all()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Добавление катебории прошла успенно!")
            return redirect("/posts")
    else:
        form = CategoryForm()
    return render(request, "insert/category.html", {"form": form, "categories": obj_category})


def logoutUser(request):
    logout(request)
    messages.success(request, 'Вы успенно вышли из учетной запики!')
    return redirect("/")


def SingUpUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.password == request.POST.get("password2"):
                user.set_password(user.password)
                user.save()
                messages.success(request, 'Ваша учетная запись для входа успешно создана!')
                return redirect("/")
    else:
        form = UserForm()
    return render(request, "AuthenticateUser/singup.html", {"form": form})


def SingInUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли!')
            return redirect("/")
        else:
            messages.error(request, 'Неверный логин или пароль!')
            return redirect("/")
        
    return render(request, "AuthenticateUser/singin.html")


def ContactView(request):
    obj_contact = Contact.objects.all()
    slider_image = ContactSlider.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше сообщение успенно отправленно!")
            return redirect("/")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html",  {"form": form, "sliders": slider_image, "contacts": obj_contact})


def AnimeView(request):
    anime_con = ParsAnimeDemo()
    
    for i in anime_con:
        # Проверяем, существует ли аниме с таким же заголовком
        if not Anime.objects.filter(title=i['anime_title']).exists():
            anime = Anime.objects.create(
                image=i['anime_img'],
                title=i['anime_title'],
                category=", ".join(i['anime_category']),
                description=i['anime_desc']
            )
            anime.save()

    anime_obj = Anime.objects.all().reverse()  # Используем метод reverse() для изменения порядка
    return render(request, "posts/anime.html", {"animes": anime_obj})