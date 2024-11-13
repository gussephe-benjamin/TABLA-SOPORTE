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
