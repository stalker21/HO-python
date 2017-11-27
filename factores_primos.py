x= 2 #definicion de variables
numero = 600851475143

factoresprimos = [] #definicion de lista


while (numero != 1): #evaluo si numero es disntito de 1

    if (numero % x == 0): #evaluo si x es factor primo de numero
        factoresprimos.append(x) #inserto x en lista
    
        numero = numero/x #actualizo numero
        
    else:
        x = x + 1 #actualizo x si no es factor primo de numero

print factoresprimos #imprimo lista factores primos

maxfactorprimo=max(factoresprimos) #evaluo max factor primo en lista
print maxfactorprimo #imprimo max factor primo
