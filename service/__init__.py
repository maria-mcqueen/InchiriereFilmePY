'''celeMaiFilme = {}

        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdFilm() in celeMaiFilme:
                celeMaiFilme[inchiriere.getIdFilm()] += 1
            else:
                celeMaiFilme[inchiriere.getIdClient()] = 1

        idFilmeCautate = sorted(celeMaiFilme)

        return idFilmeCautate'''