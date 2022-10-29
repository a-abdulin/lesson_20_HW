from flask import request

from dao.models.movies import Movie


class MovieService:
    def __init__(self, moviedao):
        self.moviedao = moviedao

    def get_movies(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if director_id is not None and genre_id is not None:
            movies = self.moviedao.get_by_dir_gen(director_id, genre_id)
        elif director_id is not None:
            movies = self.moviedao.get_by_dir(director_id)
        elif genre_id is not None:
            movies = self.moviedao.get_by_gen(genre_id)
        elif year is not None:
            movies = self.moviedao.get_by_year(year)
        else:
            movies = self.moviedao.get_all()
        return movies

    def get_movie(self, mid):
        return self.moviedao.get_one(mid)


    def post_movie(self):
        data = request.json
        data.pop('id', None)
        try:
            movie = Movie(**data)
            self.moviedao.post_movie(movie)
        except Exception:
            return 'Failed to insert director', 400


    def delete_movie(self, mid):
        movie_delete = Movie.query.get(mid)
        self.moviedao.delete_dao_movie(movie_delete)
        return 'Ok', 204

    def put_movie(self, mid):
        get_movie_put = request.json
        movie_update = Movie.query.get(mid)
        movie_update.name = get_movie_put.get('name')
        movie_update.title = get_movie_put.get('title')
        movie_update.description = get_movie_put.get('description')
        movie_update.trailer = get_movie_put.get('trailer')
        movie_update.year = get_movie_put.get('year')
        movie_update.rating = get_movie_put.get('rating')
        movie_update.genre_id = get_movie_put.get('genre_id')
        movie_update.director_id = get_movie_put.get('director_id')
        self.moviedao.put_dao_movie(movie_update)
        return 'Ok'


