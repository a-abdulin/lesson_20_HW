from flask_restx import Namespace, Resource

from containers import director_service
from dao.models.directors import DirectorSchema

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_directors()
        return directors_schema.dump(directors), 200


@directors_ns.route('/<did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_director(did)
        return director_schema.dump(director), 200

