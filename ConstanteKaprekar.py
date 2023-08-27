'''
Consiste simplemente en reordenar los dígitos de un número de modo que se obtenga el mayor y el menor número posible, restando entonces el menor del mayor.

Si cogemos los cuatro dígitos de 6174 y formamos dos nuevos números ordenándolos en orden descendente y ascendente, obtenemos 7641 y 1467. Al restar, 
obtenemos 7641 – 1467 = 6174, el número desde el cual comenzamos.

Esto no es una gran sorpresa. Lo que sorprende es que, comenzando desde cualquier otro número de cuatro dígitos (que no sea «repdigits«, como 3333, 
debido a que su sustracción resulta en cero) y repitiendo el mismo proceso, siempre llegamos al 6174. Por ejemplo:

Cogemos el número 1234 y aplicamos el mismo proceso:
4321 – 1234 = 3087

8730 – 0378 = 8352

8532 – 2358 = 6174


Nuevamente, si elegimos el año actual, 2018, obtenemos la secuencia:
8210 – 0128 = 8082

8820 – 0288 = 8532

8532 – 2358 = 6174
'''

def constanteKaprekar(numero):
    
    digitos = [int(a) for a in str(numero)]#guardando los digitos en una lista ej: [1,2,3,4]
    #ordenar la lista de digitos de forma descendente y ascendente.
    menor = int(''.join(map(str,sorted(digitos)))) #concatenar los digitos de la lista como cadenas para luego convertir esa cadena a 'enter ej: [1,2,3,4] -> '1234' -> 1234
    mayor = int(''.join(map(str,sorted(digitos,reverse=True)))) #[4,3,2,1] -> '4321' -> 4321
    resta = mayor - menor #Restar el menor al mayor
    print(f"{mayor} - {menor} = {resta}")
    #Volver a llamar a la función hasta que el resultado sea 6174
    if resta == 6174: 
        print(f"Se alcanzó la constante de kaprekar: {resta}")
        return resta
    else:
        constanteKaprekar(resta)
# Verificar que el número sea de 4 digitos   
while(True):
    pedir_numero = input("Digita un número de 4 digitos: ")
    if(len(pedir_numero)<=4):break

numero = constanteKaprekar(int(pedir_numero))


    
    
    
    
    
    
