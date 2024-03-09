


class Repository:
    def __init__(self):
        self._entitati = {}

    def getAll(self):

        return list(self._entitati.values())

    def getById(self, idEntitate):


        if idEntitate in self._entitati:
            return self._entitati[idEntitate]
        return None

    def adauga(self, entitate):

        if self.getById(entitate.getIdEntitate()) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat!")
        self._entitati[entitate.getIdEntitate()] = entitate

    def modifica(self, entiateNoua):

        if self.getById(entiateNoua.getIdEntitate()) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self._entitati[entiateNoua.getIdEntitate()] = entiateNoua

    def sterge(self, idEntitate):

        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self._entitati.pop(idEntitate)

