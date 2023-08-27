'''
CONJETURA DE COLLATZ
'''

def conjeturaCollatz(numero):
    
    if numero % 2 == 0: 
        numero = numero/2
    else: 
        numero = (3*numero) + 1
        
    print(numero)
    if numero != 1: #Volver a llamar la función hasta que el numero sea 1
        conjeturaCollatz(numero)
    else:
        return numero
        
numero_entero = int(input("Digita un número entero: "))
serie = conjeturaCollatz(numero_entero)




    


    