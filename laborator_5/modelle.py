import functools
from laborator_5.repository import *
class Identifizierbar:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f'{self.id}'


class Gericht(Identifizierbar):
    def __init__(self, Portionsgrosse, Preis, name, id):
        super().__init__(id)
        self.Portionsgrosse = Portionsgrosse
        self.Preis = Preis
        self.name = name
        
    def __str__(self):
        return f'{self.name},{self.Portionsgrosse}, {self.Preis}, {self.id}'

class GekochterGericht(Gericht):
    def __init__(self, Portionsgrosse, Preis, Zubereitungszeit, name, id):
        # super().__init__()
        Gericht.__init__(self,Portionsgrosse, Preis, name, id)
        self.Zubereitungszeit = Zubereitungszeit
    def __str__(self):
        return f'Name: {self.name},      Portionsgrosse: {self.Portionsgrosse} g,      Preis: {self.Preis} lei,      Zubereitungszeit: {self.Zubereitungszeit} min,      ID: {self.id}'

class Getrank(Gericht):
    def __init__(self,Portionsgrosse, Preis, Alkoholinhalt, name, id):
        Gericht.__init__(self, Portionsgrosse, Preis, name, id)
        self.Alkoholinhalt = Alkoholinhalt
    def __str__(self):
        return f'Name: {self.name},     Eine Portion bedeutet: {self.Portionsgrosse} ml,     Enthalt {self.Alkoholinhalt} % Alkohol,     Preis:{self.Preis} lei,      ID: {self.id}'

class kunde(Identifizierbar):
    def __init__(self, name, Adresse, id):
        Identifizierbar.__init__(self, id)
        self.name = name
        self.Adresse = Adresse

    def __eq__(self, other):
        if isinstance(other, kunde):
            return self.name == other.name or self.Adresse == other.Adresse

    def __str__(self):
        return f'Name: {self.name},     Adresse: {self.Adresse},      ID: {self.id}'


class Bestellung(Identifizierbar):
    def __init__(self, kunden_id, liste_der_IDs_fur_Gerichte: list, liste_der_IDs_fur_Getranke:list, Gesamtkosten, id):
        super().__init__(id) #vezi sa pui una din gerichte la pret dupaia una din getranke dupaia din nou gerichte si tot asa ca sa poti pune la gesamtkosten si numele
        self.kunden_id = kunden_id
        self.liste_der_IDs_fur_Gerichte =liste_der_IDs_fur_Gerichte
        self.liste_der_IDs_fur_Getranke =liste_der_IDs_fur_Getranke
        self.Gesamtkosten = Gesamtkosten

    def kosten( self, liste_mit_kosten: list): #das berechnet die kosten der gewahlten Elementen
        for i in range(len(liste_mit_kosten)):
            liste_mit_kosten[i] = float(liste_mit_kosten[i])
        self.Gesamtkosten = functools.reduce(lambda a, b: a+b, liste_mit_kosten)
        return self.Gesamtkosten

    def __kostenstring(self, liste_mit_kosten): #das ist sozusagen die Rechnung
        zahl_gericht = len(self.liste_der_IDs_fur_Gerichte)
        zahl_getrank = zahl_gericht + len(self.liste_der_IDs_fur_Getranke)
        kosten_string =list(map(lambda a: f'{str(self.find(repo=CookedDishRepo(), id=self.liste_der_IDs_fur_Gerichte[liste_mit_kosten.index(a)]))}: {a} lei + ', liste_mit_kosten[:zahl_gericht]))
        kosten_string +=list(map(lambda a: f'{str(self.find(repo=DrinkRepo(), id=self.liste_der_IDs_fur_Getranke[liste_mit_kosten.index(a)-zahl_gericht-1]))}: {a} lei + ', liste_mit_kosten[zahl_gericht:-1]))
        if zahl_getrank == 0:
            kosten_string+=f'{self.find(CookedDishRepo(), self.liste_der_IDs_fur_Gerichte[-1])}: {liste_mit_kosten[-1]} lei = {self.kosten(liste_mit_kosten)} lei'
            kosten_string = ''.join(kosten_string)
        if zahl_getrank != 0:
            kosten_string += f'{self.find(DrinkRepo(), self.liste_der_IDs_fur_Getranke[-1])}: {liste_mit_kosten[-1]} lei = {self.kosten(liste_mit_kosten)} lei'
            kosten_string = ''.join(kosten_string)
        return kosten_string

    def find(self, repo, id):
        # alimente = []
        gojira = repo
        gojira.load()
        for something in gojira.list:
            if something.id == id:
                return something.name
                # alimente.append(something.name)
        # return alimente


    def kosten_string(self, liste_mit_kosten):
        return self.__kostenstring(liste_mit_kosten)

    def __str__(self):
        return f'Kunden-ID: {self.kunden_id}, Liste fur Gerichte {self.liste_der_IDs_fur_Gerichte}, Liste fur Getranke {self.liste_der_IDs_fur_Getranke}, die Gesamtkosten: {self.Gesamtkosten}, id der Bestellung: {self.id}'


# strinf = ''
# strinf += 'aha'
# print(strinf)
# aha = Gericht('59', '67', 'Barosaneala',5)
# print(aha)

# l = ['12', '25', '69']
# Bestellung(14,[5],[6, 7],l,8).kosten_string(l)
