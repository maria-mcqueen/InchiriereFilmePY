from domeniu.entitate import Entitate


class Client(Entitate):
    def __init__(self, idClient, nume, cnp):

        #relatie de 1 la n intre entitati, adica un client poate inchiria mai multe filme
        #dar un film poate fi inchiriat doar la o persoana o data, nu exista mai multe
        #exemplare de acelasi film gen

        super().__init__(idClient)
        self.__nume = nume
        self.__cnp = cnp


    def getnume(self):
        return self.__nume

    def getcnp(self):
        return self.__cnp

    def setnume(self, nume):
        self.__nume = nume

    def setcnp(self, cnp):
        self.__cnp = cnp

    def __str__(self):
        return f"id: {self.getIdEntitate()}, nume: {self.__nume}, cnp: {self.__cnp}"