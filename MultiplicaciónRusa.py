def multiplicacionRusa(in_multiplicando,in_multiplicador):
    x = 1; suma = 0; 
    valores_multiplicando = [];valores_multiplicador = []; #listas vacías 
    #Se ejecuta hasta que el valor del input_multplicador sea >= 1
    while(in_multiplicador >= 1):
        
        if (in_multiplicador % 2 != 0): #Si no es par el valor del input_multiplicador 
            
            valores_multiplicador.append(in_multiplicador) #Agregar a la lista el valor del input_multiplicador
            valores_multiplicando.append(in_multiplicando) #Agregar a la lista el valor del in_multiplicando 
                
        in_multiplicador //= 2 #mitad
        in_multiplicando *= 2 #doble
    #Recorriendo la lista para sumar sus elementos  
    for x in valores_multiplicando: 
        suma += x 
    
    return suma

in_multiplicando = int(input("Multiplicando: "))
in_multiplicador = int(input("Multiplicador: "))

mult = multiplicacionRusa(in_multiplicando,in_multiplicador)
print(f"{in_multiplicando} x {in_multiplicador} = {mult}")