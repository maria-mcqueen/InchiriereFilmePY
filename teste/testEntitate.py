from domeniu.entitate import Entitate


def testEntitate():
    film = Entitate("1")

    assert film.getIdEntitate() == "1"


def testEntitateSetteri():
    film = Entitate("1")

    film.setIdEntitate("2")
    assert film.getIdEntitate() == "2"

