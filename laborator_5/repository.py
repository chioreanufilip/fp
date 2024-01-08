import pickle
# from laborator_5.modelle import *
from abc import abstractmethod

class DataRepo():
    def __init__(self, datei: str):
        self.datei = datei
        self.list = []

    def write_to_file(self, ceva): #uberschreibt den Datei und schreibt dort was man will
        with open(self.datei, 'wb') as f:
            pickle.dump(ceva, f)

    def add(self, nou):
        try:
            DataRepo.load(self) #liest was vorher in der Datei war und wenn der Datei lehr ist gibt eine lehre Liste zuruck
            self.list.append(nou)
        except EOFError:
            self.list = []
            self.list.append(nou)

    def save(self): #steckt die self.list in einer Datei
        with open(self.datei, 'wb') as f:
            pickle.dump(self.list, f)

    def read_file(self):
        content = ''
        n = 0
        with open(self.datei, 'rb') as f:  #liest alles von einer Datei
            while n != 1:
                try:
                    content += str(pickle.load(f)) + '\n'

                except EOFError:
                    n = 1
        return content

    def load(self):  #ladet self.list mit was in der geoffnete Datei ist
        with open(self.datei, 'rb') as f:
            self.list = pickle.load(f)
        return self.list

    def loeschen(self, repo, id_zu_loschen): #loescht ein Element von der Liste und ruft convert_to_string an, was der
        gojira = repo   #Element in ein string umwandel und ihn in ein Datei steckt
        gojira.load()
        backup = gojira.list
        self.list = list(filter(lambda x: x.id != id_zu_loschen, gojira.list))
        gojira.write_to_file(self.list)
        for item in backup:
            if item.id == id_zu_loschen:
                gojira.convert_to_string([item])

    def aktualisieren(self, repo, id_zu_aktualisieren, new, what_needs_change):#aktualisiert ein atribut von der instanz
        gojira = repo
        gojira.load()
        for something in gojira.list:
            if something.id == id_zu_aktualisieren:
                if what_needs_change == 1:
                    something.name = new
                if what_needs_change == 2:
                    something.Portionsgrosse = new
                if what_needs_change == 3:
                    something.Preis = new
                if what_needs_change == 4:
                    something.Zubereitungszeit = new
                if what_needs_change == 5:
                    something.Alkoholinhalt = new
                if what_needs_change == 6:
                    something.Adresse = new
        gojira.save()
    @abstractmethod
    def convert_to_string(self, Objektliste): #steckt klassen in dateien, nachdem ihren Attribute in string verwandelt wurden
        pass
        #deci practic sa poti scrie tu numele la ce alei in loc sa alegi id-urile cum am facut eu si atunci ti l-ar transforma in tro lista de obiecte
    @abstractmethod
    def string_to_list(self, string):
        pass

    def __str__(self):
        return f'{self.list}'


class CookedDishRepo(DataRepo): #GekochterGericht):
    def __init__(self):
        DataRepo.__init__(self, 'texte/kochen.pickle')

    def convert_to_string(self, Objektliste):
        string_matrice = list(map(lambda a:self.for_convert_to_string(a) , Objektliste))
        # with open('kochen_string.pickle', 'w') as f:
        #     f.write('')
        for lista in string_matrice:
            # with open('kochen_string.pickle', 'ab') as f:
                # pickle.dump('\n',f)
            # for elem in lista:
            with open('texte/kochen_string.pickle', 'ab') as f:
                pickle.dump(lista, f)


    def for_convert_to_string(self, ceva):  #baut der string
        atribute = ''
        atribute += ceva.name+', '
        atribute +=ceva.Preis+', '
        atribute+=ceva.Zubereitungszeit+', '
        atribute +=ceva.Portionsgrosse+', '
        atribute+=str(ceva.id)
        return atribute


    def convert_from_string(self): #liest der Datei und wandelt der string in eine klasse
        liste_obiecte = []
        n =0
        with open('texte/kochen_string.pickle', 'rb') as f:
            while n != 1:
                try:
                    item = pickle.load(f)
                    liste_obiecte.append(item)
                except EOFError:
                    n = 1
        # print(liste_obiecte)
        object_list = list(map(self.create_gekochter_gericht, liste_obiecte))
        # for obj in object_list:
        #     print(obj)
        return object_list
        # for obj in object_list:
        #     print(obj)

    def create_gekochter_gericht(self, line): #baut die klasse
        from laborator_5.modelle import GekochterGericht
        # atribute = line.strip('\n')
        atribute = line.split(', ')
        # atribute[4] = atribute[4].strip(',')
        # print(atribute)
        return GekochterGericht(name=atribute[0], Portionsgrosse=atribute[3], Preis=atribute[1],
                                Zubereitungszeit=atribute[2], id=int(atribute[4]))

class DrinkRepo(DataRepo):
    def __init__(self):
        super().__init__('texte/getranke.pickle')

    def convert_to_string(self, Objektliste):
        string_matrice = list(map(lambda a: self.for_convert_to_string(a), Objektliste))
        # with open('kochen_string.pickle', 'w') as f:
        #     f.write('')
        for lista in string_matrice:
            # with open('kochen_string.pickle', 'ab') as f:
            # pickle.dump('\n',f)
            # for elem in lista:
            with open('texte/getranke_string.pickle', 'ab') as f:
                pickle.dump(lista, f)

    def for_convert_to_string(self, ceva):
        atribute = ''
        atribute += ceva.name + ', '
        atribute += ceva.Preis + ', '
        atribute += ceva.Alkoholinhalt + ', '
        atribute += ceva.Portionsgrosse + ', '
        atribute += str(ceva.id)
        return atribute

    def convert_from_string(self):
        liste_obiecte = []
        n = 0
        with open('texte/getranke_string.pickle', 'rb') as f:
            while n != 1:
                try:
                    item = pickle.load(f)
                    liste_obiecte.append(item)
                except EOFError:
                    n = 1
        # print(liste_obiecte)
        object_list = list(map(self.create_getrank, liste_obiecte))
        # for obj in object_list:
        #     print(obj)
        return object_list
        # for obj in object_list:
        #     print(obj)

    def create_getrank(self, line):
        from laborator_5.modelle import Getrank
        # atribute = line.strip('\n')
        atribute = line.split(', ')
        # atribute[4] = atribute[4].strip(',')
        # print(atribute)
        # return GekochterGericht(name=atribute[0], Portionsgrosse=atribute[3], Preis=atribute[1],
        #                         Zubereitungszeit=atribute[2], id=int(atribute[4]))

        return Getrank(name=atribute[0], Preis=atribute[1], Alkoholinhalt=atribute[2],Portionsgrosse=atribute[3], id=atribute[4])


class CustomerRepo(DataRepo):
    def __init__(self):
        super().__init__('texte/customer.pickle')
    def convert_to_string(self, Objektliste):
        string_matrice = list(map(lambda a: self.for_convert_to_string(a), Objektliste))
        # with open('kochen_string.pickle', 'w') as f:
        #     f.write('')
        for lista in string_matrice:
            # with open('kochen_string.pickle', 'ab') as f:
            # pickle.dump('\n',f)
            # for elem in lista:
            with open('texte/customer_string.pickle', 'ab') as f:
                pickle.dump(lista, f)

    def for_convert_to_string(self, ceva):
        atribute = ''
        atribute += ceva.name + ', '
        atribute += ceva.Adresse + ', '
        atribute += str(ceva.id)
        return atribute

    def convert_from_string(self):
        liste_obiecte = []
        n = 0
        with open('texte/customer_string.pickle', 'rb') as f:
            while n != 1:
                try:
                    item = pickle.load(f)
                    liste_obiecte.append(item)
                except EOFError:
                    n = 1
        # print(liste_obiecte)
        object_list = list(map(self.create_kunde, liste_obiecte))
        # for obj in object_list:
        #     print(obj)
        return object_list
        # for obj in object_list:
        #     print(obj)

    def create_kunde(self, line):
        from laborator_5.modelle import kunde
        # atribute = line.strip('\n')
        atribute = line.split(', ')
        # atribute[4] = atribute[4].strip(',')
        # print(atribute)
        # return GekochterGericht(name=atribute[0], Portionsgrosse=atribute[3], Preis=atribute[1],
        #                         Zubereitungszeit=atribute[2], id=int(atribute[4]))
        return kunde(name=atribute[0], Adresse=atribute[1], id=atribute[2])
class OrderRepo(DataRepo):
    def __init__(self):
        super().__init__('texte/order.pickle')

    def convert_to_string(self, Objektliste):
        string_matrice = list(map(lambda a: self.for_convert_to_string(a), Objektliste))
        # with open('kochen_string.pickle', 'w') as f:
        #     f.write('')
        for lista in string_matrice:
            print(lista)
            # with open('kochen_string.pickle', 'ab') as f:
                # pickle.dump('\n',f)
            # for elem in lista:
            with open('texte/bestellungen.pickle', 'ab') as f:
                pickle.dump(lista, f)


    def for_convert_to_string(self, ceva): #das wird am Ende einer Bestellung gezeigt
        from laborator_5.ui import datum
        atribute = '\nDiese Bestellung besteht aus die gekochte Gericht: \n'
        for elem in ceva.liste_der_IDs_fur_Gerichte:
            atribute += self.gerichte(CookedDishRepo(), elem)+'\n'
        atribute += 'Sie besteht auch aus die Getränke: \n'
        for elem in ceva.liste_der_IDs_fur_Getranke:
            atribute += self.gerichte(DrinkRepo(), elem)+'\n'
        atribute += 'Die Bestellung ist fur : \n'
        for elem in ceva.kunden_id:
            atribute += self.gerichte(CustomerRepo(), elem)+'\n'
        atribute += 'Die Bestellung hat den ID: '+str(ceva.id)+'\n'
        atribute+='Insgesamt muss man : '
        atribute+= ceva.kosten_string(ceva.Gesamtkosten)
        atribute+=' bezahlen \n'
        atribute+= 'Es muss an :'
        atribute+= datum()
        atribute+=' Uhr geliefert werden werden. \n'
        return atribute


    def gerichte(self, repo, id_der_gericht):
        gojira = repo
        gojira.load()
        for something in gojira.list:
            if something.id == int(id_der_gericht):
                return something.name

    def read_bestellung(self):
        content=[]
        content_suprem=''
        n=0
        with open('texte/bestellungen.pickle', 'rb') as f:
            while n != 1:
                try:
                    item = pickle.load(f)
                    content.append(item)
                except EOFError:
                    n = 1
        for obj in content:
            content_suprem+= obj
        return content_suprem
