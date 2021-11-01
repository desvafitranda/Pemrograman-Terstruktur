def sum(*bil):
    hasil = 0
    for i in bil:
        hasil += i
    print(hasil)

def average(*bil):
    hasil = 0
    x = 0
    for i in bil:
        hasil += i
        x += 1
    print(hasil / x)

def maks(*bil):
    hasil = 0
    for i in bil:
        if i >= hasil:
            hasil = i
    print(hasil)

def min(*bil):
    hasil = 9999999999999999
    for i in bil:
        if i <= hasil:
            hasil = i
    print(hasil)

sum(5, 10, 4, 9, 30, 16, 2, 11)
average(5, 10, 4, 9, 30, 16, 2, 11)
maks(5, 10, 4, 9, 30, 16, 2, 11)
min(5, 10, 4, 9, 30, 16, 2, 11)

sum(81, 98, 12, 83, 45, 77, 69, 30, 56)
average(81, 98, 12, 83, 45, 77, 69, 30, 56)
maks(81, 98, 12, 83, 45, 77, 69, 30, 56)
min(81, 98, 12, 83, 45, 77, 69, 30, 56)