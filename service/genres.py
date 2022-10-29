class GenreService:
    def __init__(self, genredao):
        self.genredao = genredao

    def get_genres(self):
        return self.genredao.get_all()

    def get_genre(self, gid):
        return self.genredao.get_one(gid)
