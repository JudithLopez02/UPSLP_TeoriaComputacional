

def multiplicacionEgipcia(in_multiplicando,in_multiplicador):
    x = 1; suma = 0; num = 0 
    #Listas vacías 
    valores_multiplicando = [];valores_multiplicador = []; valores_finales = []

    while(x<in_multiplicador): #repetir hasta que el valor de x sea menor al multiplicador
        print(in_multiplicando)
        valores_multiplicando.append(in_multiplicando) #agregando a la lista el valor de multiplicando
        valores_multiplicador.append(x) #Agregar a la lista el valor de x (multiplicador)
        in_multiplicando *= 2 #aumentando el doble al valor de multiplicando 
        x *= 2 #aumentando el doble al valor de x (multiplicador)
    print(valores_multiplicando)
    print(valores_multiplicador)
    #Ordenando las listas en orden inverso -> facilíta (operaciones de abajo hacía arriba)
    valores_multiplicador = sorted(valores_multiplicador,reverse=True)
    valores_multiplicando = sorted(valores_multiplicando,reverse=True)
    
    #Recorriendo ambas listas (multiplicando y multiplicador)
    for multiplicando,multiplicador in zip(valores_multiplicando,valores_multiplicador):
        print(f"[{multiplicando}] [{multiplicador}]")
        if multiplicador + num <= in_multiplicador: #Evalúa si el valor de multiplicador + num es <= al input_multiplicador
            valores_finales.append(multiplicando)#Añadiendo a la lista los valores del multiplicando que cumplen con dicha condición
            num += multiplicador #sumando el valor del multplicador a la variable num
    print(valores_finales)
    #Recorriendo la lista de valores finales para sumar sus elementos
    for x in valores_finales: 
        suma += x 
    return suma

in_multiplicando = int(input("Multiplicando: "))
in_multiplicador = int(input("Multiplicador: "))

mult = multiplicacionEgipcia(in_multiplicando,in_multiplicador)
print(f"{in_multiplicando} x {in_multiplicador} = {mult}")
    
    