from flask_restx import Namespace, Resource

from containers import genre_service
from dao.models.genres import GenreSchema

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_genres()
        return genres_schema.dump(genres), 200


@genres_ns.route('/<gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_genre(gid)
        return genre_schema.dump(genre), 200

