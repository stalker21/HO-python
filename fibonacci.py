a=1 #defino variables
b=2
suma=0

while b<=1000000: #evaluo que b sea menor o igual que 1000000
    if b%2 != 0: #evaluo que b sea multiplo de 3 o 5
        suma += b #calculo la suma de los multiplos de 3 y 5
    temp=b #si no es multiplo guardo en temp
    b= b+a #actualizo b
    a= temp #actualizo a
print suma #imprimo suma multiplos 3 y 5
