def ingresar_respuestas(evaluacion,numero_de_preguntas):
    archivo = open(evaluacion+".csv","w")

    iniciar = input("Añadir alumnos?(S/N) -> ")
    while iniciar.lower()=="s": 
        nombres = input("Nombres: ")
        apellidos = input("Apellidos")
        rut = input("RUT: ")
        datos=nombres+","+apellidos+","+rut
        for i in range(0, numero_de_preguntas):
            respuesta = input(str(i+1)+". -> ")
            datos=datos+","+respuesta
        datos = datos+"\n"
        archivo.write(datos)
        iniciar = input("Ingresar otro alumno?(S/N) -> ")
    archivo.close

evaluacion = input("Qué evaluación es esta? -> ")
numero_de_preguntas = int(input("Número de preguntas: "))

respuesta = input("Deseas comenzar a ingresar las respuestas?(S/N) -> ")
if respuesta.lower()=="s":
    ingresar_respuestas(evaluacion,numero_de_preguntas)
