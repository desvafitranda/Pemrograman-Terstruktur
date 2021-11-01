def average(*bil):
    hasil = 0
    x = 0
    for i in bil:
        hasil += i
        x += 1
    print(hasil / x)