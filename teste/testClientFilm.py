from domeniu.clientFilm import clientFilm


def testCFilm():
    film = clientFilm("1", "avengers","film")

    assert film.getIdEntitate() == "1"


def testCFilmSetteri():
    film = clientFilm("1", "avengers","film")

    film.setIdEntitate("2")
    assert film.getIdEntitate() == "2"

