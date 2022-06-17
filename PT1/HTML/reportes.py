from os import startfile


class HTML():

    def createHTML(self, name_html, lista):
        file = open('PT1/HTML/tabla_tokens/table-07/{}.html'.format(name_html),
                    'w+', encoding='utf-8')

        body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link href='https://fonts.googleapis.com/css?family=Roboto:400,100,300,700' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" href="css/style.css">
    <title>{name_html}</title>
</head>"""

        body = body + f"""
<body>
        """

        body = body + f"""
    <section class="ftco-section">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-6 text-center mb-5">
                    <h1 class="heading-section">Tablas</h1>
                </div>
            </div>
        """
        if lista['tokens']:
            body = body + f"""
            <h2 class="heading-section">Tablas de Tokens</h2>
            <div class = "row" >
                <div class = "col-md-12" > 
                    <div class = "table-wrap" >
                        <table class="table table-bordered table-dark table-hover">
                            <thead>
                            <tr>
                                <th> Identificador </th>
                                <th> Token </th>
                                <th> Descripcion </th>
                                <th> Fila </th>
                                <th> Columna </th>
                                <th> Patron </th>
                            </tr>
                            </thead>
        """
            body = body + f"""
                            <tbody>
        """

        # ? Contenido BODY HTML

            tokens = lista['tokens']
            for elemento in tokens:
                id = elemento.id
                lex = elemento.valor
                descripcion = lex.descripcion
                valor = lex.valor
                fila = lex.fila
                columna = lex.col
                patron = lex.patron
                body = body + f"""  
                                <tr >
                                    <th scope="row">{id}</th>
                                    <td>{valor}</td>
                                    <td>{descripcion}</td>
                                    <td>{fila}</td>
                                    <td>{columna}</td>
                                    <td>{patron}</td>
                                </tr>"""

            body = body + f"""
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>"""

        body = body + f"""
            <br>
            <br>"""

        if lista['estados']:
            body = body + f"""
            <h2 class="heading-section">Tablas de Estados</h2>
            """
            estados = lista['estados']
            for elemento in estados:
                body = body + f"""
            <h2 class="heading-section">Lexema: {elemento.lexema} Token:{elemento.nombre} </h2>
            <div class = "row" >
                <div class = "col-md-12" > 
                    <div class = "table-wrap" >
                        <table class="table table-bordered table-dark table-hover">
                            <thead>
                            <tr>
                                <th> Estado </th>
                                <th> Caracter </th>
                                <th> Lexema Reconocido </th>
                                <th> Siguiente Estado </th>
                            </tr>
                            </thead>
            """
                body = body + f"""
                            <tbody>
            """
            # ? Contenido BODY HTML
                for datos in elemento.estados:
                    body = body + f"""
                                <tr >"""
                    for dato in datos:
                        body = body + f"""  
                                    <td>{dato}</td>
                                    """
                    body = body + f"""
                                </tr >"""

                body = body + f"""
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>"""

                body = body + f"""
            <br>
            <br>"""

        if lista['errores']:
            body = body + f"""
            <h2 class="heading-section">Tablas de Errores</h2>
            <div class = "row" >
                <div class = "col-md-12" > 
                    <div class = "table-wrap" >
                        <table class="table table-bordered table-dark table-hover">
                            <thead>
                            <tr>
                                <th> Identificador </th>
                                <th> Fila </th>
                                <th> Columna </th>
                            </tr>
                            </thead>
        """
            body = body + f"""
                            <tbody>
        """

        # ? Contenido BODY HTML

            errores = lista['errores']
            for elemento in errores:
                id = elemento.caracter
                fila = elemento.fila
                columna = elemento.col
                body = body + f"""  
                                <tr >
                                    <th scope="row">{id}</th>
                                    <td>{fila}</td>
                                    <td>{columna}</td>
                                </tr>"""

            body = body + f"""
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>"""

        body = body + f"""
            <br>
            <br>"""

        body = body + f"""
        </div>
    </section>
        """

        body = body + f"""
    <script src="js/jquery.min.js"></script>
    <script src="js/popper.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
</body>
        """

        body = body + f"""
</html>"""

        file.write(body)
        file.close()

        index = 'PT1\\HTML\\tabla_tokens\\table-07\\{}.html'.format(
            name_html)
        startfile(index)
