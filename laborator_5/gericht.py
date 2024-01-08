
class Identifizierbar:
    def __init__(self, id :int):
        self.id = id

    def __str__(self):
        return f'{self.id}'


# caras = DataRepo('exemplu.pickle')
# DataRepo.save(caras)
# print(DataRepo.load(caras))
# print(caras.list)
# caras = DataRepo('exemplu.pickle')
# print(caras.read_file())
# with open('exemplu.pickle', 'w') as f:
    # c = f.write(2)
# zahlen = [1, 2, 3, 4, 5]
# zahlen= [1]
# a = [2]
# ergebnisse = map(lambda x: x**2, zahlen)
# print(zahlen[:-1])
# print(zahlen+a)

# obj.__private_methode()  # Dies würde einen Fehler auslösen
# def test(a):
#     return a+1
l = [1, 2]
print(l.index(1))
