import random

trivial = {'¿Cuál es la capital de Qatar?' : 'Doha' , 
           '¿Cuál es el país más grande del mundo?' : 'Rusia', 
           '¿Cuál es la montaña más alta del mundo?' : 'Everest', 
           '¿Cuántos estados hay en Estados Unidos?' : '50', 
           '¿Cuántos países forman parte de la Unión Europea?' : '27', 
           '¿Cuál es el continente más poblado?' : 'Asia', 
           '¿Cuál es el idioma oficial de Andorra?' : 'Catalán', 
           '¿Cuál es el país menos densamente poblado del mundo?' : 'Mongolia', 
           '¿En qué océano desemboca el río Amazonas?' : 'Atlántico', 
           '¿Qué país africano tiene como capital Nairobi?' : 'Kenia'}

lista_preguntas = list(trivial.keys())
aciertos = 0
fallos = 0
intentos = 3

## LÓGICA DEL JUEGO ##

while aciertos < 5 and fallos < 3:
   
    ## CONDICIONALES ##

    if intentos > 0:
        if intentos == 3:
            pregunta_random = random.choice(lista_preguntas)
            lista_preguntas.remove(pregunta_random) # ----- eliminamos el random de la lista de preguntas
            # --Mantiene la misma pregunta durante los 3 intentos para acertarla
        
        respuesta = input(pregunta_random).capitalize().strip() # ----- capitalize.() para que salgan correctamente escritas en el print de lín. 45
        # --Solicita la respuesta de la jugadora

        if trivial.get(pregunta_random) == respuesta:
            aciertos += 1
            intentos = 3
            print(f"¡Enhorabuena, has acertado!")
            print("------------------------------------------------")
            print(f"------- Llevas {aciertos} acierto(s) y {fallos} fallo(s) -------")
            print("------------------------------------------------")
            # --Si la respuesta es correcta, da un punto y pasa a la siguiente pregunta. También se restablece el número de intentos para la siguiente ronda
        
        else: 
            intentos -= 1
            if intentos != 0: # --Condicional extra para que el print no muestre un mensaje diciendo que quedan "0 intentos"
                print(f"No es correcto, respondiste {respuesta} y la respuesta era {trivial.get(pregunta_random)}. Aún te quedan {intentos} intento(s). ¡Prueba de nuevo!")
                # --Si la respuesta es errónea, pero aún quedan intentos, vuelve a solicitar respuesta a la jugadora. Cada respuesta errónea resta 1 intento  

    else:
        fallos += 1
        intentos = 3
        print(f"Lástima, has fallado esta pregunta :(")
        print("------------------------------------------------")
        print(f"------- Llevas {aciertos} acierto(s) y {fallos} fallo(s) -------")
        print("------------------------------------------------")
        print(lista_preguntas) # ---esto es para verificar que se están eliminando las preguntas; hay que quitarlo del código
        # --Si la jugadora ha agotado sus intentos y no ha acertado la pregunta, cuenta un fallo y pasa a la siguiente pregunta. También se restablece el número de intentos para la siguiente ronda 