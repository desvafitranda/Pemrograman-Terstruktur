from operation import *

a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
hasil = bagi(bagi(jumlah(a, b), jumlah(c, d)), kurang(e, f))
print('(', a, '+', b, ')', '/', '(', c, '+', d, ')', '/', '(', e, '-', f, ')', '=', hasil)