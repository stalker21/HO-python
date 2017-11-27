x= 2
numero = 600851475143
suma = 0
factoresprimos = []


while (numero != 1):

    if (numero % x == 0):
        factoresprimos.append(x)
    
        numero = numero/x
        suma +=1
    else:
        x = x + 1

print factoresprimos

maxfactorprimo=max(factoresprimos)
print maxfactorprimo
