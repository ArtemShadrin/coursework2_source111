import json
import os


def get_posts_all() -> list[dict]:  # получаем список словарей
    """
    Возвращает все посты
    """
    path = 'data/data.json'
    with open(path, 'r', encoding='utf-8') as file:  # открываем файл на чтение с кодировкой
        return json.load(file)  # Возвращает все посты - V


def get_posts_by_user(user_name) -> list[dict]:  # получаем список словарей
    """
    Возвращает посты определенного пользователя.
    """

    result = []  # создаем список, куда будем записывать результат
    for posts in get_posts_all():  # используем цикл по полученным (всем) постам
        if posts['poster_name'] == user_name:  # сравниваем значение с полученными данными
            result.append(posts)  # фиксируем результат
    return result  # Возвращает посты определенного пользователя


def get_comments_all() -> list[dict]:  # получаем список словарей
    """
    Возвращает все комментарии
    """
    with open('data/comments.json', 'r', encoding='utf-8') as file:  # открываем файл на чтение с кодировкой
        return json.load(file)  # Возвращает все комментарии


def get_comments_by_post_id(post_id) -> list[dict]:  # получаем список словарей
    """
    Возвращает комментарии определенного поста
    """
    result = []  # создаем список, куда будем записывать результат
    for comments in get_comments_all():  # используем цикл по полученным (всем) комментариям
        if comments['post_id'] == post_id:  # сравниваем значение с полученными данными
            result.append(comments)  # фиксируем результат
    return result  # Возвращает комментарии определенного поста


def search_for_posts(query: str) -> list[dict]:  # получаем список словарей
    """
    Возвращает список постов по ключевому слову
    """
    result = []  # создаем список, куда будем записывать результат
    for post in get_posts_all():  # используем цикл по полученным (всем) постам
        if query.lower() in post['content'].lower():  # сравниваем значение с полученными данными
            result.append(post)  # фиксируем результат
    return result  # Возвращает список постов по ключевому слову - V


def get_post_by_pk(pk: int) -> dict:  # получаем словарь
    """
    Возвращает один пост по его идентификатору.
    """
    for post in get_posts_all():  # используем цикл по полученным (всем) постам
        if post['pk'] == pk:  # сравниваем значение с полученными данными
            return post  # Возвращает один пост по его идентификатору - V
