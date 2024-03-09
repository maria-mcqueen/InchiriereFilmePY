from domeniu.client import Client
from repository.repository import Repository


def testAdaugaClientRepository():
    clientRepository = Repository()
    client = Client("1", "1", "1")

    clientRepository.adauga(client)

    clienti = clientRepository.getAll()
    assert len(clienti) == 1


    try:
        clientRepository.adauga(client)
        assert False
    except KeyError:
        ...


def testModificaClientRepository():
    clientRepository = Repository()
    client = Client("1", "avegers", "filmfilm")
    client2 = Client("2", "avegers", "filmfilm")
    clientnou1=Client("1", "ironman", "filmfilm")

    clientRepository.adauga(client)
    clientRepository.adauga(client2)

    clientRepository.modifica(client)
    clienti = clientRepository.getAll()
    assert len(clienti) == 2
#    assert clienti[0].getidClient() == "1"
 #   assert clienti[1].getidClient() == "2"

    try:
        clientRepository.modifica(clientnou1)

    except KeyError:
        ...


def teststergeclientrepository():
    clientRepository = Repository()
    client = Client("1", "avegers", "filmfilm")

    clientRepository.adauga(client)

    clientRepository.sterge("1")

    assert  len(clientRepository.getAll()) == 0

    try:
        clientRepository.sterge("!")
        assert False
    except KeyError:
        ...
