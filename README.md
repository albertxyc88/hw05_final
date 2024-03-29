# Проект «Yatube»

## Социальная сеть для публикации личных дневников. Пользователи могут заходить на чужие страницы, подписываться на авторов и комментировать их записи.
Автор может выбрать имя и уникальный адрес для своей страницы.

Возможности:
- Регистрация на сайте, с возможностью восстановления пароля по почте.
- Создание редактирование постов с картинками и категориями.
- Подписка на авторов, просмотр избранных постов.
- Система комментариев.
- Применен кэш для снижения нагрузки на сервер.
- Написаны тесты проверяющие работу проекта.

Полные права к постам, комментариям и подпискам доступны только для авторизованных пользователей, редактирование чужого контента запрещено. 
Для анонимных пользователей доступ только на чтение к постам, комментариям и сообществам.

## Технологии

Python 3.7, Django 2.2, JWT, SQLite3, Unittest.

## Установка

- склонируйте репозитарий 

- создайте и активируйте виртуальное окружение

`python3 -m venv venv`

`python3 venv/bin/activate`

- установите все зависимости из файла requirements.txt командой: 

`pip install -r requirements.txt`

- выполните миграции

`python manage.py migrate`

- запустите веб сервер

`python manage.py runserver`
