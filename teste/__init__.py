#rolul Repository este doar sa implementeze C.R.U.D.E
'''
class Repository:
    def __init__(self):
        self.__entitati = {}

    def getAll(self):


        return list(self.__entitati.values())

    def getById(self, idEntitate):


        #return self.__clienti.get(idClient, None) (1)
        # (1) si (2) sunt echivalente

        if idEntitate in self.__entitati:
            return self.__entitati[idEntitate]         #(2)
        return None


    def adauga(self, entitate):


        if self.getById(entitate.getIdEntitate()) is not None:
            raise KeyError("Exista deja un client cu id-ul dat")
        self.__entitati[entitate.getIdEntitate()] = entitate

    def modifica(self, entitateNoua):


        if self.getById(entitateNoua.getidEntitate()) is None:
            raise KeyError("Nu exista niciun client cu id-ul dat")
        self.__entitati[entitateNoua.getidEntitate()] = entitateNoua

    def sterge(self, idEntitate):

        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista niciun client cu id-ul dat")
        self.__entitati.pop(idEntitate)
        '''