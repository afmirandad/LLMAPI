# API de Inventario de Activos

Esta API permite la gestión, consulta y administración de activos de información de una organización. Está desarrollada en FastAPI, expone endpoints RESTful y utiliza una base de datos MySQL. Es ideal para prácticas y proyectos de estudiantes de ingeniería de sistemas o afines.

## Características principales
- CRUD completo sobre activos de información
- Búsqueda avanzada por cualquier campo
- Documentación interactiva con Swagger (en español)
- Manejo de errores y logs
- Listo para despliegue en Docker

## Requisitos
- Docker (opcional, recomendado para despliegue)
- Python 3.12 (si se ejecuta localmente)
- Acceso a una base de datos MySQL (ver variable `DATABASE_URL` en `.env`)

## Instalación y despliegue

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd LLMAPI
```

### 2. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (ajusta los valores según tu base de datos):

```
DATABASE_URL=mysql+pymysql://usuario:contraseña@host:puerto/nombre_db
```

### 3. Construir y ejecutar con Docker
```bash
docker build -t inventario-api .
docker run -d -p 8000:8000 --env-file .env inventario-api
```

### 4. Acceso a la documentación
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Endpoints principales

### Listar activos
- **GET** `/inventario/`
- **Descripción:** Devuelve una lista paginada de activos.
- **Parámetros opcionales:** `skip` (int), `limit` (int)
- **Respuesta:**
```json
[
  {
    "id": 1,
    "NOMBRE_DEL_ACTIVO": "...",
    "DESCRIPCION": "...",
    ...
  },
  ...
]
```

### Obtener activo por ID
- **GET** `/inventario/{id}`
- **Descripción:** Devuelve un activo específico por su ID.
- **Respuesta:**
```json
{
  "id": 1,
  "NOMBRE_DEL_ACTIVO": "...",
  "DESCRIPCION": "...",
  ...
}
```

### Crear un activo
- **POST** `/inventario/`
- **Descripción:** Crea un nuevo activo.
- **Body (JSON):**
```json
{
  "NOMBRE_DEL_ACTIVO": "...",
  "DESCRIPCION": "...",
  ...
}
```
- **Respuesta:** Activo creado (incluye su `id`).

### Actualizar un activo
- **PUT** `/inventario/{id}`
- **Descripción:** Actualiza los datos de un activo existente.
- **Body (JSON):** Igual que en creación.
- **Respuesta:** Activo actualizado.

### Eliminar un activo
- **DELETE** `/inventario/{id}`
- **Descripción:** Elimina un activo por su ID.
- **Respuesta:** Activo eliminado.

### Búsqueda avanzada
- **GET** `/inventario/buscar/`
- **Descripción:** Permite buscar activos por cualquier campo (parámetros opcionales en la URL).
- **Ejemplo:**
```
/inventario/buscar/?NOMBRE_DEL_ACTIVO=plan&IDIOMA=Español
```
- **Respuesta:** Lista de activos que cumplen los filtros.

## Estructura de datos (modelo)
Cada activo tiene los siguientes campos:
- `id`: int (autoincremental)
- `NOMBRE_DEL_ACTIVO`: string
- `DESCRIPCION`: string
- `TIPO_DE_ACTIVO`: string
- `MEDIO_DE_CONSERVACIÓN`: string
- `FORMATO`: string
- `IDIOMA`: string
- `PROCESO`: string
- `DUEÑO_DE_ACTIVO`: string
- `TIPO_DE_DATOS_PERSONALES`: string
- `FINALIDAD_DE_LA_RECOLECCIÓN`: string
- `CONFIDENCIALIDAD`: string
- `INTEGRIDAD`: string
- `DISPONIBILIDAD`: string
- `CRITICIDAD_TOTAL_DEL_ACTIVO`: string
- `INFORMACIÓN_PUBLICADA_O_DISPONIBLE`: string
- `LUGAR_DE_CONSULTA`: string

## Ejemplo de uso con curl

**Crear un activo:**
```bash
curl -X POST "http://localhost:8000/inventario/" -H "Content-Type: application/json" -d '{
  "NOMBRE_DEL_ACTIVO": "Servidor Web",
  "DESCRIPCION": "Servidor de aplicaciones web",
  "TIPO_DE_ACTIVO": "Hardware",
  "IDIOMA": "Español"
}'
```

**Buscar activos:**
```bash
curl "http://localhost:8000/inventario/buscar/?IDIOMA=Español"
```

## Manejo de errores
- Todos los endpoints retornan errores HTTP estándar (404, 500, etc.) con mensajes claros.
- Los errores se registran en consola para facilitar el diagnóstico.

## Notas para estudiantes
- Puedes consumir la API desde cualquier lenguaje que soporte HTTP (Python, JavaScript, Java, etc.).
- Usa la documentación Swagger para probar y entender los endpoints.
- El modelo es flexible y puedes extenderlo según tus necesidades.

---

¿Dudas o sugerencias? Abre un issue en el repositorio.
