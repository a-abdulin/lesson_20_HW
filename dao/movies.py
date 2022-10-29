from dao.models.movies import Movie


class MovieDao():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)


    def get_by_dir_gen(self, director_id, genre_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id, Movie.genre_id == genre_id).all()

    def get_by_dir(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_gen(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def post_dao_movie(self, movie):
        self.session.add(movie)
        self.session.commit(movie)
        return 'Ok', 201

    def delete_dao_movie(self, movie):
        self.session.delete(movie)
        self.session.commit()
        self.session.close()

    def put_dao_movie(self, movie):
        self.session.add(movie)
        self.session.commit()
        self.session.close()
