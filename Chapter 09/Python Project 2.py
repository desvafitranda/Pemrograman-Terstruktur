def bintang(n):
    for x in range(n):
        print(('*'*(2*x+1)).center(1+2*n))

bintang(4)