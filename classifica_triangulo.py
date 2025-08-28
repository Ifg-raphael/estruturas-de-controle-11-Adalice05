'''a= int(input(" "))
b= int(input(" "))
c= int(input(" "))'''

a, b, c = map(int, input().split())

if  a < b+c and b < a+c and c < a+b:
    if a==b==c:
        print("equilátero")
    if a==b!=c or a==c!=b or c==b!=a:
        print("isóceles")
    if a!=b!=c:
        print("escaleno")
else:
    print("Não forma triângulo")


    