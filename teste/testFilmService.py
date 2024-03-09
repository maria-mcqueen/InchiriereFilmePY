from repository import repository
from repository.repository import Repository

from service.FilmService import FilmService


def testAdaugaService():
    filmRepository = Repository()
    filmService = FilmService(filmRepository, Repository)

    filmService.adauga("1","got","joc","sf")

    filme = filmService.getAllFilme()


    try:
        filmService.adauga("1","lotr","joc","sf")
        assert False
    except KeyError:
        ...

def testModificaService():
    filmRepository = Repository()
    filmService = FilmService(filmRepository, Repository)

    filmService.adauga("1", "got", "joc", "sf")

    filmService.modifica("1", "lotr", "joc", "sf")
    filme = filmService.getAllFilme()

    assert filme[0].gettitlu() == "lotr"
    assert (len(filme) == 1)
    try:
        filmService.modifica("2","lotr","joc","sf")
        assert False
    except KeyError:
        ...

def testStergeService():
    filmRepository = Repository()
    filmService = FilmService(filmRepository, Repository)

    filmService.adauga("1", "got", "joc", "sf")
    filmService.stergere("1")
    filme = filmService.getAllFilme()
    assert (len(filme) == 0)
    try:
        filmService.stergere("1")
        assert False
    except KeyError:
        ...
def testCeleMaiCautate():
    filmRepository = Repository()
    filmService = FilmService(filmRepository, Repository)

    filmService.adauga("1", "got", "joc", "sf")
    filmService.adauga("2", "gots", "joc", "sfi")
    filmService.adauga("3", "gotr", "joc", "sf")

    
