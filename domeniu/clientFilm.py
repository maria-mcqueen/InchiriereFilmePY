from domeniu.entitate import Entitate


class clientFilm(Entitate):
    def __init__(self, idclientFilm , idClient, idFilm):
        super().__init__(idclientFilm)
        self.__idClient = idClient
        self.__idFilm = idFilm

    def getIdClient(self):
        return self.__idClient

    def getIdFilm(self):
        return self.__idFilm

    def setIdClient(self, idClient):
        self.__idClient = idClient

    def setIdFilm(self, idFilm):
        self.__idFilm = idFilm

    def __str__(self):
        return f'id: {self.getIdEntitate()}, id client: {self.__idClient}, id film: {self.__idFilm}'