from Analisis.Lexema import *
from Analisis.Error import *
from Analisis.Token import *


class Lexico:

    def __init__(self) -> None:
        self.estado = 0
        self.indice = 0
        self.fila = 1
        self.col = 1
        self.prefijo = ''
        self.entrada = list()
        self.tokens = list()
        self.errores = list()
        self.imgs = list()
        self.img = dict()
        self.contenedor = list()
        self.subcont = list()
        self.reserved = [
            'while', 'do',
            'if', 'else',
            'return','void'
        ]

    def escanear(self, entrada):
        self.str_to_list(entrada)
        while self.indice < len(self.entrada):
            if self.getSeparador():
                continue
            elif self.getCommentLine():
                continue
            elif self.getCommentMultiLine():
                continue
            elif self.getOperatorRs():
                continue
            elif self.getOperators():
                continue
            # elif self.getOperatorLs():
            #     continue
            else:  # Hay un error léxico
                self.error()
                


    def str_to_list(self, entrada):
        chars = list()
        for c in entrada:
            chars.append(c.lower())
        self.entrada = chars


    def sigChar(self) -> str:
        if self.indice < len(self.entrada):
            return self.entrada[self.indice]
        else:
            return ''

    def getLexema(self,descripcion) -> Lexema:
        lexema = Lexema(self.prefijo, descripcion, self.fila, self.col)
        self.prefijo = ''
        return lexema
    
    def getCommentLine(self) -> bool:
        self.regresar()
        tipo = ''
        descripcion = ''
        while 1:
            if self.estado == 0:
                if self.sigChar() == '/':
                    self.transicion(1)
                    self.walk('go')
                else:
                    return False
            elif self.estado == 1:
                if self.sigChar() == '/':
                    self.transicion(2)
                    self.walk('go')
                else:
                    self.walk('back')
                    return False
            elif self.estado == 2:
                c = self.sigChar()
                if c != '\n' and self.indice < len(self.entrada):
                    self.transicion(2)
                    self.walk('go')
                elif c == '\n':
                    tipo = 'comment_line'
                    descripcion = 'Comentario de una Linea'
                    token = Token(tipo, self.getLexema(descripcion))
                    self.addToken(token)
                    return True
                else:
                    if self.indice == len(self.entrada):
                        tipo = 'comment_line'
                        descripcion = 'Comentario de una Linea'
                        token = Token(tipo, self.getLexema(descripcion))
                        self.addToken(token)
                        return True
                    else:
                        return False
                
    def getCommentMultiLine(self) -> bool:
        self.regresar()
        tipo = ''
        descripcion = ''
        while 1:
            if self.estado == 0:
                if self.sigChar() == '/':
                    self.transicion(1)
                    self.walk('go')
                else:
                    return False
            elif self.estado == 1:
                if self.sigChar() == '*':
                    self.transicion(2)
                    self.walk('go')
                else:
                    self.walk('back')
                    return False
            elif self.estado == 2:
                c = self.sigChar()
                if c == '\n':
                    self.getSeparador()
                    continue
                #/*hola59*/
                elif c != '*' and c != '\n' and self.check() != '':
                    self.transicion(2)
                    self.walk('go')
                #9
                elif c != '*' and c != '\n' and self.check() == '':
                    self.transicion(2)
                    return False
                elif c == '*' and self.check() == '':
                    self.transicion(2)
                    return False
                elif c == '*' and c != '\n' and self.check() != '/' and self.check != '':
                    self.transicion(2)
                    self.walk('go')
                elif c == '*' and self.check() == '/':
                    self.transicion(3)
                    self.walk('go')
                else:
                    return False
            elif self.estado == 3:
                if self.sigChar() == '/':
                    self.transicion(4)
                    self.walk('go')
            elif self.estado == 4:
                tipo = 'comment_multiLine'
                descripcion = 'Comentario multilinea Linea'
                token = Token(tipo, self.getLexema(descripcion))
                self.addToken(token)
                return True

    def getOperatorRs(self) -> bool:
        self.regresar()
        tipo = ''
        descripcion = ''
        while 1:
            if self.estado == 0:
                if self.sigChar() == '=':
                    self.transicion(1)
                    self.walk('go')
                elif self.sigChar() == '!':
                    self.transicion(3)
                    self.walk('go')
                elif self.sigChar() == '>':
                    self.transicion(4)
                    self.walk('go')
                elif self.sigChar() == '<':
                    self.transicion(5)
                    self.walk('go')
                else:
                    return False
            elif self.estado == 1:
                if self.sigChar() == '=':
                    self.transicion(2)
                    self.walk('go')
                    tipo = 'operator_Rs'
                    descripcion = 'Operador de relacion Igualacion'
                else:
                    self.walk('back')
                    return False
            elif self.estado == 3:
                if self.sigChar() == '=':
                    self.transicion(2)
                    self.walk('go')
                    tipo = 'operator_Rs'
                    descripcion = 'Operador de relacion Diferenciacion'
                else:
                    self.walk('back')
                    return False
            elif self.estado == 4:
                if self.sigChar() == '=':
                    self.transicion(2)
                    self.walk('go')
                    tipo = 'operator_Rs'
                    descripcion = 'Operador de relacion Mayor igual'
                else:
                    self.walk('back')
                    return False
            elif self.estado == 5:
                if self.sigChar() == '=':
                    self.transicion(2)
                    self.walk('go')
                    tipo = 'operator_Rs'
                    descripcion = 'Operador de relacion Menor igual'
                else:
                    self.walk('back')
                    return False
            elif self.estado == 2:
                token = Token(tipo, self.getLexema(descripcion))
                self.addToken(token)
                return True
                
    def getOperators(self) -> bool:
        self.regresar()
        tipo = ''
        descripcion = ''
        while 1:
            if self.estado == 0:
                if self.sigChar() == '+':
                    self.transicion(1)
                    self.walk('go')
                    tipo = 'operator_Ar'
                    descripcion = 'Operador aritmetico suma'
                elif self.sigChar() == '-':
                    self.transicion(1)
                    self.walk('go')
                    tipo = 'operator_Ar'
                    descripcion = 'Operador aritmetico resta'
                elif self.sigChar() == '*':
                    self.transicion(1)
                    self.walk('go')
                    tipo = 'operator_Ar'
                    descripcion = 'Operador aritmetico multiplicacion'
                elif self.sigChar() == '/':
                    self.transicion(1)
                    self.walk('go')
                    tipo = 'operator_Ar'
                    descripcion = 'Operador aritmetico division'
                elif self.sigChar() == '%':
                    self.transicion(1)
                    self.walk('go')
                    tipo = 'operator_Ar'
                    descripcion = 'Operador aritmetico resto'
                elif self.sigChar() == '=':
                    self.transicion(1)
                    self.walk('go')
                    tipo = 'operator_Ar'
                    descripcion = 'Operador de asignación'
                elif self.sigChar() == '>':
                    self.transicion(1)
                    self.walk('go')
                    tipo = 'operator_Rs'
                    descripcion = 'Operador de relacion Mayor'
                elif self.sigChar() == '<':
                    self.transicion(1)
                    self.walk('go')
                    tipo = 'operator_Rs'
                    descripcion = 'Operador de relacion Menor'
                else:
                    return False
            elif self.estado == 1:
                token = Token(tipo, self.getLexema(descripcion))
                self.addToken(token)
                return True

    def getOperatorLs(self) -> bool:
        self.regresar()
        tipo = ''
        descripcion = ''
        while 1:
            if self.estado == 0:
                if self.sigChar() == '&':
                    self.transicion(1)
                    self.walk('go')
                elif self.sigChar() == '|':
                    self.transicion(3)
                    self.walk('go')
                elif self.sigChar() == '!':
                    self.transicion(2)
                    self.walk('go')
                    tipo = 'operator_Ls'
                    descripcion = 'Operador logico not'
                else:
                    return False
            elif self.estado == 1:
                if self.sigChar() == '&':
                    self.transicion(2)
                    self.walk('go')
                    tipo = 'operator_Ls'
                    descripcion = 'Operador logico and'
                else:
                    self.walk('back')
                    return False
            elif self.estado == 3:
                if self.sigChar() == '|':
                    self.transicion(2)
                    self.walk('go')
                    tipo = 'operator_Ls'
                    descripcion = 'Operador logico or'
                else:
                    self.walk('back')
                    return False
            elif self.estado == 2:
                token = Token(tipo, self.getLexema(descripcion))
                self.addToken(token)
                return True
          
    def getSeparador(self) -> bool:
        c = self.sigChar()
        if c == ' ' or c == '\t':
            self.consumir()
            self.walk('go')
            return True
        elif self.sigChar() == '\n':
            self.updateCount()
            self.walk('go')
            return True
        else:
            return False

    def transicion(self, estado: int):
        self.prefijo += self.consumir()
        self.estado = estado

    def walk(self, accion) -> None:
        if accion == 'go':
            self.indice += 1
        elif accion == 'back':
            self.indice -= 1
        
    def consumir(self) -> str:
        self.col += 1
        return self.entrada[self.indice]
    
    def check(self) -> bool:
        if self.indice < len(self.entrada): 
            if self.indice != (len(self.entrada)-1):
                return self.entrada[self.indice+1]
            else:
                return ''
        else:
            return 'None'

    def updateCount(self):
        self.fila += 1
        self.col = 1

    def addToken(self, t: Token):
        self.tokens.append(t)
        self.estado = 0

    def regresar(self):
        self.prefijo = ''
        self.estado = 0

    def error(self):            
        err = Error(self.fila, self.col, self.prefijo)
        self.errores.append(err)
        self.estado = 0
        self.prefijo = ''
        if self.indice < len(self.entrada):
            self.indice += 1
