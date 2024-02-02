import random

reglas = {"piedra" : "papel" , "papel" : ["tijeras", "tijera"] , "tijeras" : "piedra"}
lista = ['piedra', 'papel', 'tijeras']
puntos_jugadora = 0
puntos_maquina = 0

while puntos_jugadora < 3 and puntos_maquina < 3:
    jugadora = input('Elige opción').lower().strip()
    maquina = random.choice(lista)

    if jugadora not in reglas:
        print('ERROR: elección no válida')

    else:
        if jugadora == maquina:
            print(f"Has escogido {jugadora} y la máquina {maquina}. Empate. Vais {puntos_jugadora} a {puntos_maquina}")
    
        else:
            if reglas.get(jugadora) == maquina:
                puntos_maquina += 1 
                print(f'Has escogido {jugadora} y la máquina {maquina}. Ohhhh, perdiste. Vais {puntos_jugadora} a {puntos_maquina}')

            else:
                puntos_jugadora += 1  
                print(f'Has escogido {jugadora} y la máquina {maquina}. Enhorabuena crack. Vais {puntos_jugadora} a {puntos_maquina}')

    print('--------------------------------------------------')

if puntos_jugadora > puntos_maquina:
    print(f'Enhorabuena, jugadora, has ganado con {puntos_jugadora} puntos!')
else:
    print(f'Lo lamento, la máquina ha ganado con {puntos_maquina} puntos :(') 