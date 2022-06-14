from re import L
from numpy import character


class Estados():

    def __init__(self) -> None:
        self.estado_dict = dict()

    def arbol(self, tipo,lexema) -> list:
        valor_estado = ''
        if tipo == 'tk_dato_int':
            valor_estado = self.EstadosNumeroEntero(lexema)
        elif tipo == 'tk_dato_double':
            pass
        return valor_estado
    
    def EstadosNumeroEntero(self,lexema) -> list:
        lista_estados = ['S0','S1']
        indice = 0
        large = 0
        lexema_reade = ''
        estadoNumEntero = list()
        while indice < len(lexema):
            if large == 0:
                estado = f'{lista_estados[0]}'
            else:
                estado = f'{lista_estados[1]}'
            
            caracter = lexema[indice]
            
            if indice == 0:
                transicion = f'{lista_estados[1]}'
            else:
                transicion = f'{lista_estados[1]}'
                
            estadoNumEntero.append([estado, caracter, lexema_reade, transicion])
            lexema_reade += lexema[indice]
            indice += 1
            large +=1
        
        if indice == len(lexema):
            estadoNumEntero.append(
                [estado, '#', lexema, transicion])

        
        return estadoNumEntero
        
        
        
        