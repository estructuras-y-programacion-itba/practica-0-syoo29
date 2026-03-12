# Tu implementacion va aqui
from random import *

# 5 dados, 2 jugadores
# 1-3 tiradas por turno
# 1er tirada 5 dados
# decide qué dados mantener y cuáles volver a lanzar
# turno termina cuando decide no volver a lanzar o alcanza 3 tiradas
# fin de turno 
# elige en que categoria registra el puntaje, no puede en una ya utilizada

# - **"E" (Escalera)**: 5 dados consecutivos. Vale **20 puntos**.
# - **"F" (Full)**: 3 dados iguales y 2 dados iguales (distintos a los primeros). Vale **30 puntos**.
# - **"P" (Póker)**: 4 dados iguales. Vale **40 puntos**.
# - **"G" (Generala)**: 5 dados iguales. Vale **50 puntos**.
# - **Números (1 al 6)**: Se anota la suma de los dados que coincidan con el número elegido (ej: tres dados "4" suman 12 puntos).

# Bonificaciones y Reglas Especiales

# - **Primera Tirada**: Si se forma "E", "F" o "P" en la primera tirada del turno, se suman **5 puntos adicionales**.
# - **Generala Real**: Si se forma "G" en la primera tirada del turno, se suman **30 puntos adicionales** y el juego termina inmediatamente (victoria automática).
# - **Jugada Obligatoria**: Si al finalizar el turno no se tiene ninguna jugada válida disponible, el jugador debe elegir una categoría pendiente y anotar **0 puntos**.

# Fin del Juego

# El juego termina cuando:
# - Ambos jugadores completaron las 11 categorías en su planilla.
# - O algún jugador obtuvo una **"Generala Real"**.

# Al finalizar, el programa debe informar el ganador o si hubo empate.

def ordenar_custom(lista): #ordena una lista de forma ascendente
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def escalera(dados):
    dadosordenados = ordenar_custom(dados) #ordeno los valores de los dados de menor a mayor
    es_escalera = True
    i = 1
    while i < len(dadosordenados):
        if not ((dadosordenados[i-1] + 1) == dadosordenados[i]): # si el numero sig en la lista no es el num consecutivo, entonces no es escalera
            es_escalera = False
        i += 1
    return es_escalera

def full(dados):
    dadosord = ordenar_custom(dados) #ordeno para ubicar
    num1 = dadosord[0] # en teoria deben ser distintos, el primero y el ultimo
    num2= dadosord[-1] 
    es_full = False
    j = 0 
    cont1 = 0
    cont2 = 0
    while j < len(dadosord):
        if dadosord[j] == num1:
            cont1 += 1
        elif dadosord[j] == num2:
            cont2 += 1
        j += 1
    
    if (cont1 == 3 and cont2 == 2) or (cont1== 2 and cont2 == 3):
        es_full = True
    else:
        es_full = False
    return es_full

def poker(dados):
    dadosord = ordenar_custom(dados) # ordeno para ubicar
    # utilizo la misma logica que con el full, pero cambio la cant de repeticiones del numero
    num1 = dadosord[0] # en teoria deben ser distintos, el primero y el ultimo
    num2= dadosord[-1] 
    es_poker = False
    j = 0 
    cont1 = 0
    cont2 = 0
    while j < len(dadosord):
        if dadosord[j] == num1:
            cont1 += 1
        elif dadosord[j] == num2:
            cont2 += 1
        j += 1
    
    if (cont1 == 4 and cont2 == 1) or (cont1== 1 and cont2 == 4):
        es_poker = True
    else:
        es_poker = False
    return es_poker

def generala(dados):
    p = 0 
    copiadados = dados[:]
    num = copiadados[0]
    es_generala = True
    while p < len(dados):
        if copiadados[p] != num:
            es_generala = False
        p += 1
        
    return es_generala

def numeros(dados):
    num = int(input("Escriba el numero elegido para el puntaje: "))
    i = 0
    suma = 0
    while i < len(dados):
        if dados[i] == num:
            suma += num
        i += 1
    
    return suma # retorno el puntaje

def tiradas(): # son 3 tiradas por turno, output= dados, puntosextras, generalareal
    sigue = True
    generalareal = False
    while (sigue == True):
        dados = [0,0,0,0,0] # son 5 dados, por tirada quiero almacenar los numeros que van saliendo
        puntosextras = 0
        i = 0
        while i < len(dados):
            dados[i] = randint(1,6)
            i += 1
        
        print(f"Primer tirada: {dados}") # muestro la 1er tirada
        if (escalera(dados) == True) or (full(dados) == True) or (poker(dados) == True):
            print("Se agregan 5 puntos adicionales")
            puntosextras += 5
        elif (generala(dados) == True): # si hay generala real
            puntosextras += 30
            generalareal = True
            print ("Generala real, victoria automatica!")
            sigue = False
            return dados, puntosextras, generalareal
            
        mantener = input ("Quiere mantener estos valores? (Si/No) ")
        
        if (mantener == "No") or (mantener == "no"):
            # Analizo la 2da y 3er tirada
            
            tirada = 2
            
            while tirada < 4:
                posiciones = [] # guardo las posiciones de los dados que quiere cambiar
                pos = 0
                while pos < len(dados):
                    dado = str(pos + 1) # el numero del dado actual
                    rta = input (f"¿Quiere volver a lanzar el dado {dado}? (Si/No) ") #pregunto que dados quiere mantener o volver a lanzar
                    if (rta == "Si") or (rta=="si"):
                        posiciones.append(pos) #agrego la posicion del dado que quiere volver a lanzar
                    pos += 1
            
                if posiciones != []:
                    k = 0 
                    while k < len(posiciones):
                        numdado = posiciones[k] # el numero del dado a cambiar
                        dados[numdado] = randint(1,6) # cambio el dado
                        k += 1
                    print(dados) # Hay algo que esta mal pero no encuentro el error, guarda bien el indice de la posicion que quiero cambiar 
                    #pero devuelve una lista de dados completamente distinta
                    
                    if tirada == 3: # luego de la 3er tirada no le doy mas opcion de cambiar los dados
                        print ("Termino su turno")
                        return dados, puntosextras, generalareal
                    
                    rta2 = input("Quiere mantener estos valores? (Si/No) ")
                    if (rta2 == "Si") or (rta2 == "si"): #si desea mantener los dados, devuelvo la lista de dados, puntosextras y si hubo generala real 
                        print("Termino su turno")
                        return dados, puntosextras, generalareal
                    else:
                        tirada += 1
                else: 
                    print("Debe seleccionar los dados que quiere volver a lanzar.")
        else:
            sigue = False
        
    return dados, puntosextras, generalareal

def colocar_puntaje(dados,puntaje): #output = puntaje
    print(puntaje)
    valido = input("¿Tiene una jugada valida? (Si/No): ")
    if (valido == "No") or (valido == "no"):
        cat = input("Elija una categoria pendiente: ")
        if (cat == "E") and (puntaje[0] == -1): # aseguro que no haya sido utilizada
            puntaje[0] == 0 # anoto 0
        elif cat == "F" and (puntaje[1] == -1):
            puntaje[1] == 0
        elif cat == "P" and (puntaje[2] == -1):
            puntaje[2] == 0
        elif cat == "G" and (puntaje[3] == -1):
            puntaje[3] == 0
        elif cat == "1" and (puntaje[4] == -1):
            puntaje[4] == 0
        elif cat == "2" and (puntaje[5] == -1):
            puntaje[5] == 0
        elif cat == "3" and (puntaje[6] == -1):
            puntaje[6] == 0
        elif cat == "4" and (puntaje[7] == -1):
            puntaje[7] == 0
        elif cat == "5" and (puntaje[8] == -1):
            puntaje[8] == 0
        elif cat == "6" and (puntaje[9] == -1):
            puntaje[9] == 0
        
    categoria = input("Elija en que categoria quiere registrar el puntaje, recuerde que no puede registarla en una ya utilizada (E/F/P/G/1-6): ")
    if (categoria == "E") and (puntaje[0] == -1): # aseguro que no haya sido utilizado
        if escalera(dados) == True:
            puntaje[0] += 21 # agrego uno porque en todos puse -1 en la lista
    elif categoria == "F" and (puntaje[1] == -1):
        if full(dados) == True:
            puntaje[1] += 31 
    elif categoria == "P" and (puntaje[2] == -1):
        if poker(dados) == True:
            puntaje[2] += 41
    elif categoria == "G" and (puntaje[3] == -1):
        if generala(dados) == True:
            puntaje[3] += 51
    elif categoria == "1" and (puntaje[4] == -1):
        puntaje[4] += (numeros(dados) + 1)
    elif categoria == "2" and (puntaje[5] == -1):
        puntaje[5] += (numeros(dados) + 1)
    elif categoria == "3" and (puntaje[6] == -1):
        puntaje[6] += (numeros(dados) + 1)
    elif categoria == "4" and (puntaje[7] == -1):
        puntaje[7] += (numeros(dados) + 1)
    elif categoria == "5" and (puntaje[8] == -1):
        puntaje[8] += (numeros(dados) + 1)
    elif categoria == "6" and (puntaje[9] == -1):
        puntaje[9] += (numeros(dados) + 1)
    
    return puntaje

def suma_pts (puntaje, ptsextra):
    suma = 0
    k = 0 
    while k < len(puntaje):
        suma += puntaje[k]
        k += 1
    suma += ptsextra # sumo los puntos extra
    return suma 
            
def menos_uno(lista):
    i = 0
    encontrado = False

    while i < len(lista) and (not encontrado):
        if lista[i] == -1:
            encontrado = True
        i += 1

    return encontrado
            
def turnos(jug1,jug2):
    
    #comienza el juego
    genreal1 = False
    genreal2 = False
    while (menos_uno(jug1) == True) and (menos_uno(jug2) == True) and (genreal1 == False) and (genreal2 == False): # si una categoria esta vacia o no hay generala real, continuo el juego
        print("Turno del jugador 1")
        dadosjug1, ptsextra1,genreal1 = tiradas()
        jug1 = colocar_puntaje(dadosjug1, jug1)
        puntosjug1 = suma_pts(jug1, ptsextra1)
        print("Turno del jugador 2")
        dadosjug2, ptsextra2,genreal2 =tiradas ()
        jug2 = colocar_puntaje(dadosjug2,jug2)
        puntosjug2 = suma_pts(jug2, ptsextra2)
    
    return puntosjug1, puntosjug2


def main():
    # Aqui ejecutas tus soluciones
    # categorias = ["E","F","P","G","1","2","3","4","5","6"] (lista representativa) armo listas simultaneas
    jugador1 = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] # armo listas que almacenan los puntos de los jugadores
    jugador2 = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    puntos1, puntos2 = turnos(jugador1, jugador2)
    if puntos1 > puntos2:
       print("Gano el jugador 1")
    elif puntos1 == puntos2:
        print("¡Hubo empate!")
    else:
        print("Gano el jugador 2")


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
