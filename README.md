# Tarea Semana 16: Aplicación GUI - Lista de Tareas con Atajos de Teclado (Mejora del Sistema Semana 15)

**Autor:** ANDREW DAVID VALENZUELA YELA

## Objetivo

Desarrollar una nueva versión del sistema trabajado en la Semana 15, partiendo de la aplicación de lista de tareas previamente implementada, incorporando mejoras en la interacción mediante el uso de atajos de teclado. El estudiante deberá mantener estrictamente la arquitectura modular por capas, evidenciando una evolución del sistema sin alterar la separación de responsabilidades.

Aplicación de escritorio desarrollada en Python con Tkinter para la gestión de tareas (To-Do List). Implementa operaciones CRUD en memoria, manejo de eventos de usuario (teclado y ratón), sigue una arquitectura modular por capas y permite generar un ejecutable utilizando PyInstaller.

## Características

- ✅ **Interfaz Gráfica Moderna**: Diseño minimalista con colores pastel para una experiencia visual agradable.
- ✅ **Atajos de Teclado**: 
  - `Enter`: Agregar nueva tarea
  - `C`: Marcar tarea como completada
  - `D` o `Delete`: Eliminar tarea seleccionada
  - `Escape`: Cerrar aplicación
- ✅ **Feedback Visual**: Tareas completadas se muestran en verde pastel.
- ✅ **Barra de Estado**: Muestra estadísticas en tiempo real (Total, Pendientes, Completadas).
- ✅ **Arquitectura Modular**: Separación clara entre modelos, servicios y UI.
- ✅ **Operaciones CRUD**: Crear, leer, actualizar y eliminar tareas en memoria.

## Estructura del Proyecto

```
lista_tareas_app/
│
├── main.py                    # Punto de entrada del sistema
├── modelos/
│   └── tarea.py               # Modelo de datos para las tareas
├── servicios/
│   └── tarea_servicio.py      # Lógica de negocio y operaciones CRUD
└── ui/
    └── app_tkinter.py         # Interfaz gráfica con Tkinter
```

## Requisitos

- Python 3.6+
- Tkinter (incluido en la instalación estándar de Python)

## Instalación y Ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/davidesya-design/Aplicaci-n-GUI-Lista-de-Tareas-con-Atajos-de-Teclado-Mejora-del-Sistema-Semana-15-.git
   cd lista_tareas_app
   ```

2. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

## Generar Ejecutable

Para crear un ejecutable independiente usando PyInstaller:

1. Instala PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Genera el ejecutable:
   ```bash
   pyinstaller --onefile --windowed main.py
   ```

3. El ejecutable se encontrará en la carpeta `dist/`.

## Uso

- **Agregar tarea**: Escribe en el campo de entrada y presiona Enter o haz clic en "Agregar Tarea".
- **Completar tarea**: Selecciona una tarea y presiona C o haz clic en "Marcar Completada".
- **Eliminar tarea**: Selecciona una tarea y presiona D/Delete o haz clic en "Eliminar Tarea".
- **Cerrar aplicación**: Presiona Escape.

## Arquitectura

El sistema sigue una arquitectura modular por capas:

- **Capa de Modelo** (`modelos/`): Define la estructura de datos (Tarea).
- **Capa de Servicio** (`servicios/`): Contiene la lógica de negocio y operaciones CRUD.
- **Capa de Presentación** (`ui/`): Maneja la interfaz gráfica y eventos de usuario.
- **Capa de Inicio** (`main.py`): Punto de entrada que inicializa la aplicación.

## Mejoras sobre Semana 15

- Interfaz modernizada con diseño minimalista y colores pastel.
- Implementación de atajos de teclado para mejorar la usabilidad.
- Barra de estado con estadísticas en tiempo real.
- Mejor feedback visual sin alterar la arquitectura existente.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Tkinter**: Biblioteca para la interfaz gráfica.
- **PyInstaller**: Para generar ejecutables (opcional).

## Licencia

Este proyecto es para fines educativos como parte del curso de desarrollo de software.</content>
<parameter name="filePath">c:\Users\tralk\Desktop\SIO\lista_tareas_app\README.md