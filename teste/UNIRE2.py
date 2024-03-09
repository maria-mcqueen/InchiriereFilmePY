from domeniu.client import Client
from domeniu.clientFilm import clientFilm
from domeniu.entitate import Entitate
from domeniu.film import Film
from repository.repository import Repository
from service.clientService import ClientService
from service.FilmService import FilmService


def testClient():
    client = Client("1", "Popescu Maria", "6070917234")

    assert client.getIdEntitate() == "1"
    assert client.getnume() == "Popescu Maria"
    assert client.getcnp() == "6070917234"

def testClientSetteri():
    client = Client("2", "Popescu Maria", "6070917234")

    client.setIdEntitate("2")
    assert client.getIdEntitate() == "2"

    client.setnume("Popa Paul")
    assert client.getnume() == "Popa Paul"

    client.setcnp("6070917294")
    assert client.getcnp() == "6070917294"

def test_str_client():
    client = Client("1", "Mara", "8945")
    assert ("id: " + str(client.getIdEntitate()) + "nume: " + str(client.getnume()) + "CNP: " + str(client.getcnp())) == ("id: " + "1" + "nume: " + "Mara" + "CNP: " + "8945")

def testFilm():
    film = Film("1", "Pe aripile vantului", "film bun", "drama")

    assert film.getIdEntitate() == "1"
    assert film.gettitlu() == "Pe aripile vantului"
    assert film.getdescriere() == "film bun"
    assert film.getgen() == "drama"

def testFilmSetteri():
    film = Film("1" ,"Pe aripile vantului", "film bun", "drama")

    film.setIdEntitate("2")
    assert film.getIdEntitate() == "2"

    film.settitlu("Downfall")
    assert film.gettitlu() == "Downfall"

    film.setdescriere("film la fel de bun")
    assert film.getdescriere() == "film la fel de bun"

    film.setgen("istoric")
    assert film.getgen() == "istoric"

def test_str_film():
    film = Film(1, "Stalingrad", "istoric", "ok")
    assert "id: " + str(film.getIdEntitate()) + "titlu: " + str(film.gettitlu()) + "descriere: " + str(film.getdescriere()) + "gen: " + str(film.getgen())

def testEntitate():
    entitate = Entitate("1")

    assert entitate.getIdEntitate() == "1"


def testEntitateSetteri():
    entitate = Entitate("2")

    entitate.setIdEntitate("2")
    assert entitate.getIdEntitate() == "2"




def testAdaugaClientService():
    clientRepository = Repository()
    clientFilmRpository = Repository()
    clientService = ClientService(clientRepository, clientFilmRpository)
    clientService.adauga("1", "Popescu Maria", "6070917234")

    clienti = clientService.getAllClienti()
    assert len(clienti) == 1
    assert clienti[0].getIdEntitate() == "1"
'''
    try:
        clientService.adauga("1", "Pop Ioan", "6070917238")
        assert False
    except KeyError:
        ...
'''
def testModificaClientService():
    clientRepository = Repository()
    clientFilmRpository = Repository()
    clientService = ClientService(clientRepository, clientFilmRpository)
    clientService.adauga("1", "Popescu Maria", "6070917234")

    clientService.modifica("1", "Pop Ioana", "6070917354")

    clienti = clientService.getAllClienti()
    assert clienti[0].getNume() == "Pop Ioana"

    #try:
     #   clientService.modifica("2", "Popa Elena", "6070917266")
      #  assert False
    #except KeyError:
      #  ...

def testOrdoneazaClientiDupaNume():
    clientRepository = Repository()
    clientFilmRpository = Repository()
    clientService = ClientService(clientRepository, clientFilmRpository)
    clientService.adauga("1", "Popa Elena", "6070917234")

    clientService.adauga("2", "Barbu Mara", "6090000000")

    clientService.ordoneazaClientiDupaNume()

    clienti = clientService.getAllClienti()
    assert clienti[1].getNume() == "Barbu Mara"

def testAdaugaFilmSevice():
    filmRepository = Repository()
    clientFilmRpository = Repository()
    #filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, clientFilmRpository) #filmValidator)
    filmService.adauga("1", "Stalingrad", "film despre batalia de la Stalingerad", "istoric")

    filme = filmService.getAllFilme()
    assert len(filme) == 1
    assert filme[0].getIdEntitate() == "1"

    #try:
    #    filmService.adaugaFilm("1", "Ziua Z", "film despre debarcarea din Normandia", "istoric")
    #    assert False
    #except KeyError:
    #    ...

def testModificaFilmService():
    filmRepository = Repository()
    clientFilmRpository = Repository()
    #filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, clientFilmRpository) #filmValidator)
    filmService.adauga("1", "Stalingrad", "film despre batalia de la Stalingerad", "istoric")

    filmService.modifica("1", "Moartea lui Stalin", "film despre URSS", "istoric")

    filme = filmService.getAllFilme()
    assert filme[0].getTitlu() == "Moartea lui Stalin"

    #try:
    #    filmService.modificaFilm("2", "Look who's back", "film", "comedie")
    #    assert False
    #except KeyError:
    #    ...

def testAdaugaRepository():
    entitateRepository = Repository()
    entitate = Entitate("1")

    entitateRepository.adauga(entitate)

    entitati = entitateRepository.getAll()
    assert len(entitati) == 1
    assert entitati[0].getIdEntitate() == "1"

    try:
        entitateRepository.adauga(entitate)
    except :
        ...



def testModificaRepository():
    entitateRepository = Repository()
    entitate = Entitate("1")
    entitateNoua = Entitate("1")
    entitateNoua2 = Entitate("2")
    entitateRepository.adauga(entitate)

    entitateRepository.modifica(entitateNoua)

    entitati = entitateRepository.getAll()
    assert entitati[0].getIdEntitate() == "1"

    try:
        entitateRepository.modifica(entitateNoua2)

    except KeyError:
        ...

def testStergeRepository():
    entitateRepository = Repository()
    entitate = Entitate("1")
    entitate1 = Entitate("2")
    entitateRepository.adauga(entitate)

    entitateRepository.sterge("1")

    assert len(entitateRepository.getAll()) == 0

    try:
        entitateRepository.sterge(entitate1)

    except KeyError:
        ...