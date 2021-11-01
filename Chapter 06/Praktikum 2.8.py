def luasSegitiga(a, t):
    luas = a * t / 2
    return luas
def total(x, z):
    tot = x + z
    return tot

alas = 10
tinggi = 20
alas2 = 15
tinggi2 = 45
print('luas segitiga dengan alas', alas,
    'dan tinggi', tinggi,
    "adalah", luasSegitiga(alas, tinggi))
print('luas segitiga kedua dengan alas', alas2,
    'dan tinggi', tinggi2,
    "adalah", luasSegitiga(alas2, tinggi2))
Segitiga1 = luasSegitiga(alas, tinggi)
Segitiga2 = luasSegitiga(alas2, tinggi2)
print("Total Luas Kedua segitiga =", Segitiga1 + Segitiga2)
