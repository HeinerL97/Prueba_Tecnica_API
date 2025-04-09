
#Importacion de librerias
import requests
import time
from tabulate import tabulate

# Lista de IDs de personajes principales de la serie Rick and Morty
personajes_principales = [1, 2, 3, 4, 5, 47, 103, 191, 216, 278, 726, 849, 801, 821, 812]

# Convertir el estado de los personajes del inglés al español
estado_personaje = {
    "Alive": "Vivo",
    "Dead": "Muerto",
    "unknown": "Desconocido"
}

# Diccionario con los campos que se espera validar y su tipo de dato correspondiente
tipos_esperados = {
    "id": int,
    "name": str,
    "status": str,
}

# Medición del tiempo de respuesta de la API
start = time.time()
response = requests.get(f"https://rickandmortyapi.com/api/character/{','.join(map(str, personajes_principales))}")
end = time.time()

# Se redondea el tiempo de respuesta a 9 decimales
tiempo_respuesta = round(end - start, 9)
status_code = response.status_code

# Impresión de tiempo de respuesta y código de estado HTTP
print(f"\nTiempo de respuesta: {tiempo_respuesta} segundos")
print(f"Código de estado: {status_code}\n")

# Validación de respuesta exitosa
if response.status_code == 200:
    data = response.json()

    # Si la respuesta no es una lista (cuando solo se consulta un personaje), se convierte a lista
    if not isinstance(data, list):
        data = [data]

    # Contadores para los estados de los personajes
    vivos, muertos, desconocidos = 0, 0, 0

    # Lista para almacenar filas de la tabla que se imprimir
    tabla = []

    # Recorrido de cada personaje recibido
    for personaje in data:
        # Primeros datos de cada fila: nombre y estado convertido
        fila = [
            f" {personaje['name']} (ID: {personaje['id']})",
            estado_personaje.get(personaje["status"])
        ]

        # Validación de tipo de dato por campo
        for campo, tipo_esperado in tipos_esperados.items():
            valor = personaje.get(campo)
            tipo_real = type(valor)
            valido = isinstance(valor, tipo_esperado)
            estado = "valido" if valido else "invalido"
            fila.append(f"{estado} ({tipo_real.__name__})")

        # Clasificación del personaje por estado
        if personaje["status"] == "Alive":
            vivos += 1
        elif personaje["status"] == "Dead":
            muertos += 1
        else:
            desconocidos += 1

        # Agrega la fila a la tabla final
        tabla.append(fila)

    # Encabezado de la tabla para impresión
    encabezado = [" Personaje", " Estado"] + [f"{campo} " for campo in tipos_esperados.keys()]

    # Impresión en formato tabla el resultado
    print(tabulate(tabla, headers=encabezado, tablefmt="fancy_grid"))

    # Resumen de resultados
    print(f"Total personajes: {len(data)}")
    print(f"Vivos: {vivos}")
    print(f"Muertos: {muertos}")
    print(f"Desconocidos: {desconocidos}")

else:
    # Mensaje de error si la respuesta no fue exitosa
    print("Error al consultar al API.")