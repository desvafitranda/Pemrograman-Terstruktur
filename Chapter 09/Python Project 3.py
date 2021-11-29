def starFormation1(z,n):
    for x in range(1,n+1):
        bintang = "*" * (1 +(x-1)*2)
        print(bintang.center(1+2*z))

def starFormation2(z,n):
    for x in range(n,0,-1):
        bintang = "*" * (1 +(x-1)*2)
        print(bintang.center(1+2*z))

def starFormation3(n):
    if(n % 2 == 1): 
        starFormation1(n, n//2 + 1)
        starFormation2(n, n//2)
        

starFormation3(7)