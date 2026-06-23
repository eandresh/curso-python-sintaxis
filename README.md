# Calculadora de Promedios Escolares (Python)

Este programa es una herramienta interactiva diseñada en Python que permite gestionar materias y calificaciones de estudiantes de forma estructurada (sin programación orientada a objetos).

## Requisitos

*   **Python 3.6** o superior instalado en el sistema.

## Instrucciones de Ejecución

Para iniciar el programa en tu terminal, sigue estos pasos:

1.  Abre la terminal en la carpeta raíz del proyecto.
2.  Ejecuta el siguiente comando:
    ```bash
    python3 calculadora_promedios.py
    ```

---

## Funcionalidades y Flujo del Programa

El programa guía al usuario a través de los siguientes pasos:

1.  **Registro de Materias y Calificaciones**: El usuario ingresa el nombre de la materia y su respectiva calificación.
    *   *Validación integrada*: La calificación debe ser un valor numérico entre `0.0` y `10.0`. En caso de ingresar datos no válidos, el programa muestra un mensaje de error y solicita el ingreso nuevamente.
    *   *Control de finalización*: El usuario puede presionar `Enter` en el nombre de la materia o responder `n` a la pregunta de continuar para finalizar la captura de datos.
2.  **Cálculo del Promedio**: Calcula el promedio general aritmético de todas las materias ingresadas.
3.  **Estado de Materias**: Clasifica las materias en *Aprobadas* y *Reprobadas* basándose en un umbral configurable (por defecto `5.0`).
4.  **Extremos**: Identifica las materias que obtuvieron la calificación más alta y la más baja.
5.  **Resumen Final**: Muestra un reporte estructurado y limpio con toda la información calculada.
6.  **Manejo de Casos Especiales**: Si no se ingresa ninguna materia, el programa finaliza ordenadamente con un mensaje descriptivo.

---

## Estructura del Código

El código está organizado exclusivamente bajo el paradigma de programación estructurada, utilizando las siguientes funciones:

*   `ingresar_calificaciones()`: Captura de datos de materias y calificaciones con validaciones de entrada. Retorna dos listas separadas.
*   `calcular_promedio(calificaciones)`: Retorna la media aritmética de las calificaciones de la lista.
*   `determinar_estado(calificaciones, umbral=5.0)`: Clasifica e identifica los índices de materias aprobadas y reprobadas.
*   `encontrar_extremos(calificaciones)`: Identifica los índices del valor máximo y mínimo en la lista.
*   `main()`: Coordina el flujo principal y la impresión del resumen del programa.
