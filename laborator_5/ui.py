# from laborator_5.modelle import *
from laborator_5.repository import *
from laborator_5.controller import *


def menu():  #Der Menu der am anfang angezeigt wird
    opt = input("""
    1- neue Bestellung hinzufügen
    2- etwas anderes
    3- siehe bisherige Bestellungen
    4- Exit
    """)
    if opt == '1':
        first_choice()
    if opt == '2':
        second_choice()
    if opt == '3':
        third_opt()


def first_choice():
    from laborator_5.modelle import Bestellung
    suchen_der_name_addresse()
    id_der_kunde = input("""
    schreibt der ID der Kunde:
    """)
    id_der_kunde = mehere_id(id_der_kunde)
    menu_practic(CookedDishRepo())
    id_der_gerichte = input("""
    Schreibt die IDs fur die Gerichte, die man wahlt:
    """)
    id_der_gerichte = mehere_id(id_der_gerichte)
    menu_practic(DrinkRepo())
    id_der_getranke = input("""
    Schreibt die IDs fur die Getranke, die man wahlt:
    """)
    id_der_getranke = mehere_id(id_der_getranke)
    # print(id_der_getranke,id_der_kunde,id_der_gerichte)
    kosten_gerichte = []
    gesamtkosten(repo=CookedDishRepo(), lista_aleasa=id_der_gerichte, gesamtkost=kosten_gerichte)
    gesamtkosten(repo=DrinkRepo(), lista_aleasa=id_der_getranke, gesamtkost=kosten_gerichte)
    # Bestellung(kunden_id=id_der_kunde,liste_der_IDs_fur_Gerichte= id_der_gerichte, liste_der_IDs_fur_Getranke=id_der_getranke, Gesamtkosten=kosten_gerichte, id=id_generator('order.pickle')).kosten_string(kosten_gerichte)
    bestellung =Bestellung(kunden_id=id_der_kunde, liste_der_IDs_fur_Gerichte= id_der_gerichte, liste_der_IDs_fur_Getranke=id_der_getranke, Gesamtkosten=kosten_gerichte, id=id_generator(
        'texte/order.pickle'))
    Controller(OrderRepo()).add_thing(thing=bestellung)
    bestellunglist= [bestellung]
    try:
        OrderRepo().convert_to_string(bestellunglist)  #Wenn der User die falsche ids schreibt dann muss er von vorne anfangen
    except TypeError:
        print("""
    Du hast etwas Falsch geschrieben, bitte noch mal versuchen
    """)
        first_choice()
    menu()

def suchen_der_name_addresse():# Diese Funktion sucht ob das input in der kunde.name oder in kunde.adresse in der customer.pickle ist und gibt die instanz zuruck
    client = input("""
        Wem wird diese Bestellung sein (man kann entweder nach Name oder nach Adresse suchen):
        """)
    suchen = Controller(CustomerRepo()).filter_by_adress(client)
    suchen1 = Controller(CustomerRepo()).filter_by_name(client)
    suchen_supreme = []
    for item in suchen:
        if item not in suchen_supreme:
            suchen_supreme.append(item)
    for item in suchen1:
        if item not in suchen_supreme:
            suchen_supreme.append(item)
    for item in suchen_supreme:
        print(item)
    if suchen == [] and suchen1 == []:
        opt = input("""
        Es existiert keiner Kunde mit solcher Name oder Adresse. Willst du ein neuer Kunde hinzufügen oder noch einmal suchen?
        1- Noch mal suchen
        2- Ein neuer Kunde hinzufügen
         """)
        if opt == '1':
            first_choice()
        if opt == '2':
            hinzufugen()

def datum():
    lieferung_datum = input("""
        Für welches Datum ist diese Bestellung: 
        """)+' '
    lieferung_uhrzeit = input('''
        Schreibt die Uhrzeit:
         ''')
    return lieferung_datum+lieferung_uhrzeit

def gesamtkosten(repo, lista_aleasa: list, gesamtkost: list): # gibt zuruck eine Liste mit die instanz.Preis der instanzen von lista_aleasa
    gojira = repo
    gojira.load()
    for id in lista_aleasa:
        for something in gojira.list:
            if something.id == id:
                if something.Preis not in gesamtkost:
                    gesamtkost.append(something.Preis)
    return gesamtkost



def mehere_id(lista):       #Wenn es mehrere id's gibt, wird diese Funktion sie in eine liste verwandeln
    lista = lista.split(',')
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista

def second_choice():
    from laborator_5.modelle import GekochterGericht, Getrank
    opt1 = input("""
    1- Bei Gerichte etwas ändern
    2- Bei Getränke etwas ändern
    3- Bei Kunde etwas ändern
    """)
    if opt1=='1':
        opt2 = input("""
    1- Ein Gericht hinzufügen
    2- Ein Gericht löschen
    3- Ein Gericht aktualisieren
    4- Ein Gericht zurückbringen
    """)
        if opt2 == '1':
            name = input('''
            Schreibt den Namen des neues Gerichts: ''')
            Portionsgrosse = input("""
            Wie gross ist eine Portion: 
                        """)
            Preis = input("""
            Wie viel kostet eine Portion: 
                        """)
            Zbz = input("""
            Wie viel dauert es, um eine Portion zu kochen: """)
            Gericht = GekochterGericht(name=name, Portionsgrosse=Portionsgrosse, Preis=Preis, Zubereitungszeit=Zbz,
                                       id=id_generator('texte/kochen.pickle'))
            Controller(CookedDishRepo()).add_thing(thing=Gericht)
            # content = CookedDishRepo().load()
            # for item in content:
            #     print(item.__dict__)
            # print(item.__dict__['Zubereitungszeit'])
            menu_practic(CookedDishRepo())
            menu()

        if opt2 =='2':
            menu_practic(CookedDishRepo())
            delete = int(input("""
            ID des Gerichts, das gelöscht werden soll, eingeben: 
            """))
            Controller(CookedDishRepo()).delete(delete)
            menu_practic(CookedDishRepo())
            menu()

        if opt2 == '3':
            menu_practic(CookedDishRepo())
            was_soll = int(input('Was ist das id des Gerichts: '))
            andern = int(input("""
        Was soll aktualisiert werden?
        1- Name
        2- Portionsgröße
        3- Preis
        4-Zubereitungszeit
            """))
            new_stuff = input("""
        Was soll eigentlich dort schreiben: 
            """)
            Controller(CookedDishRepo()).aktualisieren1(id_zu_aktualisieren=was_soll, new=new_stuff, what_needs_change= andern)
            menu_practic(CookedDishRepo())
            menu()
        if opt2 == '4':
            Controller(CookedDishRepo()).redoing_history()
            to_bring_back = int(input("""
    Schreibt den ID von was man zurückbringen will: 
    """))
            Controller(CookedDishRepo()).bring_back_the_dead(to_bring_back, 'texte/kochen.pickle')
            menu()

    if opt1 == "2":
        opt3 = input("""
    1- Ein Getränk hinzufügen
    2- Ein Getränk löschen
    3- Ein Getränk aktualisieren
    4- Ein Getränk zurückbringen
    """)
        if opt3 == '1':
            name = input("""
        Name des Getränks: 
            """)
            Portionsgrosse = input("""
        Wie viel ml hat ein Getränk dieser Art: 
            """)
            preis = input("""
        Wie viel kostet dieses Produkt: 
            """)
            alkoholinhalt = input("""
        Wie viel Prozent Alkohol enthält dieses Produkt: 
            """)
            getrank = Getrank(name=name, Portionsgrosse=Portionsgrosse, Preis=preis, Alkoholinhalt=alkoholinhalt,
                              id=id_generator('texte/getranke.pickle'))
            Controller(DrinkRepo()).add_thing(thing=getrank)
            menu_practic(DrinkRepo())
            menu()

        if opt3 == '2':
            menu_practic(DrinkRepo())
            delete = int(input("""
        ID des Getränks, das gelöscht werden soll, eingeben: """))
            Controller(DrinkRepo()).delete(delete)
            # content = DrinkRepo().load()
            # for item in content:
            #     print(item.__dict__)
            menu()

        if opt3 == '3':
            menu_practic(DrinkRepo())
            was_soll = int(input('''
        Was ist das id des Getränks: '''))
            andern = int(input("""
        Was soll aktualisiert werden?
        1- Name
        2- Portionsgröße
        3- Preis
        4- Alkoholinhalt
            """))
            new_stuff = input("""
        Was soll eigentlich dort schreiben: 
            """)
            if andern == 4:
                andern =5

            Controller(DrinkRepo()).aktualisieren1(id_zu_aktualisieren=was_soll, new=new_stuff, what_needs_change= andern)
            menu_practic(DrinkRepo())
            menu()

        if opt3 == '4':
            Controller(DrinkRepo()).redoing_history()
            to_bring_back1 = input("""
    Schreibt den ID von was man zurückbringen will: 
    """)
            Controller(DrinkRepo()).bring_back_the_dead(to_bring_back1, 'texte/getranke.pickle')
            # repo=DrinkRepo()
            # lista_obiecte = repo.convert_from_string()
            # for item in lista_obiecte:
            #     if item.id == to_bring_back1:
            #         print('ahahaahah')
            #         item.id = id_generator('texte/getranke.pickle')
            #         Controller(repo).add_thing(thing=item)
            menu()
    if opt1 == '3':
        opt4= input("""
    1- Ein Kunde hinzufügen
    2- Ein Kunde löschen
    3- Ein Kunde aktualisieren
    4- Ein Kunde zurückbringen
    """)
        if opt4 == '1':
            hinzufugen()
            menu()


        if opt4 == '2':
            menu_practic(CustomerRepo())
            delete = int(input("""
        ID der Kunde, das gelöscht werden soll, eingeben: 
                    """))
            Controller(CustomerRepo()).delete(delete)
            menu()
        if opt4 == '3':
            menu_practic(CustomerRepo())
            was_soll = int(input('''
        Was ist das id des Getränks: '''))
            andern = int(input("""
        Was soll aktualisiert werden?
        1- Name
        2- Adresse
        """))
            new_stuff = input("""
        Was soll eigentlich dort schreiben: 
                    """)
            if andern == 2:
                andern = 6
            Controller(CustomerRepo()).aktualisieren1(id_zu_aktualisieren=was_soll, new=new_stuff, what_needs_change=andern)
            menu_practic(CustomerRepo())
            menu()

        if opt4 == '4':
            Controller(CustomerRepo()).redoing_history()
            to_bring_back = input("""
    Schreibt den ID von was man zurückbringen will: 
    """)
            Controller(CustomerRepo()).bring_back_the_dead(to_bring_back,'texte/customer.pickle')
            menu()

def third_opt(): #zeigt die vorherigen Bestellungen
    print(OrderRepo().read_bestellung())
    menu()
def hinzufugen(): #fugt ein neuer Kunde hinzu
    from laborator_5.modelle import kunde
    name = input('''
        Schreibt den Namen der neuer Kunde: ''')
    Adresse = input("""
        Schreibt die Adresse der neuen Kunde: 
                   """)
    Kunde = kunde(name=name, Adresse=Adresse, id=id_generator('texte/customer.pickle'))
    Controller(CustomerRepo()).add_thing(thing=Kunde)
    menu_practic(CustomerRepo())


def menu_practic(repo): #zeigt die instanzen der Klassen
    content = repo.load()
    for item in content:
        print(item)

def id_generator(file:str): #generiert ein einzigartiges id
    nou = DataRepo(file)
    try:
        nou.load()
        return nou.list[len(nou.list) - 1].id + 1
    except EOFError:
        return 1
    except IndexError:
        return 1


# menu()