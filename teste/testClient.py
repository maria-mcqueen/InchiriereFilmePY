from domeniu.client import Client


def testClient():
    film = Client("1", "avengers","film")

    assert film.getIdEntitate() == "1"
    assert film.getnume() == "avengers"

def testClientSetteri():
    film = Client("1", "avengers","film")

    film.setIdEntitate("2")
    assert film.getIdEntitate() == "2"

    film.setnume("ironman")
    assert  film.getnume() == "ironman"