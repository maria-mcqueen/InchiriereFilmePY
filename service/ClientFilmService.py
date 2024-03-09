from domeniu.clientFilm import clientFilm
from repository.repository import Repository
from domeniu.dto.clientFilmDto import FilmSortareDto, ClientSortareDto, ClientFilmDTOAssembler, \
    FilmInchirieriDTOAssembler


class ClientFilmService:
    def __init__(self, clientFilmRepository: Repository, clientRepository: Repository, filmRepository: Repository):
        self.__clientFilmRepository = clientFilmRepository
        self.__clientRepository = clientRepository
        self.__filmRepository = filmRepository

    def adaugaInchiriere(self, idclientFilm, idClient, idFilm):
        if self.__clientRepository.getById(idClient) is None:
            raise  KeyError("nu exis un client cu id ul dat lmao")
        if self.__filmRepository.getById(idFilm) is None:
            raise  KeyError("nu exis un film cu id ul dat lmao")

        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() == idClient and inchiriere.getIdFilm() == idFilm:
                raise KeyError("clientul a inchiriat deja filmul")

        inchiriere = clientFilm(idclientFilm, idClient, idFilm)
        self.__clientFilmRepository.adauga(inchiriere)

    def getAllInchirieri(self):
        return self.__clientFilmRepository.getAll()

    def returnare(self, idClient, idFilm):
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() == idClient and inchiriere.getIdFilm() == idFilm:
                self.__clientFilmRepository.sterge(inchiriere.getIdEntitate())

    '''def getAllInchirieriSortByNumeClientNrFilmeDTO(self, clienti, inchirieri):
        rezultat = {}
        for client in clienti:
            nrFilme = 0
            for inchiriere in inchirieri:
                if client.getIdEntitate() == inchiriere.getIdClient():
                    nrFilme = nrFilme + 1
            rezultat[client.getIdEntitate()] = ClientSortareDto(client.getNume(), nrFilme)
        return rezultat.values()'''

    '''def getAllInchirieriSortByNumeFilmDTO(self, inchirieri, filme):
        
        rezultatFilme = {}
        for film in filme:
            nrClienti = 0
            for inchiriere in inchirieri:
                if film.getIdEntitate() == inchiriere.getIdFilm():
                    nrClienti += 1
            rezultatFilme[film.getIdEntitate()] = FilmSortareDto(film.gettitlu(), nrClienti)
        return rezultatFilme.values()'''

    def creazaDTO(self):
        inchirieri = self.getAllInchirieri()
        l=[]
        for inchiriere in inchirieri:
            client = self.__clientRepository.getById(inchiriere.getIdClient)
            film = self.__filmRepository.getById(inchiriere.getIdFilm)
            clientFilmDTO = ClientFilmDTOAssembler.creaza(client,film)
            l.append(clientFilmDTO)
        return l

    def ordoneazaDTO(self):
        l = self.creazaDTO()
        l.sort(key = lambda obiect: obiect.titluFilm)
        return l

    def creazaDTO2(self):
        inchirieri = self.getAllInchirieri()
        l={}
        for inchiriere in inchirieri:
            if inchiriere.getIdFilm in l:
                l[inchiriere.getIdFilm()].append(inchiriere.getIdClient())
            else:
                l[inchiriere.getIdFilm()] = []
                l[inchiriere.getIdFilm()].append(inchiriere.getIdClient())

        dto=[]
        for i in l:
            film = self.__filmRepository.getById(i)
            cid = FilmInchirieriDTOAssembler.creaza(film, l[i])
            dto.append(cid)
        return dto

    def ordoneazaDTO2(self):
        l= self.creazaDTO2()
        l.sort(key =lambda i: i.nrinchirieri, reverse = True)
        lmax=[]
        lmax.append(l[0])
        for i in range(1,len(l)):
            if l[i].nrinchirieri == lmax[0].nrinchirieri:
                lmax.append(l[i])
        return lmax