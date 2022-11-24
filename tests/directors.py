import os
import pytest
from unittest.mock import MagicMock

from dao.models.directors import Director
from dao.directors import DirectorDao
from service.directors import DirectorService


@pytest.fixture(autouse=True)
def director_dao():
    director_dao = DirectorDao(None)

    d1 = Director(id=1, name='Phill')
    d2 = Director(id=2, name='John')

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()
    return director_dao


class TestDirectorsServices:
    @pytest.fixture(autouse=True)
    def director_services(self, director_dao):
        self.director_services = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director != None
        assert director.id == 1

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0
        assert directors is not None
