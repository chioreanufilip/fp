class Controller:
    def __init__(self, repo):
        self.repo = repo

    def add_thing(self, thing): #fugt eine neue Klasse in einer Datei
        self.repo.add(thing)
        self.repo.save()
        # print(self.repo)

    def delete(self, item): #loescht den Item
        # self.repo.convert_to_string([item])
        self.repo.loeschen(self.repo, item)

    def aktualisieren1(self, id_zu_aktualisieren, new, what_needs_change):
        self.repo.aktualisieren(self.repo, id_zu_aktualisieren, new, what_needs_change)

    def redoing_history(self): #zeigt die klassen die geloescht wurden
        lista_obiecte = self.repo.convert_from_string()
        for item in lista_obiecte:
            print(item)

    def bring_back_the_dead(self, id, file): #fuegt ein von der User geloeschtes Instanz zuruck in der menu
        from laborator_5.ui import id_generator
        lista_obiecte = self.repo.convert_from_string()
        for item in lista_obiecte:
            if item.id == id:
                item.id = id_generator(file)
                self.add_thing(item)

    def filter_by_name(self, name): #zeigt ob der Name einer Kunde schon gibt
        self.repo.load()
        return list(filter(lambda x: name.lower() in x.name.lower(), self.repo.list))

    def filter_by_adress(self, adress):#zeigt ob es jemand gibt, der eine bestimmte Adresse hat
        self.repo.load()
        return list(filter(lambda x: adress.lower() in x.Adresse.lower(), self.repo.list))


