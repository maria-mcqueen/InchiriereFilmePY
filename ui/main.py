from repository.fileRepository import FileClientRepository
from repository.filmfileRepository import FileFilmRepository
from repository.repository import Repository
from service.FilmService import FilmService
from service.clientService import ClientService
from teste.testAll import testAll
from ui.consola.consola import Consola
from service.ClientFilmService import ClientFilmService

def main():
    #testAll()


    filmFileRepository = FileFilmRepository('filme.txt')
    clientFileRepository = FileClientRepository('clienti.txt')
    clientFilmRepository = Repository()


    clientService= ClientService(clientFileRepository,clientFilmRepository)
    filmService = FilmService(filmFileRepository,clientFilmRepository)
    clientFilmService = ClientFilmService(clientFilmRepository, clientFileRepository, filmFileRepository)

    consola = Consola(filmService,clientService,clientFilmService)

    consola.meniu()

main()
