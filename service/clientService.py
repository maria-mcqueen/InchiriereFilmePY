from domeniu.client import Client
from repository.repository import Repository



class ClientService:
    def __init__(self, clientRepository: Repository, clientFilmRepository: Repository):
        self.__clientRepository = clientRepository
        self.__clientFilmRepository = clientFilmRepository

    def getAllClienti(self):
        '''
        returneaza o lista de clienti
        :return: o lista de obiecte de tipul Client
        '''
        return self.__clientRepository.getAll()

    def adaugaClient(self, idClient,nume,cnp):
        '''
        adauga un client in lista
        :param idClient: string
        :param nume:string
        :param cnp:nr natural
        :param idFilm:string
        :return:
        '''

        client = Client(idClient,nume,cnp)
        self.__clientRepository.adauga(client)

    def modificaClient(self,idClient,numeNou,cnpNou):
        

        client = Client(idClient,numeNou,cnpNou)
        self.__clientRepository.modifica(client)

    def stergeClient(self,idClient):
        
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() == idClient:
                self.__clientFilmRepository.sterge(inchiriere.getIdEntitate())

        self.__clientRepository.sterge(idClient)


    def clientiordonatidupafilme(self):
        clientidupafilme ={}
        inchirieri = self.__clientFilmRepository.getAll()

        for inchiriere in inchirieri:
            if inchiriere.getIdClient() in clientidupafilme:
                clientidupafilme[inchiriere.getIdClient()] += 1
            else:
                clientidupafilme[inchiriere.getIdClient()] = 1

        idClientiordonati = sorted(clientidupafilme, key=lambda idClient: clientidupafilme[idClient])

        clientiordonati = []
        for idClient in idClientiordonati:
            #clientiordonati.append((self.__clientRepository.getById(idClient),clientidupafilme[idClient]))
            clientiordonati.append((idClient, clientidupafilme[idClient]))


        return clientiordonati

    def cautareClient(self, idClient):

        clientcautat = self.__clientRepository.getById(idClient)
        return clientcautat

    def treizecilasuta(self):
        clientidupafilme = {}
        inchirieri = self.__clientFilmRepository.getAll()

        for inchiriere in inchirieri:
            if inchiriere.getIdClient() in clientidupafilme:
                clientidupafilme[inchiriere.getIdClient()] += 1
            else:
                clientidupafilme[inchiriere.getIdClient()] = 1

        idClientiordonati = sorted(clientidupafilme, key=lambda idClient: clientidupafilme[idClient])

        clientiordonati = []
        for idClient in idClientiordonati:
            # clientiordonati.append((self.__clientRepository.getById(idClient),clientidupafilme[idClient]))
            clientiordonati.append((idClient, clientidupafilme[idClient]))


def ceiMaiCautati(self):
        clientiinchiriate={}
        inchirieri = self.__clientFilmRepository.getAll()
        maxId=0
        max=0
        l=[]
        for inchiriere in inchirieri:
            if inchiriere.getIdClient in clientiinchiriate:
                clientiinchiriate[inchiriere.getIdClient()] +=1
                if int(clientiinchiriate[inchiriere.getIdClient()]) > int(max):
                    maxId = int(inchiriere.getIdClient())
                    max = int(clientiinchiriate[inchiriere.getIdClient()])

            else:
                clientiinchiriate[inchiriere.getIdClient()] = 1
                if int(clientiinchiriate[inchiriere.getIdClient()]) > int(max):
                    maxId = int(inchiriere.getIdClient())
                    max = int(clientiinchiriate[inchiriere.getIdClient()])
        for inchiriere in inchirieri:
            if clientiinchiriate[inchiriere.getIdClient()] == max:
                clientiinchiriate[inchiriere.getIdClient()] = 0
                l.append(inchiriere.getIdClient())


        return l
