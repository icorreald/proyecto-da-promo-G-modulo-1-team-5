class Juegos:
    
    def trivial_has_acertado(self):
        print(f"¡Enhorabuena, has acertado!")
        print("------------------------------------------------")
        print(f"------- Llevas {self.aciertos} acierto(s) y {self.fallos} fallo(s) -------")
        print("------------------------------------------------")

    def trivial_has_fallado(self):
        print(f"La respuesta correcta era {trivial.get(pregunta_random).capitalize()}. Lástima, has fallado esta pregunta :(")
        print("------------------------------------------------")
        print(f"------- Llevas {self.aciertos} acierto(s) y {self.fallos} fallo(s) -------")
        print("------------------------------------------------")

    
 
    def ahorcado_banner_inicio(self): # inicio del juego + primer display de la palabra oculta
        print(('-'*23).center(40))
        print('EL AHORCADO'.center(40))
        print(('-'*23).center(40))
        print(' ')
        print('Intenta adivinar la palabra'.center(40))
        print((self.guiones).center(40))

          

    def ahorcado_adivinar_letra(self):
        print('* * *'.center(40))
        print(f"¡Enhorabuena, has acertado! La letra {self.letra} está en la palabra secreta.")
        print(' ')
        print(self.guiones.center(40))
        print(f"Las letras utilizadas hasta el momento son: {self.letras_dichas}")
        print(' ')

    def ahorcado_fallar_letra(self):
        print('* * *'.center(40))
        print(self.ahorcado[self.intentos-1])
        print(' ')
        print(self.guiones.center(40))
        print(f"Lástima, has fallado. La letra {self.letra} no se encuentra en la palabra secreta")
        print(f"Te quedan {self.vidas} vidas")
        print(' ')
        print(f"Las letras utilizadas hasta el momento son: {self.letras_dichas}")
        print(' ')



    def piedrapapeltijera_bienvenida(self):
        print(('-'*37).center(40))
        print(f'PIEDRA, PAPEL O TIJERA'.center(40))
        print(f"Intenta ganar a la máquina".center(40))
        print(f" ")
        print(f"Reglas:".center(40))
        print(f"Papel vence a Piedra".center(40))
        print(f"Piedra vence a Tijera".center(40))
        print(f"Tijeras vence a Papel".center(40))
        print(f"La vencedora será quien consiga 3 victorias".center(40))
        print(f" ") 

    def piedrapapeltijera_empate(self):
        print(f"-------------- Ronda {self.ronda} --------------".center(40))
        print(f"¡Ha habido un empate!".center(40))
        print(f"Has escogido {self.jugadora} y la máquina {self.maquina}".center(40))
        print(f"---- Jugadora ({self.puntos_jugadora}) vs. Máquina ({self.puntos_maquina}) ---".center(40))
        print(f" ")

    def piedrapapeltijera_puntomaquina(self):
        print(f"-------------- Ronda {self.ronda} --------------".center(40))
        print(f"¡Lástima! Has perdido...".center(40))
        print(f"Has escogido {self.jugadora} y la máquina {self.maquina}".center(40))
        print(f"---- Jugadora ({self.puntos_jugadora}) vs. Máquina ({self.puntos_maquina}) ---".center(40))
        print(f" ")

    def piedrapapeltijera_puntojugadora(self):
        print(f"-------------- Ronda {self.ronda} --------------".center(40))
        print(f"¡Genial! ¡Has ganado!".center(40))
        print(f"Has escogido {self.jugadora} y la máquina {self.maquina}".center(40))
        print(f"---- Jugadora ({self.puntos_jugadora}) vs. Máquina ({self.puntos_maquina}) ---".center(40))
        print(f" ")

    def piedrapapeltijera_ganajugadora(self):
        print(f"¡¡HAS GANADO AL PIEDRA, PAPEL O TIJERA!!".center(40))
        print(f"Venciste a la máquina con un total de {self.puntos_jugadora} puntos".center(40))
        print(self.banner1.center(40))

    def piedrapapeltijera_ganamaquina(self):
        print(f"PERDISTE AL PIEDRA, PAPEL O TIJERA...".center(40))
        print(f"Te quedaste con un total de {self.puntos_jugadora} punto(s)".center(40))
        print(self.banner1.center(40))

import random
import string

class Ahorcado(Juegos):
    def __init__ (self):
        self.lista = ['casa', 'perro', 'cachopo', 'dinosaurio', 'python',
              'bucle', 'pesadilla', 'anaconda', 'lista', 'funcion',
              'variable', 'gato', 'lapiz', 'pez', 'sol', 'clavo',
              'pais', 'oro', 'mesa', 'vaso', 'vino', 'cuadro',
              'elefante', 'estrella', 'universo', 'ventana', 'ordenador',
              'quimera']
        self.ahorcado = ['''

  +---+
  |   |
      |
      |
      |
      |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
        self.palabra_secreta = random.choice(self.lista)
        self.guiones = '_ ' * len(self.palabra_secreta)
        self.lista_guiones = self.guiones.split()
        self.vidas = 7
        self.letras_dichas = []
        self.intentos = 0
        self.letra = ''

    
    def validar_letra(self): # aquí validamos si la letra es, en efecto, una letra
        self.validacion = False
        while not self.validacion:
            self.letra = input('Introduce una letra').lower()
            if self.letra in string.ascii_lowercase:
                self.letras_dichas.extend(self.letra)
                self.validacion = True
            else:
                return f'{self.letra} no es una opción válida'
            
       
            
    def adivinar_letra(self):
        
        if self.letra in self.palabra_secreta:
           for i in range(len(self.palabra_secreta)):
                if self.palabra_secreta[i] == self.letra:
                    self.lista_guiones[i] = self.letra
                    self.guiones = " ".join(self.lista_guiones)
                    self.ahorcado_adivinar_letra()
                    
                else:
                    self.vidas -= 1
                    self.intentos += 1
                    self.ahorcado_fallar_letra()



    def fin_juego(self):
        if self.guiones.replace(' ', '') == self.palabra_secreta:
            print('Enhorabuena, figura. ¡Has ganado!')

        else:
            print(f'Mala suerte. ¡Perdiste! La palabra era: {self.palabra_secreta}')

            

    def insert_coin(self):
        self.ahorcado_banner_inicio()
            
        while self.vidas > 0 and self.guiones.replace(' ', '') != self.palabra_secreta:
            self.validar_letra()

            self.adivinar_letra()                      

        self.fin_juego()

ahorcado = Ahorcado()

jugar_ahorcado = ahorcado.insert_coin()