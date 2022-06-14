# Ejemplo de implementación de un analizador léxico

# LENGUAJE

'''
# Definición de tokens

| Token             | Descripción                         | Patrón                                                  |
| ----------------- | ----------------------------------- | ------------------------------------------------------- |
| comment_line      | Comentario de una Linea             | //.\*                                                   |
| comment_multiLine | Comentario multilinea Linea         | \/\*([^\*]|\n)\*\*\/                                    |
| tipo_int          | Tipo de dato int                    | int                                                     |
| tipo_double       | Tipo de dato double                 | double                                                  |
| tipo_string       | Tipo de dato string                 | string                                                  |
| tipo_char         | Tipo de dato char                   | char                                                    |
| tipo_boolean      | Tipo de dato boolean                | boolena                                                 |
| tipo              | Tipo de dato                        | tipo_int/tipo_double/tipo_string/tipo_char/tipo_boolean |
| identificador     | Simbolo nombre entidad              | ^([a-zA-Z_])([\w]*)                                     |
| operator_Ar       | Operador aritmetico suma            | +                                                       |
| operator_Ar       | Operador aritmetico resta           | -                                                       |
| operator_Ar       | Operador aritmetico multiplicacion  | \*                                                      |
| operator_Ar       | Operador aritmetico division        | /                                                       |
| operator_Ar       | Operador aritmetico resto           | %                                                       |
| operator_As       | Operador de asignación              | =                                                       |
| operator_Rs       | Operador de relacion Igualacion     | ==                                                      |
| operator_Rs       | Operador de relacion Diferenciacion | !=                                                      |
| operator_Rs       | Operador de relacion Mayor          | >                                                       |
| operator_Rs       | Operador de relacion Mayor igual    | >=                                                      |
| operator_Rs       | Operador de relacion Menor          | <                                                       |
| operator_Rs       | Operador de relacion Menor igual    | <=                                                      |
| operator_Ls       | Operador logico and                 | &&                                                      |
| operator_Ls       | Operador logico or                  | ||                                                      |
| operator_Ls       | Operador logico not                 | !                                                       |
| dato_int          | Tipo de dato int                    | [+|-]?([0-9]+)                                          |
| dato_double       | Tipo de dato double                 | [+-]?([0-9]*[.])?[0-9]+                                 |
| dato_string       | Tipo de dato string                 | "([^"]\|(\"))*"                                         |
| dato_char         | Tipo de dato char                   | "([^"]\|(\"))"                                          |
| dato_boolean      | Tipo de dato boolean                | ^(false|true)                                           |
| dato              | Dato de cualquier tipo              | dato_int/dato_double/dato_string/dato_char/dato_boolean |
| conditional_if    | Estructura condicional if           | if                                                      |
| conditional_else  | Estructura condicional else         | else                                                    |
| iterative_do      | Estructura iterativa do             | do                                                      |
| iterative_while   | Estructura iterativa while          | while                                                   |
| parA              | Paréntesis abierto                  | (                                                       |
| parB              | Paréntesis cerrado                  | )                                                       |
| punto_coma        | Punto y coma                        | ;                                                       |
| llaveA            | Llave abierta                       | {                                                       |
| llaveB            | Llave cerrada                       | }                                                       |
| metodo_void       | Metodo void                         | void                                                    |
| coma              | Operador coma                       |  ,                                                      |
| metodo_run        | Retorna un valor                    |  return                                                 |
| corA              | Corchete abierto                    | [                                                       |
| corB              | Corchete cerrado                    | ]                                                       |
| punto             | Operador punto                      | .                                                       |
'''

# IMPLEMENTACIÓN

from Analisis.Lexema import *
from Analisis.Error import *
from Analisis.Token import *
from Analisis.Estados import *
import os


class Lexico():

    def __init__(self) -> None:
        self.list_tokens = list()
        self.list_errors = list()
        self.digito = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                      "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","_"]
        self.punto = ["."]
        self.asterisco = ["*"]
        self.diagonal = ["/"]
        self.vacio = []
        self.saltoLinea = ["\n"]
        self.omite = ["*", "/"]
        self.string = ["\""]
        self.char = ["'"]
        self.IGNORAR = " \n\t"
        self.tokens = {
            # "tk_dato_string": self.AFDString,
            # "tk_dato_char": self.AFDChar,
            # "tk_operadorRs_igualacion": "==",
            # "tk_operadorRs_diferenciacion": "!=",
            # "tk_operadorRs_MayorIgual": ">=",
            # "tk_operadorRs_MenorIgual": "<=",
            # "tk_operadorLs_and": "&&",
            # "tk_operadorLs_or": "||",
            # "tk_operadorLs_not": "!",
            # "tk_operadorAs_asignacion": "=",
            # "tk_operatorAr_suma": "+",
            # "tk_operatorAr_resta": "-",
            # "tk_comment_multiLine": self.ADFCommentMultyLine,
            # "tk_operadorAr_multiplicacion": "*",
            # "tk_comment_line": self.ADFCommentLine,
            # "tk_operadorAr_division": "/",
            # "tk_operadorAr_resto": "%",
            # "tk_operadorRs_Menor": ">",
            # "tk_operadorRs_Mayor": "<",
            # "tk_parA": "(",
            # "tk_parC": ")",
            # "tk_llaveA": "{",
            # "tk_llaveC": "}",
            # "tk_puntoYcoma": ";",
            # "tk_coma": ",",
            # "tk_tipo_int": "int",
            # "tk_tipo_double": "double",
            # "tk_tipo_string": "string",
            # "tk_tipo_char": "char",
            # "tk_tipo_boolean": "boolean",
            # "tk_metodo_void": "void",
            # "tk_metodo_return": "return",
            # "tk_conditional_if": "if",
            # "tk_conditional_else": "else",
            # "tk_iterative_do": "do",
            # "tk_iterative_while": "while",
            # "tk_dato_boolean_true": "true",
            # "tk_dato_boolean_false": "false",
            # "tk_dato_double": self.AFDNumeroDouble,
            "tk_dato_int": self.AFDNumeroEntero,
            #"tk_identificador": self.AFDIdentificador,
        }

    def _descriptionsTk(self, patron, _token) -> str:
        descipcion = {
            "==": "Operador de relacion Igualacion",
            "!=": "Operador de relacion Diferenciacion",
            ">=": "Operador de relacion Mayor igual",
            "<=": "Operador de relacion Menor igual",
            "&&": "Operador logico and",
            "||": "Operador logico or",
            "!": "Operador logico not",
            "=": "Operador de asignación",
            "+": "Operador aritmetico suma	",
            "-": "Operador aritmetico resta",
            "*": "Operador aritmetico multiplicacion",
            "/": "Operador aritmetico division",
            "%": "Operador aritmetico resto",
            ">": "Operador de relacion Mayor",
            "<": "Operador de relacion Menor",
            "(": "Paréntesis abierto",
            ")": "Paréntesis cerrado",
            "{": "Llave abierta",
            "}": "Llave cerrada",
            ";": "Punto y coma",
            ",": "Operador coma",
            "tk_tipo_int": "Tipo de dato int",
            "tk_tipo_double": "Tipo de dato double",
            "tk_tipo_string": "Tipo de dato string",
            "tk_tipo_char": "Tipo de dato char",
            "tk_tipo_boolean": "Tipo de dato boolean",
            "tk_metodo_void": "Funcion no retorna valor",
            "tk_metodo_return": "Retorna un valor",
            "tk_conditional_if": "Estructura condicional if",
            "tk_conditional_else": "Estructura condicional else",
            "tk_iterative_do": "Estructura iterativa do",
            "tk_iterative_while": "Estructura iterativa while",
            "tk_dato_int": "Tipo de dato int",
            "tk_dato_double": "Tipo de dato double",
            "tk_comment_line": "Comentario de una Linea",
            "tk_comment_multiLine": "Comentario multilinea Linea",
            "tk_dato_string": "Tipo de dato string",
            "tk_dato_char": "Tipo de dato char",
            "tk_dato_boolean_true": "Tipo de dato boolean",
            "tk_dato_boolean_false": "Tipo de dato boolean",
            "tk_identificador": "Simbolo nombre entidad",
        }

        patrones = {
            "==": "==",
            "tk_dato_int": "[+|-]?([0-9]+)",
        }
        
        dict_contenido = dict()
        for token, description in descipcion.items():
            if patron == token:
                dict_contenido['description'] = description
            elif _token == token:
                dict_contenido['description'] = description
        
        for token, ptr in patrones.items():
            if patron == token:
                dict_contenido['patron'] = ptr
            elif _token == token:
                dict_contenido['patron'] = ptr
        
        return dict_contenido

    def ADFCommentLine(self, lexema):
        estado = 0
        estados_aceptacion = [2,3]

        for char in lexema:
            if estado == 0:
                if char in self.diagonal:
                    estado = 1

                else:
                    estado = -1

            elif estado == 1:

                if char in self.diagonal:
                    estado = 2

                else:
                    estado = -1

            elif estado == 2:

                if char not in self.vacio:
                    estado = 2
                
                elif char == '\n':
                    estado = 3

                else:
                    estado = -1

            if estado == -1:
                return False

        return estado in estados_aceptacion

    def ADFCommentMultyLine(self, lexema):
        estado = 0
        estados_aceptacion = [4]

        for char in lexema:
            if estado == 0:

                if char in self.diagonal:
                    estado = 1

                else:
                    estado = -1

            elif estado == 1:

                if char in self.asterisco:
                    estado = 2

                else:
                    estado = -1

            elif estado == 2:

                if char not in self.omite:
                    estado = 2

                elif char in self.asterisco:
                    estado = 3
                
                elif char == '\n':
                    estado = 3

                else:
                    estado = -1

            elif estado == 3:

                if char in self.asterisco:
                    estado = 3

                elif char in self.diagonal:
                    estado = 4

                else:
                    estado = -1
            
            elif estado == 4:
                estado = -1
                
            if estado == -1:
                return False

        return estado in estados_aceptacion

    def AFDChar(self, lexema):
        estado = 0
        estados_aceptacion = [2]

        for char in lexema:
            if estado == 0:
                if char in self.char:
                    estado = 1

                else:
                    estado = -1

            elif estado == 1:

                if char not in self.saltoLinea and char not in self.char:
                    estado = 1
                    
                elif char in self.char:
                    estado = 2

                else:
                    estado = -1
            
            elif estado == 2:
                estado = -1


            if estado == -1:
                return False

        return estado in estados_aceptacion   

    def AFDString(self, lexema):
        estado = 0
        estados_aceptacion = [2]

        for char in lexema:
            if estado == 0:
                
                if char in self.string:
                    estado = 1

                else:
                    estado = -1

            elif estado == 1:

                if char not in self.saltoLinea and char not in self.string:
                    estado = 1
                    
                elif char in self.string:
                    estado = 2

                else:
                    estado = -1
                    
            elif estado == 2:
                estado =-1


            if estado == -1:
                return False

        return estado in estados_aceptacion

    def AFDNumeroDouble(self, lexema):
        estado = 0
        estados_aceptacion = [3]

        for char in lexema:
            if estado == 0:

                if char in self.digito:
                    estado = 1

                elif char in self.punto:
                    estado = 2

                else:
                    estado = -1

            elif estado == 1:

                if char in self.digito:
                    estado = 1

                elif char in self.punto:
                    estado = 2

                else:
                    estado = -1

            elif estado == 2:

                if char in self.digito:
                    estado = 3

                else:
                    estado = -1

            elif estado == 3:

                if char in self.digito:
                    estado = 3

                else:
                    estado = -1

            if estado == -1:
                return False

        return estado in estados_aceptacion

    def AFDNumeroEntero(self, lexema):
        estado = 0
        estados_aceptacion = [1]

        for char in lexema:
            if estado == 0:
                if char in self.digito:
                    estado = 1

                else:
                    estado = -1

            elif estado == 1:

                if char in self.digito:
                    estado = 1

                else:
                    estado = -1

            if estado == -1:
                return False

        return estado in estados_aceptacion

    def AFDIdentificador(self,lexema):
        estado = 0
        estados_aceptacion = [1]

        for char in lexema:
            if estado == 0:
                
                if char in self.letra:
                    estado = 1

                else:
                    estado = -1

            elif estado == 1:
                
                if char in self.letra or char in self.digito:
                    estado = 1

                else:
                    estado = -1
            
            if estado == -1:
                return False

        return estado in estados_aceptacion


    def scanner(self, codigo):
        fila, columna = 1, 1
        indice = 0
        lexema = ''
        _dictEstados = ''

        while indice < len(codigo):
            caracter = codigo[indice]
            reconocido = False

            # Conteo de líneas
            if caracter == "\n":
                fila += 1
                columna = 1

            # Caracteres a ignorar
            if caracter in self.IGNORAR:
                indice += 1
                continue

            for token, patron in self.tokens.items():
                if isinstance(patron, str):
                    if indice + len(patron) > len(codigo):
                        continue

                    lexema = codigo[indice: indice + len(patron)]

                    if lexema == patron:
                        reconocido = True
                        indice += len(patron)
                        columna += len(patron)
                        descripcion = self._descriptionsTk(token, patron)
                        _lexema = Lexema(
                            lexema, descripcion['description'], fila, columna, descripcion['patron'])
                        _token = Token(token, _lexema)
                        self.list_tokens.append(_token)
                        print(f"RECONOCIDO: '{lexema}' | {token} - {patron}")

                else:  # AFD
                    # \n # \n $ 
                    #  0,1, 2,3 = 4
                    indice_adelante = indice + 1
                    anterior_reconocido = False

                    while indice_adelante <= len(codigo):
                        lexema = codigo[indice: indice_adelante] # -> #\n$
                        reconocido = patron(lexema)

                        if not reconocido and anterior_reconocido:
                            lexema = codigo[indice: indice_adelante - 1]
                            reconocido = True
                            indice = indice_adelante - 1
                            break

                        anterior_reconocido = reconocido
                        indice_adelante += 1

                    if reconocido:
                        if '\n' in lexema:
                            descripcion = self._descriptionsTk(token, patron)
                            _lexema = Lexema(
                                lexema, descripcion['description'], fila, columna, descripcion['patron'])
                            _token = Token(token, _lexema)
                            self.list_tokens.append(_token)
                            print(f"RECONOCIDO: '{lexema}' | {token} - AFD")
                            indice = indice_adelante - 1
                        else:
                            columna += len(lexema)
                            descripcion = self._descriptionsTk(token, patron)
                            _lexema = Lexema(
                                lexema, descripcion['description'], fila, columna, descripcion['patron'])
                            _token = Token(token, _lexema)
                            _estadosTabla = Estados()
                            _dictEstados = _estadosTabla.arbol(token, lexema)
                            self.list_tokens.append(_token)
                            print(f"RECONOCIDO: '{lexema}' | {token} - AFD")
                            indice = indice_adelante - 1
                    
                if reconocido:
                    break

            if not reconocido:
                if indice_adelante > len(codigo):
                    lexema = codigo[indice]
                _error = Error(fila, columna, lexema)
                self.list_errors.append(_error)
                print(f"Error Lexico: '{lexema}' ")
                indice += 1

        diccionario = {'tokens': self.list_tokens,
                       'errores': self.list_errors, 'estados': _dictEstados}
        return diccionario
