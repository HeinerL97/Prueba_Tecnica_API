# Prueba_Tecnica_API
Prueba tecnica de consumo de API
# Rick and Morty Character Checker

Este proyecto consume la API pública de Rick and Morty para obtener información de un conjunto de personajes principales. Evalúa su estado (vivo, muerto o desconocido), valida tipos de datos y presenta los resultados en una tabla clara y legible en consola.

---

## Descripción del Proyecto

Consume la siguiente API:

[[https://rickandmortyapi.com/api/character](https://rickandmortyapi.com/api/character)](https://rickandmortyapi.com/api)

Realiza scripts en el lenguaje de programación que domines (en este caso, **Python**) para consumir a los **personajes principales** y obtener los personajes **vivos** de esta serie.

---

## Resultados Esperados

Este script cumple con los siguientes objetivos:

- **Indicar el tiempo de respuesta** de la API.
- **Mostrar el código de estado (status code)** de la respuesta.
- **Validar y clasificar** personajes vivos, muertos y desconocidos.
- **Validar tipos de datos** (`id`, `name`, `status`) en el JSON de respuesta.

---

## Requisitos

Este script requiere Python 3.7+ y las siguientes librerías:

```bash
pip install requests tabulate
