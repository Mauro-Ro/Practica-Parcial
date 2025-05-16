"""
Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos):

Realizar el juego "Radar del Tesoro"
Dado el siguiente mapa de 5x5 donde se encuentra oculto un único tesoro, marcado con un 1:
mapa = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0] ]
Pedir al usuario una coordenada fila (x) entre 0 y 4 (inclusive).
Pedir al usuario una coordenada columna (y) entre 0 y 4 (inclusive).

Desarrollar una función con el siguiente prototipo:
 verificar_tesoro(mapa: list, x: int, y: int) -> int
La función debe retornar:
 - 0 si el usuario encontró el tesoro.
 - En caso contrario, retornar la distancia Manhattan entre la coordenada ingresada y la ubicación real del
tesoro.
**Distancia Manhattan**:
distancia = |x_usuario - x_tesoro| + |y_usuario - y_tesoro|
Según el valor retornado, mostrar al usuario:
 - "¡Encontraste el tesoro!" si retorna 0.
 - "Fallaste. El tesoro está a X casilleros de distancia." si retorna otro número.
El juego continúa hasta que el usuario encuentre el tesoro o hasta que el usuario lo desee.
Nota: No se pueden utilizar funciones propias.

"""

mapa = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0] ]



def verificar_tesoro(mapa: list, x: int, y: int):
    x_tesoro = 0
    y_tesoro = 0

    distancia = 0

    for i in range(len(mapa)):
        for j in range(len(mapa[i)):
            if mapa[i][j] == 1:
                x_tesoro = i
                y_tesoro = j

    if x > 4 or y > 4:
        print("Fuera de rango")
    else:
        if mapa[x][y] == 1:
            print("¡Encontraste el tesoro!")
            return 0
        else:
            distancia = (x - x_tesoro) + (y - y_tesoro)
            
    print(f"Fallaste. El tesoro está a {distancia} casilleros de distancia.")


def desea_continuar():  
    
    continuar = input("Ingrese (si) si desea seguir jugando de lo contrario ponga (no): ")

    while continuar.lower() == "si":
        ingrese_x = int(input("Ingrese x: "))

        ingrese_y = int(input("Ingrese y: "))

        verificar_tesoro(mapa, ingrese_x, ingrese_y)
        
        continuar = input("Ingrese (si) si desea seguir jugando de lo contrario ponga (no): ")

desea_continuar()
