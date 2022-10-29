# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

from flask import Flask
from flask_restx import Api

from config import Config
from dao.models.directors import Director
from dao.models.genres import Genre
from dao.models.movies import Movie
from setup_db import db

from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)

    create_data(app, db)


# функция
def create_data(app, db):
    with app.app_context():
        db.create_all()
        m1 = Movie(id=1, title="Гарри Поттер и Тайная Комната", description="Джоан Роулинг", trailer = 111, year=1990, rating=400, genre_id = 1, director_id = 1)
        m2 = Movie(id=2, title="Граф Монте-Кристо", description="Дюма", trailer = 123, year=1510, rating=1344, genre_id = 2, director_id = 1)
        m3 = Movie(id=3, title="Гарри Поттер и Орден Феникса", description="Джоан Роулинг", trailer = 134, year=1993, rating=500, genre_id = 1, director_id = 2)
        m4 = Movie(id=4, title="Гарри Поттер и Кубок Огня", description="Джоан Роулинг", trailer = 333, year=1994, rating=600, genre_id = 2, director_id = 2)
#
        g1 = Genre(id=1, name="Comedy")
        g2 = Genre(id=2, name="Shit")

        d1 = Director(id=1, name="Hulio Gonzales")
        d2 = Director(id=2, name="Vasyliy Petrovich")

#         # создать несколько сущностей чтобы добавить их в БД
#
        with db.session.begin():
            db.session.add_all([m1, m2, m3, m4])
            db.session.add_all([g1, g2])
            db.session.add_all([d1, d2])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)

