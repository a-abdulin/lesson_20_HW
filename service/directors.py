

class DirectorService:
    def __init__(self, director_dao: object) -> object:
        self.director_dao = director_dao

    def get_directors(self):
        return self.director_dao.get_all()

    def get_director(self, did):
        return self.director_dao.get_one(did)

