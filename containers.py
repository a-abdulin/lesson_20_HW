from dao.directors import DirectorDao
from dao.genres import GenreDao
from dao.movies import MovieDao
from service.directors import DirectorService
from service.genres import GenreService
from service.movies import MovieService
from setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)
