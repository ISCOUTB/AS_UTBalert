# AS_UTBalert
Sistema de alertas tempranas para la Universidad Tecnológica de Bolívar.

## Integrantes
- Brayan Maluenga (T00061692)
- Juan David Hernandez (T00081559)
- Zulianys Orozco (T00078330)
- Tatiana Marrugo (T00080393)
- Valery Aurela (T00078728)

## Descripción
El proyecto consiste en desarrollar un sistema de alertas tempranas con base en un análisis
de las variables institucionales que permita identificar a estudiantes con riesgo académico o
con riesgo de deserción en el marco de una institución de educación superior.

## Tecnologías
- Python 3.x (backend)
- FastAPI / Flask / Django (según se implemente)
- PostgreSQL / SQLite (base de datos)

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/<usuario>/AS_UTBalert.git
   cd AS_UTBalert
   ```
2. Crear y activar un entorno virtual (recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. Instalar dependencias (ajustar según el archivo de requerimientos):
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Configurar las variables de entorno / base de datos según `database/script.sql`.
2. Ejecutar el backend:
   ```bash
   python src/backed/main.py
   ```

## Estructura del proyecto
- `database/` - Contiene scripts SQL de inicialización.
- `src/backed/` - Código del backend.
- `src/frontend/` - Código del frontend (si aplica).

## Contribuir
1. Crear una rama con nombre descriptivo.
2. Hacer commits pequeños y claros.
3. Abrir un Pull Request para revisión.

## Licencia
Este proyecto está bajo la licencia que decida el equipo (por ejemplo, MIT)."}