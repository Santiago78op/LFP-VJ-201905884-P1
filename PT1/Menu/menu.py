import os
from colorama import Fore
from Analisis.Lexico import Lexico
from HTML.reportes import HTML


class Menu():

    def __init__(self):
        self.diccionario_elementos = ''
        self.cargar = 1
        self.nombre_html = 2
        self.salir = 0

    def mostrar_menu(self) -> None:
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
        print(Fore.CYAN, f'''\t<--Menu Principal-->\n
Selecciona una opción:\n
    \t{self.cargar }) - Cargar Archivo 
    \t{self.nombre_html}) - Nombre del Archivo
    \t{self.salir}) - Salir\n''')

    def menu(self) -> None:
        name_html = ''
        while True:

            self.mostrar_menu()

            opcionMenu = input("Inserta el numero de la opcion: >> ")

            try:
                opcionMenu = int(opcionMenu)

                os.system('cls')

                if opcionMenu == self.cargar:
                    carga = input("Inserta la ruta del archivo .cs: >> \n")

                    try:
                        archivo = open(carga, encoding="utf8").read()
                        archivo = archivo.lower()
                        print(Fore.LIGHTYELLOW_EX, 'Archivo Cargado con Exito!!!')
                        lex = Lexico()
                        self.diccionario_elementos = lex.scanner(archivo)
                    except OSError as exception:
                        print(f"\n Error: {exception}")

                elif opcionMenu == self.nombre_html:
                    if self.diccionario_elementos != '':
                        name_html = input(
                            "Ingresa nombre del archivo .html: >> \n")
                        html = HTML()
                        html.createHTML(name_html, self.diccionario_elementos)
                        
                    else:
                        print(Fore.LIGHTYELLOW_EX, 'Necesitas Cargar Archivo antes')                    

                elif opcionMenu == self.salir:
                    print("\nEsto no es un adios sino un asta pronto!!!!!!\n")
                    False
                    break
                else:
                    print(Fore.YELLOW, 'Opcion no válida...')
                input('\nPresiona enter para Ingresar al Menú...')

            except ValueError as error:
                opcionMenu = -1
                print(Fore.RED, f'Error: {error}')
                print(Fore.RED, 'El programa no permite carateres tipo Caracter')
                input('Presione la tecla para continuar@')

