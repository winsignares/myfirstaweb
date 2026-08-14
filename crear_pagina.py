html = """
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cinthia Rivera</title>
</head>

<body>

    <h1>Hola, soy Cinthia Rivera</h1>

    <h2>Estudiante de Ingeniería de Sistemas</h2>

    <p>
        Soy estudiante de Ingeniería de Sistemas en la Universidad Libre
        y estoy aprendiendo desarrollo web y programación.
    </p>

    <h2>Sobre mí</h2>

    <p>
        Me interesa la tecnología, el desarrollo de software y el análisis
        de datos. Estoy aprendiendo nuevas herramientas para fortalecer
        mis conocimientos como futura ingeniera de sistemas.
    </p>

</body>

</html>
"""

with open("Cinthia_Rivera.html", "w", encoding="utf-8") as archivo:
    archivo.write(html)

print("Página creada correctamente.")