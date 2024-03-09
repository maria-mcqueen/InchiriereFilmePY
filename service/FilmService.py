#doar cerintele din enuntul problemei, nu mai faci inca o data ce ai facut in repository
from domeniu import film
from domeniu.film import Film
from repository.repository import Repository



class FilmService:
    def __init__(self, filmRepository: Repository, clientFilmRepository: Repository):
        self.__FilmRepository = filmRepository
        self.__clientFilmRepository = clientFilmRepository

    def getAllFilme(self):
        '''
        returneaza o lista de filme
        :return: o lista de obiecte de tipul Film
        '''

        return self.__FilmRepository.getAll()

    def adauga(self, idFilm, titlu,descirere,gen):
        '''
        adauga un film
        :param idFilm: string
        :param titlu: string
        :param descirere: string
        :param gen: string
        :return:
        '''
        film = Film(idFilm, titlu, descirere,gen)
        self.__FilmRepository.adauga(film)


    def modifica(self, idFilm, titluNou, descrierenou, genNou):
        '''
        modifica un film dupa id
        :param idFilm: string
        :param titluNou: string
        :param descrierenou: string
        :param genNou: string
        :return:
        '''
        filmNou = Film(idFilm,titluNou,descrierenou,genNou)
        self.__FilmRepository.modifica(filmNou)


    def stergere(self, idFilm):
        
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdFilm() == idFilm:
                self.__clientFilmRepository.sterge(inchiriere.getIdEntitate())

        self.__FilmRepository.sterge(idFilm)

    def celeMaiCautate(self):
        filmeinchiriate={}
        inchirieri = self.__clientFilmRepository.getAll()
        maxId=0
        max=0
        l=[]
        for inchiriere in inchirieri:
            if inchiriere.getIdFilm in filmeinchiriate:
                filmeinchiriate[inchiriere.getIdFilm()] +=1
                if int(filmeinchiriate[inchiriere.getIdFilm()]) > int(max):
                    maxId = int(inchiriere.getIdFilm())
                    max = int(filmeinchiriate[inchiriere.getIdFilm()])

            else:
                filmeinchiriate[inchiriere.getIdFilm()] = 1
                if int(filmeinchiriate[inchiriere.getIdFilm()]) > int(max):
                    maxId = int(inchiriere.getIdFilm())
                    max = int(filmeinchiriate[inchiriere.getIdFilm()])
        for inchiriere in inchirieri:
            if filmeinchiriate[inchiriere.getIdFilm()] == max:
                filmeinchiriate[inchiriere.getIdFilm()] = 0
                l.append(inchiriere.getIdFilm())
        return l




    def cautareFilm(self, idFilm):

        filmcautat= self.__FilmRepository.getById(idFilm)
        return filmcautat





