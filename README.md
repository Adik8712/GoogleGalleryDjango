## Интернет-магазин на Django с парсингом аниме

![GoogleGallery](https://img.shields.io/badge/GoogleGallery-Django-brightgreen)
![AnimeParser](https://img.shields.io/badge/AnimeParser-BeautifulSoup-orange)

Этот проект представляет собой полнофункциональное веб-приложение интернет-магазина, разработанное с использованием Django. В дополнение к основному функционалу, приложение также включает в себя возможность парсинга информации о новых аниме с внешнего сайта.

### Особенности проекта

- **Аутентификация и авторизация**: Пользователи могут регистрироваться, аутентифицироваться и сбрасывать пароли.
- **Корзина покупок**: Пользователи могут добавлять товары в корзину, изменять количество и удалять товары перед оформлением заказа.
- **Оформление заказов**: После добавления товаров в корзину пользователи могут оформить заказ, вводя свои данные для доставки.
- **Панель администратора**: Администраторы имеют доступ к управлению категориями товаров, продуктами и заказами через административный интерфейс Django.
- **Парсинг аниме**: Приложение автоматически собирает информацию о новых аниме с внешнего сайта и предоставляет её пользователям.

### Установка и запуск

1. **Клонирование репозитория**

    ```bash
    git clone https://github.com/Adik8712/GoogleGalleryDjango.git
    cd GoogleGalleryDjango/
    ```

2. **Установка и активация виртуального окружения**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # для Linux / macOS
    venv\Scripts\activate  # для Windows
    ```

3. **Установка зависимостей**

    ```bash
    pip install -r requirements.txt
    ```

4. **Применение миграций и создание суперпользователя**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. **Запуск сервера**

    ```bash
    python manage.py runserver
    ```

6. **Доступ к приложению**

    После запуска сервера перейдите по адресу [http://localhost:8000](http://localhost:8000) для доступа к приложению.

### Структура проекта

```
.
├── api_main
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── ...
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── main
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── ...
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── parsers
│   ├── anime_parser.py
│   └── __init__.py
├── ShopDjango
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── media
│   └── ...
├── static
│   └── ...
├── templates
│   └── ...
├── venv
│   └── ...
├── README.md
└── requirements.txt
```

Добавлен раздел `parsers` для хранения скриптов парсинга аниме. Включен BeautifulSoup для парсинга страниц.

### Участники

- [Adik](https://github.com/Adik8712)

### Лицензия

Этот проект лицензирован по лицензии MIT - см. файл [LICENSE](LICENSE) для получения дополнительной информации.

Не стесняйтесь вносить свой вклад в проект, открывая проблемы или отправляя запросы на объединение изменений (pull requests)! Если у вас возникли проблемы или есть предложения по улучшению, пожалуйста, дайте [нам](https://t.me/AdikPy) знать. Удачного кодирования! 🚀