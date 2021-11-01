def isPythagoras(a, b, c):
    if((a ** 2) + (b ** 2) == c ** 2):
        print('a =', a, ' b =', b, ' c =', c, ' ->True')
    else:
        print('a =', a, ' b =', b, ' c =', c, ' ->False')

a = 8
b = 6
c = 10
isPythagoras(a, b, c)