# TABLA-SOPORTE
Aquí tienes los JSON de ejemplo para cada operación que puedes utilizar en Postman. Estos JSON corresponden a las funcionalidades de la tabla de soporte.

---

### 1. **Crear Solicitud** (POST `/soporte/crear`)

**Request JSON:**
```json
{
  "usuario_id": "user123",
  "Titulo": "Problema con la cuenta",
  "descripcion": "No puedo acceder a mi cuenta desde ayer."
}
```

**Expected Response JSON:**
```json
{
  "usuario_id": "user123",
  "ticket_id": "uuid-ticket-id",
  "Titulo": "Problema con la cuenta",
  "descripcion": "No puedo acceder a mi cuenta desde ayer.",
  "estado": "pendiente",
  "fecha": "2024-11-13T12:00:00Z"
}
```

---

### 2. **Eliminar Solicitud** (DELETE `/soporte/eliminar`)

**Request JSON:**
```json
{
  "usuario_id": "user123",
  "ticket_id": "uuid-ticket-id"
}
```

**Expected Response JSON:**
```json
{
  "message": "Solicitud uuid-ticket-id del usuario user123 se eliminó correctamente"
}
```

---

### 3. **Editar Solicitud** (PUT `/soporte/editar`)

**Request JSON:**
```json
{
  "usuario_id": "user123",
  "ticket_id": "uuid-ticket-id",
  "Titulo": "Actualización del problema",
  "descripcion": "He intentado varias veces acceder, sigue sin funcionar."
}
```

**Expected Response JSON:**
```json
{
  "momento": "actual modificado",
  "usuario_id": "user123",
  "ticket_id": "uuid-ticket-id",
  "Titulo": "Actualización del problema",
  "descripcion": "He intentado varias veces acceder, sigue sin funcionar.",
  "estado": "pendiente"
}
```

---

### 4. **Obtener Solicitud por ID** (POST `/soporte/obtener`)

**Request JSON:**
```json
{
  "usuario_id": "user123",
  "ticket_id": "uuid-ticket-id"
}
```

**Expected Response JSON:**
```json
{
  "usuario_id": "user123",
  "ticket_id": "uuid-ticket-id",
  "Titulo": "Problema con la cuenta",
  "descripcion": "No puedo acceder a mi cuenta desde ayer.",
  "estado": "pendiente",
  "fecha": "2024-11-13T12:00:00Z"
}
```

---

### 5. **Listar Todas las Solicitudes** (GET `/soporte/listar`)

**Request JSON:** (No request body needed)

**Expected Response JSON:**
```json
[
  {
    "usuario_id": "user123",
    "ticket_id": "uuid-ticket-1",
    "Titulo": "Problema con la cuenta",
    "descripcion": "No puedo acceder a mi cuenta desde ayer.",
    "estado": "pendiente",
    "fecha": "2024-11-13T12:00:00Z"
  },
  {
    "usuario_id": "user456",
    "ticket_id": "uuid-ticket-2",
    "Titulo": "Consulta sobre transacciones",
    "descripcion": "Necesito ayuda con una transacción reciente.",
    "estado": "pendiente",
    "fecha": "2024-11-13T12:10:00Z"
  }
]
```

---

### 6. **Listar Solicitudes por Usuario** (POST `/soporte/listar-usuario`)

**Request JSON:**
```json
{
  "usuario_id": "user123"
}
```

**Expected Response JSON:**
```json
[
  {
    "usuario_id": "user123",
    "ticket_id": "uuid-ticket-1",
    "Titulo": "Problema con la cuenta",
    "descripcion": "No puedo acceder a mi cuenta desde ayer.",
    "estado": "pendiente",
    "fecha": "2024-11-13T12:00:00Z"
  },
  {
    "usuario_id": "user123",
    "ticket_id": "uuid-ticket-2",
    "Titulo": "Problema con pagos",
    "descripcion": "No se ha procesado un pago reciente.",
    "estado": "pendiente",
    "fecha": "2024-11-13T13:00:00Z"
  }
]
```

---

### 7. **Responder Solicitud** (POST `/soporte/responder`)

**Request JSON:**
```json
{
  "usuario_id": "user123",
  "ticket_id": "uuid-ticket-id",
  "response": "Hemos revisado el problema y hemos solucionado el acceso."
}
```

**Expected Response JSON:**
```json
{
  "usuario_id": "user123",
  "ticket_id": "uuid-ticket-id",
  "response": "Hemos revisado el problema y hemos solucionado el acceso.",
  "estado": "respondido",
  "fecha_respuesta": "2024-11-13T14:00:00Z"
}
```

---

Estos ejemplos te permitirán realizar las pruebas en Postman para cada una de las funcionalidades de la tabla de soporte en AWS DynamoDB a través de tus funciones Lambda. Cada caso cubre un escenario específico de manejo de solicitudes de soporte, con distintos estados y actualizaciones de datos.

**Informe de la Tabla Soporte**

### Introducción
La **Tabla Soporte** en DynamoDB ha sido diseñada para gestionar solicitudes de soporte o consultas enviadas por los usuarios de un sistema. La funcionalidad de esta tabla incluye la capacidad para que los usuarios creen, editen y consulten sus solicitudes, así como para que los administradores respondan a estas solicitudes. La tabla permite una comunicación estructurada entre usuarios y administradores, y establece un flujo de estado para gestionar las respuestas.

### Estructura de la Tabla

#### Claves Primarias
- **usuario_id** (Partition Key): Identifica de manera única al usuario que realiza la solicitud de soporte.
- **ticket_id** (Sort Key): Identificador único de la solicitud, generado automáticamente usando `uuid.v4()` para asegurar que cada solicitud tiene un ID distinto.

#### Atributos Principales
- **Titulo**: Describe brevemente el problema o consulta que el usuario tiene.
- **descripcion**: Proporciona detalles adicionales sobre la solicitud.
- **estado**: Indica el estado de la solicitud, con dos valores posibles:
  - `"pendiente"`: La solicitud aún no ha sido respondida.
  - `"respondido"`: La solicitud ha sido respondida y no puede ser modificada por el usuario.
- **fecha**: Fecha y hora en la que se crea o modifica la solicitud.
- **respuesta** (opcional): Mensaje de respuesta proporcionado por el administrador. Solo se agrega cuando la solicitud es respondida.

### Índices

#### Índice Global Secundario (GSI) - EstadoIndex
- **estado** (Partition Key): Permite realizar consultas por estado de la solicitud (`pendiente` o `respondido`).
- **fecha** (Sort Key): Facilita el ordenamiento de las solicitudes por fecha dentro de cada estado.

### Funciones Lambda Asociadas a la Tabla Soporte

1. **CrearSolicitud**
   - Crea una nueva solicitud en estado `"pendiente"`.
   - Genera un `ticket_id` único para cada solicitud.
   - Guarda el `usuario_id`, `titulo`, `descripcion`, `estado`, y `fecha` de creación en la tabla.

2. **EditarSolicitud**
   - Permite editar el `titulo` y la `descripcion` de una solicitud, siempre que su estado sea `"pendiente"`.
   - Si la solicitud ya está en estado `"respondido"`, no permite la modificación y retorna un mensaje de error con los detalles originales de la solicitud.
   - Registra la fecha de la última modificación en el campo `fecha`.

3. **EliminarSolicitud**
   - Permite eliminar una solicitud de soporte específica, identificada por el `usuario_id` y `ticket_id`.
   - Esta acción es irreversible y se usa generalmente para eliminar solicitudes duplicadas o irrelevantes.

4. **ObtenerSolicitud**
   - Obtiene los detalles completos de una solicitud específica, identificada por el `usuario_id` y `ticket_id`.
   - Si la solicitud no existe, devuelve un mensaje de error indicando que no fue encontrada.

5. **ListarSolicitudes**
   - Lista todas las solicitudes en la tabla, sin ningún filtro.
   - Útil para los administradores que desean ver todas las solicitudes de soporte en el sistema.

6. **ListarSolicitudesPorUsuario**
   - Lista todas las solicitudes de un usuario específico, identificado por su `usuario_id`.
   - Permite al usuario ver el historial de sus solicitudes de soporte.

7. **ResponderSolicitud**
   - Permite al administrador responder a una solicitud específica.
   - Agrega la respuesta en el campo `respuesta`, cambia el `estado` a `"respondido"`, y registra la `fecha_respuesta`.
   - Si la solicitud ya ha sido respondida, devuelve un mensaje de error indicando que no puede ser modificada.

### Relación con Otras Tablas y Funcionalidades

La **Tabla Soporte** está diseñada principalmente para la interacción entre usuarios y administradores, y no tiene dependencias directas con otras tablas. Sin embargo, puede formar parte de un sistema de soporte integral en conjunto con otras tablas que gestionen diferentes módulos de servicio al cliente o seguimiento de casos.

### Ventajas de Esta Implementación

- **Gestión de Estados**: La columna `estado` permite controlar si la solicitud está pendiente o respondida, evitando ediciones no autorizadas una vez que ha sido atendida.
- **Historial de Modificaciones**: Cada modificación de una solicitud en estado pendiente actualiza el campo `fecha`, proporcionando un registro temporal de las ediciones.
- **Acceso Rápido a Solicitudes**: Gracias al índice secundario `EstadoIndex`, los administradores pueden filtrar rápidamente las solicitudes en estado pendiente para priorizar las que aún requieren atención.
  
### Uso en Casos Prácticos

- **Usuario Regular**: Puede crear una solicitud para problemas técnicos o consultas, editar la solicitud si no ha sido respondida, y ver el estado de todas sus solicitudes.
- **Administrador**: Puede ver todas las solicitudes, responder a las pendientes y administrar el soporte al cliente con facilidad.

### Conclusión
La **Tabla Soporte** es un componente clave en el sistema de soporte al cliente, proporcionando un mecanismo organizado y eficiente para la comunicación entre usuarios y administradores. La implementación de esta tabla facilita la gestión de consultas y problemas, asegurando que las solicitudes sean tratadas de manera consistente y oportuna.


