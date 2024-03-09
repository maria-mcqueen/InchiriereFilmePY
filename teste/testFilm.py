from domeniu.film import Film


def testFilm():
    film = Film("1", "avengers","film","sf")

    assert film.getIdEntitate() == "1"
    assert film.gettitlu() == "avengers"

def testFilmSetteri():
    film = Film("1", "avengers","film","sf")

    film.setIdEntitate("2")
    assert film.getIdEntitate() == "2"

    film.settitlu("ironman")
    assert  film.gettitlu() == "ironman"