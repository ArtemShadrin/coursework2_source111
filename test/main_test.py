import pytest

from run import app
from utils import get_posts_all, get_post_by_pk

app.testing = True
client = app.test_client()

# Задаем, какие ключи ожидаем получать у кандидата
keys_posts = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_app():
    posts = get_posts_all()
    assert type(posts) == list, "возвращается не список"
    assert len(posts) > 0, "возвращается пустой список"
    assert set(posts[0].keys()) == keys_posts, "неверный список ключей"


def test_get_by_id():
    post_id = get_post_by_pk(1)
    assert type(post_id) == dict, "возвращается не список"
    assert (post_id["pk"] == 1), "возвращается неправильный кандидат"
    assert set(post_id.keys()) == keys_posts, "неверный список ключей"


def test_root_status_posts():
    """ Проверяем, получается ли нужный статус-код и """
    response = app.test_client().get('/api/posts', follow_redirects=True)
    assert response.status_code == 200, "Статус-код всех постов неверный"


def test_root_status_posts_pk():
    """ Проверяем, получается ли нужный статус-код и """
    response = app.test_client().get(f'/api/posts/1', follow_redirects=True)
    assert response.status_code == 200, "Статус-код всех постов неверный"
