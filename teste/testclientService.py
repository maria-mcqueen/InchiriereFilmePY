from repository.repository import Repository
from service.clientService import ClientService


def testAdaugaCService():
    clientRepository = Repository()
    clientService = ClientService(clientRepository,Repository)

    clientService.adaugaClient("1","got","joc")

    clienti = clientService.getAllClienti()


    try:
        clientService.adaugaClient("1","lotr","joc")
        assert False
    except KeyError:
        ...

def testModificaCService():
    clientRepository = Repository()
    clientService = ClientService(clientRepository,Repository)

    clientService.adaugaClient("1", "got", "joc")

    clientService.modificaClient("1", "lotr", "joc")
    clienti = clientService.getAllClienti()

    assert clienti[0].gettitlu() == "lotr"
    assert (len(clienti) == 1)
    try:
        clientService.modificaClient("2","lotr","joc")
        assert False
    except KeyError:
        ...

def testStergeService():
    clientRepository = Repository()
    clientService = ClientService(clientRepository,Repository)

    clientService.adaugaClient("1", "got", "joc")
    clientService.stergeClient("1")
    clienti = clientService.getAllClienti()
    assert (len(clienti) == 0)
    try:
        clientService.stergeClient("1")
        assert False
    except KeyError:
        ...

