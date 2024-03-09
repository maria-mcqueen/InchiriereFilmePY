from unittest import TestCase
from domeniu.client import Client

class TestClient(TestCase):
    def test_getnume(self):
        film = Client("1", "avengers", "film")

        assert film.getnume() == "avengers"

    def test_getcnp(self):
        film = Client("1", "avengers", "film")

        assert film.getcnp() == "film"

    def test_setnume(self):
        film = Client("1", "avengers", "film")


        film.setnume("ironman")
        assert film.getnume() == "ironman"

    def test_setcnp(self):
        film = Client("1", "avengers", "film")

        film.setcnp("ironman")
        assert film.getcnp() == "ironman"

    def teststr(self):
        film = Client("1", "avengers", "film")
        assert "id: "+ str(film.getcnp()) + "nume: " + str(film.getnume()) + "cnp: " +str(film.getcnp())

