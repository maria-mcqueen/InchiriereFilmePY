from teste.testClient import testClient, testClientSetteri
from teste.testClientFilm import testCFilm, testCFilmSetteri
from teste.testEntitate import testEntitate, testEntitateSetteri
from teste.testFilm import testFilm, testFilmSetteri
from teste.testFilmService import testAdaugaService, testModificaService
from teste.testclientRepository import testAdaugaClientRepository, testModificaClientRepository, \
    teststergeclientrepository
from teste.testClientFilmService import testAdaugaCService, testModificaCService ,testStergeService



def testAll():
    testFilm()
    testFilmSetteri()
    testAdaugaService()
    testModificaService()
    testAdaugaClientRepository()
    testModificaClientRepository()
    teststergeclientrepository()
    testClient()
    testClientSetteri()
    testAdaugaCService()
    testEntitate()
    testEntitateSetteri()
    testCFilm()
    testCFilmSetteri()
    #testModificaCService()
    testStergeService()