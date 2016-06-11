#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os

from _wall import Wall
wall = Wall()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session = cookie.get("session")
if session is not None:
    session = session.value
user = wall.find_cookie(session)  # Ищем пользователя по переданной куке

form = cgi.FieldStorage()
action = form.getfirst("action", "")

if action == "publish":
    text = form.getfirst("text", "")
    text = html.escape(text)
    if text and user is not None:
        wall.publish(user, text)
elif action == "login":
    login = form.getfirst("login", "")
    login = html.escape(login)
    password = form.getfirst("password", "")
    password = html.escape(password)
    if wall.find(login, password):
        cookie = wall.set_cookie(login)
        print('Set-cookie: session={}'.format(cookie))
    elif wall.find(login):
        pass  # А надо бы предупреждение выдать
    else:
        wall.register(login, password)
        cookie = wall.set_cookie(login)
        print('Set-cookie: session={}'.format(cookie))

pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Стена</title>
</head>
<body>
    Форма логина и регистрации. При вводе несуществующего имени зарегистрируется новый пользователь.
    <form action="/cgi-bin/wall.py">
        Логин: <input type="text" name="login">
        Пароль: <input type="password" name="password">
        <input type="hidden" name="action" value="login">
        <input type="submit">
    </form>

    {posts}

    {publish}
</body>
</html>
'''

if user is not None:
    pub = '''
    <form action="/cgi-bin/wall.py">
        <textarea name="text"></textarea>
        <input type="hidden" name="action" value="publish">
        <input type="submit">
    </form>
    '''
else:
    pub = ''

print('Content-type: text/html\n')

print(pattern.format(posts=wall.html_list(), publish=pub))

Здесь мы используем форматирование строк для формирования страницы (кстати, это первый шаг на пути к созданию собственного шаблонизатора).

Не забудьте дать этому файлу права на выполнение (второму файлу эти права не нужны).

cgi-bin/_wall.py (здесь определены функции publish, login и другие):

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import time


class Wall:
    USERS = 'cgi-bin/users.json'
    WALL = 'cgi-bin/wall.json'
    COOKIES = 'cgi-bin/cookies.json'

    def __init__(self):
        """Создаём начальные файлы, если они не созданы"""
        try:
            with open(self.USERS, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.USERS, 'w', encoding='utf-8') as f:
                json.dump({}, f)

        try:
            with open(self.WALL, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.WALL, 'w', encoding='utf-8') as f:
                json.dump({"posts": []}, f)

        try:
            with open(self.COOKIES, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.COOKIES, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def register(self, user, password):
        """Регистриует пользователя. Возвращает True при успешной регистрации"""
        if self.find(user):
            return False  # Такой пользователь существует
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        users[user] = password
        with open(self.USERS, 'w', encoding='utf-8') as f:
            json.dump(users, f)
        return True

    def set_cookie(self, user):
        """Записывает куку в файл. Возвращает созданную куку."""
        with open(self.COOKIES, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        cookie = str(time.time()) + str(random.randrange(10**14))  # Генерируем уникальную куку для пользователя
        cookies[cookie] = user
        with open(self.COOKIES, 'w', encoding='utf-8') as f:
            json.dump(cookies, f)
        return cookie

    def find_cookie(self, cookie):
        """По куке находит имя пользователя"""
        with open(self.COOKIES, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        return cookies.get(cookie)

    def find(self, user, password=None):
        """Ищет пользователя по имени или по имени и паролю"""
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        if user in users and (password is None or password == users[user]):
            return True
        return False

    def publish(self, user, text):
        """Публикует текст"""
        with open(self.WALL, 'r', encoding='utf-8') as f:
            wall = json.load(f)
        wall['posts'].append({'user': user, 'text': text})
        with open(self.WALL, 'w', encoding='utf-8') as f:
            json.dump(wall, f)

    def html_list(self):
        """Список постов для отображения на странице"""
        with open(self.WALL, 'r', encoding='utf-8') as f:
            wall = json.load(f)
        posts = []
        for post in wall['posts']:
            content = post['user'] + ' : ' + post['text']
            posts.append(content)
        return '<br>'.join(posts)
