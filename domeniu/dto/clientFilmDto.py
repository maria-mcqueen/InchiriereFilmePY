from dataclasses import dataclass

from domeniu import film


@dataclass
class ClientSortareDto:
    def __init__(self, id, nume, cnp):
        super().__init__(id)
        self.__nume = nume
        self.__cnp = cnp

    nume : str
    cnp : str
    nrFilme : int

@dataclass()
class FilmSortareDto:
    titlu : str
    nrClienti : str

@dataclass()
class FilmSortareDto:
    filme : str
    inchirieri : str


@dataclass()
class clientInchirieriDTO:
    numeClient: str
    nrinchirieri: int

class ClientdtoAssembler:
    @staticmethod
    def createClientAssemblerDTO(client, inchirieri):
        numeClient = client.getnume()
        nrinchirieri = len(inchirieri)
        return clientInchirieriDTO(numeClient, nrinchirieri)


@dataclass()
class filmInchirieriDTO():
    titluFilm: str
    nrinchirieri: int


class FilmdtoAssembler:
    @staticmethod
    def createFilmAssemblerDTO(film, inchirieri):
        titluFilm= film.gettitlu()
        nrInchirieri = len(inchirieri)
        return filmInchirieriDTO(titluFilm, nrInchirieri)


@dataclass()
class ClientFilmDTO:
    numeClient: str
    titluFilm: str

class ClientFilmDTOAssembler:
    @staticmethod
    def creaza(client, film):
        numeClient = client.getnume()
        titluFilm = film.gettitlu()
        return ClientFilmDTO(numeClient, titluFilm)

@dataclass()
class FilmeInchirieriDTO:
    titluFilm: str
    nrinchirieri: int

class FilmInchirieriDTOAssembler:
    @staticmethod
    def creaza(film, inchirieri):
        titluFilm = film.gettitlu()
        nrinchirieri = len(inchirieri)
        return FilmeInchirieriDTO(titluFilm, nrinchirieri)

