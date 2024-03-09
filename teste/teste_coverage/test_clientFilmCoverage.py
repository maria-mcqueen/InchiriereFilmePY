from unittest import TestCase

from domeniu.clientFilm import clientFilm


class TestclientFilmCoverage(TestCase):
    def test_get_id_client(self):
        film = clientFilm("1", "avengers", "film")

        assert film.getIdEntitate() == "1"

    def test_get_id_film(self):
        film = clientFilm("2", "avengers", "film")

        assert film.getIdEntitate() == "2"

    def test_set_id_client(self):
        film = clientFilm("1", "avengers", "film")

        film.setIdEntitate("2")
        assert film.getIdEntitate() == "2"

    def test_set_id_film(self):
        film = clientFilm("1", "avengers", "film")

        film.setIdEntitate("2")
        assert film.getIdEntitate() == "2"
