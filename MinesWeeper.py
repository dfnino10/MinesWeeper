#coding=utf8

import random

# Variables globales
ancho = 0
altura = 0
num_minas = 0
matrix = [[]]
num_minas=0
list_posiciones_minas=[]
list_marcados=[]

# Función principal
def main():
    print('Ingrese la altura, ancho y numero de minas en ese orden separados por espacio')
    global ancho
    global altura
    global num_minas
    global matrix
    global list_posiciones_minas
    user_input = input()
    altura = int(user_input.split(' ')[0])
    ancho = int(user_input.split(' ')[1])
    num_minas = int(user_input.split(' ')[2])
    # Se crea la variable que se convertira en el tablero
    matrix = [['.' for x in range(ancho)] for y in range(altura)]
    list_posiciones_minas = (random.sample(range(0, (altura*ancho)), num_minas))
    # Imprime la variable del tablero para el uuario
    matrix_printer(matrix)
    # Variable de terminación del juego
    finished = False
    # Variable para verificar el número de banderas en el tablero
    num_P=0
    while not finished:
        print ('Ingrese fila, columna y acción. (Las flias y columnas empiezan desde 0 y puede escoger entre dos acciones: U para "uncover", M para marcar la casilla))')
        inp_str = input()
        try:
            fila_actual = int(inp_str.split(' ')[0])
            columna_actual = int(inp_str.split(' ')[1])
            accion = inp_str.split(' ')[2]
            num = tuple_parser(fila_actual, columna_actual)
            if in_matrix((fila_actual, columna_actual)):
                if num in list_posiciones_minas and accion == 'U':
                    finished = True
                    print('¡Perdiste!')
                    for pos_mina in list_posiciones_minas:
                        matrix[number_parser(pos_mina)[0]][number_parser(pos_mina)[1]] = '*'
                elif num not in list_posiciones_minas and accion == 'U':
                    if matrix[fila_actual][columna_actual] == 'P':
                        num_P-=1
                    matrix[fila_actual][columna_actual] = '-'
                    for cell in adjacent_cells(fila_actual, columna_actual):
                        if in_matrix(cell):
                            count = count_adjacent_mines(cell)
                            if matrix[cell[0]][cell[1]] != '-':
                                if count == 0:
                                    matrix[cell[0]][cell[1]] = 1
                                else:
                                    matrix[cell[0]][cell[1]] = count
                elif matrix[fila_actual][columna_actual] != '-' and accion == 'M':
                    matrix[fila_actual][columna_actual] = 'P'
                    num_P += 1
                    if num_P == num_minas:
                        gana = True
                        for cell in list_posiciones_minas:
                            dupla = number_parser(cell)
                            if matrix[dupla[0]][dupla[1]]!= 'P':
                                gana = False
                        if gana:
                            finished = True
                            print('¡Ganaste!')
            else:
                print('La posición escogida no está dentro del tablero')
        except:
            print('Ops, intentalo de nuevo')

        matrix_printer(matrix)

# Función para imprimir la matriz (tablero)
def matrix_printer(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

# Función que pasa una dupla a un numero (posición en la matriz)
def tuple_parser(x,y):
    global ancho
    return x*(ancho)+ y

#Pasa un numero (posición en la matriz) a una dupla
def number_parser(x):
    global ancho
    return [int(x / ancho), x % ancho]

# Retorna todas las duplas de posiciones que son adyacentes a la posición actual
def adjacent_cells(x,y):
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)]

# Cuenta el numero de minas que hay alrededor de una posición
def count_adjacent_mines(x): #recibe una variable x que es una dupla (y,z)
    adj_mines = 0
    for cell in adjacent_cells(x[0],x[1]):
        if in_matrix(cell) and tuple_parser(cell[0], cell[1]) in list_posiciones_minas:
            adj_mines += 1
    return adj_mines

# Función para saber si una posición está dentro de la matriz
def in_matrix(x): #recibe una variable x que es una dupla (y,z)
    return 0<=x[0] and x[0]<=altura-1 and 0<=x[1] and x[1]<=ancho-1

if __name__ == "__main__":
    main()