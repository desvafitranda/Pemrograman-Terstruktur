def luasSegitiga(a, t):
    luas = a * t / 2
    return luas
def hasil():
    print('luas segitiga dengan alas ', alas,
    'dan tinggi ', tinggi,
    "adalah ", luasSegitiga(alas, tinggi))
alas = 10
tinggi = 20
hasil()
alas = 15
tinggi = 45
hasil()
