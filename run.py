from flask import Flask

from main.views import main_blueprint

# Создаем экземпляр Flask
app = Flask(__name__)

# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False

# регистрируем блюпринт
app.register_blueprint(main_blueprint)



# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()
