from Analisis.Buil import Buil

class Estados():


    def arbol(self, tipo,lexema) -> list:
        constructor = ''
        if tipo == 'tk_dato_int':
            valor_estado = self.EstadosNumeroEntero(lexema)
            constructor = Buil(tipo,lexema,valor_estado)
        elif tipo == 'tk_dato_double':
            valor_estado = self.EstadosNumeroDouble(lexema)
            constructor = Buil(tipo, lexema, valor_estado)
        elif tipo == 'tk_identificador':
            valor_estado = self.EstadosIdentificador(lexema)
            constructor = Buil(tipo, lexema, valor_estado)
        elif tipo == 'tk_comment_line':
            valor_estado = self.EstadosCommentLine(lexema)
            constructor = Buil(tipo, lexema, valor_estado)
        elif tipo == 'tk_comment_multiLine':
            valor_estado = self.EstadosCommentMultyLine(lexema)
            constructor = Buil(tipo, lexema, valor_estado)
        elif tipo == 'tk_dato_string':
            valor_estado = self.EstadosString(lexema)
            constructor = Buil(tipo, lexema, valor_estado)
        elif tipo == 'tk_dato_char':
            valor_estado = self.EstadosChar(lexema)
            constructor = Buil(tipo, lexema, valor_estado)
        return constructor
    
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
                [estado, '#', lexema, f'{transicion} -> (aceptacion)'])

        
        return estadoNumEntero
        
    def EstadosNumeroDouble(self, lexema) -> list:
        lista_estados = ['S0', 'S1', 'S2', 'S3']
        indice = 0
        large = 0
        caracter = ''
        lexema_reade = ''
        estadoNumDouble = list()
        while indice < len(lexema):
            if large == 0 and lexema[indice].isdigit():
                caracter = lexema[indice]
                estado = f'{lista_estados[0]}'
                transicion = f'{lista_estados[1]}'
            elif large == 0 and lexema[indice] == '.':
                caracter = lexema[indice]
                estado = f'{lista_estados[0]}'
                transicion = f'{lista_estados[2]}'
            
            if large != 0 and transicion == 'S1' and lexema[indice].isdigit():
                caracter = lexema[indice]
                estado = f'{lista_estados[1]}'
                transicion = f'{lista_estados[1]}'
            elif large != 0 and transicion == 'S1' and lexema[indice] == '.':
                caracter = lexema[indice]
                estado = f'{lista_estados[1]}'
                transicion = f'{lista_estados[2]}'
            elif large != 0 and transicion == 'S2' and lexema[indice].isdigit():
                caracter = lexema[indice]
                estado = f'{lista_estados[2]}'
                transicion = f'{lista_estados[3]}'

            if large != 0 and transicion == 'S2' and lexema[indice].isdigit():
                caracter = lexema[indice]
                estado = f'{lista_estados[2]}'
                transicion = f'{lista_estados[3]}'
            elif large != 0 and transicion == 'S3' and lexema[indice].isdigit():
                caracter = lexema[indice]
                estado = f'{lista_estados[2]}'
                transicion = f'{lista_estados[3]}'

            estadoNumDouble.append(
                [estado, caracter, lexema_reade, transicion])
            lexema_reade += lexema[indice]
            indice += 1
            large += 1

        if indice == len(lexema):
            estadoNumDouble.append(
                [estado, '#', lexema, f'{transicion} -> (aceptacion)'])

        return estadoNumDouble

    def EstadosIdentificador(self, lexema) -> list:
        lista_estados = ['S0','S1']
        indice = 0
        large = 0
        lexema_reade = ''
        estadoIdentificador = list()
        while indice < len(lexema):
            if large == 0 and not lexema[indice].isdigit():
                caracter = lexema[indice]
                estado = f'{lista_estados[0]}'
                transicion = f'{lista_estados[1]}'
            elif large != 0:
                caracter = lexema[indice]
                estado = f'{lista_estados[1]}'
                transicion = f'{lista_estados[1]}'
                
            estadoIdentificador.append(
                [estado, caracter, lexema_reade, transicion])
            lexema_reade += lexema[indice]
            indice += 1
            large +=1
        
        if indice == len(lexema):
            estadoIdentificador.append(
                [estado, '#', lexema, f'{transicion} -> (aceptacion)'])

        return estadoIdentificador

    def EstadosCommentLine(self, lexema) -> list:
        lista_estados = ['S0', 'S1', 'S2']
        indice = 0
        large = 0
        lexema_reade = ''
        estadoIdentificador = list()
        while indice < len(lexema):
            if large == 0 and lexema[indice] == '/':
                caracter = lexema[indice]
                estado = f'{lista_estados[0]}'
                transicion = f'{lista_estados[1]}'
            elif large == 1 and lexema[indice] == '/':
                caracter = lexema[indice]
                estado = f'{lista_estados[1]}'
                transicion = f'{lista_estados[2]}'
                
            if large != 0 and transicion == 'S2':
                caracter = lexema[indice]
                estado = f'{lista_estados[2]}'
                transicion = f'{lista_estados[2]}'

            estadoIdentificador.append(
                [estado, caracter, lexema_reade, transicion])
            lexema_reade += lexema[indice]
            indice += 1
            large += 1

        if indice == len(lexema):
            estadoIdentificador.append(
                [estado, '#', lexema, f'{transicion} -> (aceptacion)'])

        return estadoIdentificador

    def EstadosCommentMultyLine(self, lexema) -> list:
        lista_estados = ['S0', 'S1', 'S2','S3','S4']
        indice = 0
        large = 0
        lexema_reade = ''
        estadoCM = list()
        while indice < len(lexema):
            if large == 0 and lexema[indice] == '/':
                caracter = lexema[indice]
                estado = f'{lista_estados[0]}'
                transicion = f'{lista_estados[1]}'
            elif large == 1 and lexema[indice] == '*':
                caracter = lexema[indice]
                estado = f'{lista_estados[1]}'
                transicion = f'{lista_estados[2]}'

            if large != 0 and transicion == 'S2' and indice != (len(lexema)-1):
                caracter = lexema[indice]
                estado = f'{lista_estados[2]}'
                transicion = f'{lista_estados[2]}'
            elif large != 0 and transicion == 'S2' and indice == (len(lexema)-1):
                caracter = lexema[indice]
                estado = f'{lista_estados[2]}'
                transicion = f'{lista_estados[3]}'

            estadoCM.append(
                [estado, caracter, lexema_reade, transicion])
            lexema_reade += lexema[indice]
            indice += 1
            large += 1

        if indice == len(lexema):
            estadoCM.append(
                [lista_estados[3], '#', lexema, f'{lista_estados[4]} -> (aceptacion)'])

        return estadoCM

    def EstadosString(self, lexema) -> list:
        lista_estados = ['S0', 'S1', 'S2']
        indice = 0
        large = 0
        lexema_reade = ''
        estadoString = list()
        while indice < len(lexema):
            if large == 0 and lexema[indice] == '"':
                caracter = lexema[indice]
                estado = f'{lista_estados[0]}'
                transicion = f'{lista_estados[1]}'
                estadoString.append(
                    [estado, caracter, lexema_reade, transicion])
                lexema_reade += lexema[indice]
                indice += 1
                large += 1
            elif large != 0 and lexema[indice] != '"':
                caracter = lexema[indice]
                estado = f'{lista_estados[1]}'
                transicion = f'{lista_estados[1]}'
                estadoString.append(
                    [estado, caracter, lexema_reade, transicion])
                lexema_reade += lexema[indice]
                indice += 1
                large += 1
            elif large != 0 and lexema[indice] == '"':
                caracter = lexema[indice]
                estado = f'{lista_estados[1]}'
                transicion = f'{lista_estados[2]}'
                estadoString.append(
                    [estado, caracter, lexema_reade, transicion])
                lexema_reade += lexema[indice]
                indice += 1
                large += 1

        if indice == len(lexema):
            estadoString.append(
                [estado, '#', lexema, f'{transicion} -> (aceptacion)'])

        return estadoString

    def EstadosChar(self, lexema) -> list:
        lista_estados = ['S0', 'S1', 'S2']
        indice = 0
        large = 0
        lexema_reade = ''
        estado = ''
        estadoString = list()
        while indice < len(lexema):
            if large == 0 and lexema[indice] == "'":
                caracter = lexema[indice]
                estado = f'{lista_estados[0]}'
                transicion = f'{lista_estados[1]}'
                estadoString.append(
                    [estado, caracter, lexema_reade, transicion])
                lexema_reade += lexema[indice]
                indice += 1
                large += 1
            elif large != 0 and lexema[indice] != "'":
                caracter = lexema[indice]
                estado = f'{lista_estados[1]}'
                transicion = f'{lista_estados[1]}'
                estadoString.append(
                    [estado, caracter, lexema_reade, transicion])
                lexema_reade += lexema[indice]
                indice += 1
                large += 1
            elif large != 0 and lexema[indice] == "'":
                caracter = lexema[indice]
                estado = f'{lista_estados[1]}'
                transicion = f'{lista_estados[2]}'
                estadoString.append(
                    [estado, caracter, lexema_reade, transicion])
                lexema_reade += lexema[indice]
                indice += 1
                large += 1

        if indice == len(lexema):
            estadoString.append(
                [estado, '#', lexema, f'{transicion} -> (aceptacion)'])

        return estadoString
