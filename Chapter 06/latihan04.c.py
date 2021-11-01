def maks(*bil):
    hasil = 0
    for i in bil:
        if i >= hasil:
            hasil = i
    print(hasil)