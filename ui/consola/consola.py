from service.FilmService import FilmService
from service.clientService import ClientService
from service.ClientFilmService import ClientFilmService

class Consola:
    def __init__(self, filmService: FilmService, clientService: ClientService, clientFilmService: ClientFilmService):
        self.__filmService = filmService
        self.__clientService = clientService
        self.__clientFilmService = clientFilmService

    def adaugaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului ")
            titlu = input("Dati titlul filmului ")
            descriere = input("Dati descriere filmului ")
            gen = input("Dati genul filmului ")
            self.__filmService.adauga(idFilm,titlu,descriere,gen)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def modificaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului de modificat ")
            titluNou = input("Dati titlu nou filmului ")
            descriereNou = input("Dati descriere noua filmului ")
            genNou = input("Dati genul nou filmului ")
            self.__filmService.modifica(idFilm,titluNou,descriereNou,genNou)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def sterge(self):
        try:
            idFilm = input("Dati id-ul filmului de sters")
            self.__filmService.stergere(idFilm)
        except KeyError as e:
            print(e)

    def adaugaClient(self):
        try:
            idClient= input("dati id-ul clientului: ")
            nume = input("dati numele clientului: ")
            cnp= int(input("Dati cnp: "))

            self.__clientService.adaugaClient(idClient,nume,cnp)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modificaClient(self):
        try:
            idClient = input("dati id-ul clientului de modificat ")
            numeNou = input("dati numele nou ")
            cnpNou = int(input("Dati cnp nou: "))

            self.__clientService.modificaClient(idClient,numeNou,cnpNou)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def stergeClient(self):
        try:
            idClient = input("dati id-ul clientului de sters ")
            self.__clientService.stergeClient(idClient)
        except KeyError as e:
            print(e)

    def inchiriereFilm(self):
        try:
            idclientFilm = input("dati id ul inchirierii: ")
            idClient = input("dati id ul clientului ")
            idFilm = input("dati id ul filmului ")
            self.__clientFilmService.adaugaInchiriere(idclientFilm,idClient,idFilm)
        except KeyError as e:
            print(e)

    def returnare(self):
        idClient = input("dati id ul clientului:" )
        idFilm = input("dati id ul filmului: ")
        self.__clientFilmService.returnare(idClient,idFilm)

    def ordonareclientidupafilme(self):
        rezultat = self.__clientService.clientiordonatidupafilme()
        self.afiseaza(rezultat)

    def clientiCautatiDupaId(self):
        try:
            idClient= input("dati id ul clientului de cautat")
            rezultat = self.__clientService.cautareClient(idClient)
            print(rezultat)
        except KeyError as e:
            print(e)

    def filmeCautateDupaId(self):
        try:
            idFilm= input("dati id ul filmului de cautat")
            rezultatunu = self.__filmService.cautareFilm(idFilm)
            print(rezultatunu)
        except KeyError as e:
            print(e)

    def CeleMaiInchiriateFilme(self):
        rezultat = self.__filmService.celeMaiCautate()
        self.afiseaza(rezultat)

    def CeleMaiInchiriateClienti(self):
        rezultat = self.__clientService.ceiMaiCautati()
        self.afiseaza(rezultat)

    def afiseaza(self, entitati):
        for entitate in entitati:
            print (entitate)


    def printMeniu(self):
        print("1.Adauga film ")
        print("2.Modifica film ")
        print("3.Stege film ")
        print("4.Adauga client")
        print("5.Modifica client")
        print("6.Sterge client")
        print("7.Adauga inchiriere")
        print("8.Returneaza ")
        print("9.Ordoneaza clientii dupa nr de filme")
        print("10.Cauta un client dupa id ")
        print("11.Afiseaza cele mai cautate filme")
        print("12.Cauta un film dupa id ")
        print("a.Afiseaza filmele ")
        print("c.Afiseaza clientii")
        print("i.Afiseaza toate inchirierile")
        print("x.Iesire ")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("Dati optiunea:")
            if optiune == "1":
                self.adaugaFilm()
            elif optiune == "2":
                self.modificaFilm()
            elif optiune == "3":
                self.sterge()
            elif optiune == "4":
                self.adaugaClient()
            elif optiune == "5":
                self.modificaClient()
            elif optiune == "6":
                self.stergeClient()
            elif optiune == "7":
                self.inchiriereFilm()
            elif optiune == "8":
                self.returnare()
            elif optiune == "9":
                    #self.ordonareclientidupafilme()
                self.afiseazaDTO()
            elif optiune == "10":
                self.clientiCautatiDupaId()
            elif optiune == "11":
                self.CeleMaiInchiriateFilme()
            elif optiune == "12":
                self.filmeCautateDupaId()
            elif optiune =="13":
                self.CeleMaiInchiriateClienti()
            elif optiune == "a":
                self.afiseaza(self.__filmService.getAllFilme())
            elif optiune == "c":
                self.afiseaza(self.__clientService.getAllClienti())
            elif optiune == "i":
                self.afiseaza(self.__clientFilmService.getAllInchirieri())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita")