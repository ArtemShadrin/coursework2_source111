import logging

from json import JSONDecodeError

from flask import Blueprint, render_template, request, jsonify

from utils import get_post_by_pk, get_comments_by_post_id, get_posts_all, search_for_posts, get_posts_by_user

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создаем или получаем новый логгер
logger_one = logging.getLogger("one")
# Logging.INFO
logger_one.setLevel('INFO')
# Cоздаем ему обработчик
file_handler = logging.FileHandler('logs/api.log', encoding='UTF-8')
# Создаем новое форматирование (объект класса Formatter)
formatter_one = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
# Применяем форматирование к обработчику
file_handler.setFormatter(formatter_one)
# Добавляем обработчик к журналу
logger_one.addHandler(file_handler)


# Get /api/posts


@main_blueprint.route('/api/posts')
def get_json_posts():
    logger_one.info("Запрос /api/posts")
    posts = get_posts_all()
    return jsonify(posts)


# Get /api/posts/<post_id>

@main_blueprint.route('/api/posts/<int:pk>')
def get_json_post_id(pk):
    logger_one.info(f"Запрос /api/posts/{pk}")
    post_id = get_post_by_pk(pk)
    return jsonify(post_id)


@main_blueprint.route('/')
def main_page():
    posts = get_posts_all()
    count_posts = len(posts)
    return render_template('index.html', posts=posts, count_posts=count_posts)


@main_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    try:
        post = get_post_by_pk(post_id)
        comments = get_comments_by_post_id(post_id)
        count_comments = len(comments)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)


@main_blueprint.route('/search/')
def search_page():
    try:
        query = request.args.get('s', '')
        posts = search_for_posts(query)
        count_posts = len(posts)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    return render_template('search.html', posts=posts, count_posts=count_posts)


@main_blueprint.route('/users/<username>')
def user_page(username):
    try:
        post_user = get_posts_by_user(username)
        count_post_user = len(post_user)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    return render_template('user-feed.html', posts=post_user, count_post_user=count_post_user)
