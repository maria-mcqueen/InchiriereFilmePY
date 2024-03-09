from unittest import TestCase

from domeniu.film import Film


class TestFilmCoverage(TestCase):
    def test_gettitlu(self):
        film = Film("1", "avengers", "film", "sf")

        assert film.gettitlu() == "avengers"

    def test_getdescriere(self):
        film = Film("1", "avengers", "film", "sf")

        assert film.getdescriere() == "film"

    def test_getgen(self):
        film = Film("1", "avengers", "film", "sf")

        assert film.getgen() == "sf"

    def test_settitlu(self):
        film = Film("1", "avengers", "film", "sf")

        film.settitlu("ironman")
        assert film.gettitlu() == "ironman"

    def test_setdescriere(self):
        film = Film("1", "avengers", "film", "sf")

        film.setdescriere("film")
        assert film.getdescriere() == "film"

    def test_setgen(self):
        film = Film("1", "avengers", "film", "sf")

        film.setgen("sf")
        assert film.getgen() == "sf"

