from flask_restx import Resource, Namespace

from containers import movie_service
from dao.models.movies import MovieSchema

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_movies()
        return movies_schema.dump(movies), 200

    def post(self):
        movie_service.post_movie()
        return '', 201


@movies_ns.route('/<mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_movie(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        movie_service.put_movie(mid)
        return 'Ok', 200

    def delete(self, mid):
        movie_service.delete_movie(mid)
        return '', 204


