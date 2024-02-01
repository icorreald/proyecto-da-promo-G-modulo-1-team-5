AHORCADO
    a) lista randomizada de palabras
   
    - si error = parte, si acierto = letra
    - seguimiento de las letras adivinadas (y fallidas: ya has probado ____)
    
  
    
    > len(caracteres) = print(rayita x caracter)
    > while
    > poner un mínimo (5) y límite de caracteres (10)
    > numero de errores = numero palotes
    
    

PREGUNTAS Y RESPUESTAS
    - geografía
    - numero limitado de intentos
    - sigue hasta 3 errores / responda 5 correctas

    > 10 preguntas: diccionario (clave pregunta - valor respuesta)
    > randomizacion
    > bucle while (para con 5 ACIERTOS o 3 ERRORES)
        - dos prints diferentes: ENHORABUENA o LO SIENTO, PERDISTE
    > input('Pregunta')
        - lower
        - strip
        - hacer un A, B, C (* preguntar esto)
        - especificar cuidado con las tildes / coger respuestas sin tilde
    > conteo de erroes y aciertos
        - esto se va imprimiendo como un contador, para que el jugador lo sepa
    > si es ERROR, devuelve también la respuesta correcta



PIEDRA, PAPEL, TIJERA
    - piedra > tijera > papel > piedra
    - 1 punto por ronda
    - juego continua hasta jugador = 3 puntos
    * preguntar si contamos con interfaz o con notebook

    - definir n puntos para ganar
    - implementa función elección J1 y valide una de las opciones
    - bucle while: registro de puntos
    - bucle acaba cuando: 3 puntos un jugador
    - randomización de elecciones (máquina)
    - determina ganador + imprime actualización puntos
    - verifica si alguno de los jugadores llega al máximo de puntos


LISTA TAREAS:
* piedra papel tijera:
J1 = input('opción jugador').lower()


opciones = [tijera, papel, piedra]

tijera == tijera (empate)
tijera > papel
tijera < papel


import random
reglas = {"piedra" : "papel" , "papel" : "tijeras" , "tijeras" : "piedra"}
lista = ['piedra', 'papel', 'tijeras']

j1 = input('Elige opción').lower()
j2 = random.choice(lista)
print(j1, j2)


reglas.get(j1) == j2