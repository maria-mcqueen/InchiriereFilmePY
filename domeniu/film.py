from domeniu.entitate import Entitate


class Film(Entitate):
    def __init__(self, idFilm, titlu,descriere,gen):
        super().__init__(idFilm)
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def gettitlu(self):
        return self.__titlu

    def getdescriere(self):
        return self.__descriere

    def getgen(self):
        return self.__gen

    def settitlu(self, titlu):
        self.__titlu = titlu

    def setdescriere(self, descriere):
        self.__descriere = descriere

    def setgen(self, gen):
        self.__gen = gen

    def __str__(self):
        return f"id: {self.getIdEntitate()}, titlu: {self.__titlu}, descriere: {self.__descriere}, gen: {self.__gen}"