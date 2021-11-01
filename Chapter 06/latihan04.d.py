def min(*bil):
    hasil = 9999999999999999
    for i in bil:
        if i <= hasil:
            hasil = i
    print(hasil)