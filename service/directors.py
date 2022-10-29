

class DirectorService:
    def __init__(self, directordao):
        self.directordao = directordao

    def get_directors(self):
        return self.directordao.get_all()

    def get_director(self, did):
        return self.directordao.get_one(did)

