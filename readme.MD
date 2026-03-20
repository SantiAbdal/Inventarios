# Inventory API

API REST desarrollada con **FastAPI** para gestionar productos, categorías e inventario con historial de movimientos de stock. Incluye autenticación mediante JWT para proteger los endpoints de escritura.

---

## Tecnologías utilizadas

- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic V2
- Uvicorn
- Pytest
- python-jose
- passlib

---

## Arquitectura del proyecto

El proyecto sigue una arquitectura en capas:

Router → Service → Repository → Database

- **Router**: define los endpoints de la API
- **Service**: contiene la lógica de negocio y validaciones
- **Repository**: se encarga de interactuar con la base de datos
- **Models**: representan las tablas de la base de datos
- **Schemas**: validan los datos de entrada y salida

---

## Estructura del proyecto

    project/
    │
    ├── core/
    │   └── security.py
    │
    ├── db/
    │   ├── db.py
    │   └── dependencies.py
    │
    ├── models/
    │   ├── product_model.py
    │   ├── category_model.py
    │   ├── stock_movement_model.py
    │   └── user_model.py
    │
    ├── schemas/
    │   ├── product_schema.py
    │   ├── product_condition_schema.py
    │   ├── category_schema.py
    │   ├── movement_type_schema.py
    │   ├── stock_movement_schema.py
    │   ├── user_schema.py
    │   └── user_state_schema.py
    │
    ├── repository/
    │   ├── product_repository.py
    │   ├── category_repository.py
    │   ├── stock_movement_repository.py
    │   └── user_repository.py
    │
    ├── services/
    │   ├── product_services.py
    │   ├── category_services.py
    │   └── auth_service.py
    │
    ├── routers/
    │   ├── product_router.py
    │   ├── category_router.py
    │   ├── stock_movement_router.py
    │   └── auth_router.py
    │
    ├── tests/
    │   ├── conftest.py
    │   ├── test_products.py
    │   └── test_categories.py
    │
    ├── pytest.ini
    └── main.py

---

## Instalación

Clonar el repositorio:

    git clone https://github.com/SantiAbdal/Inventarios.git
    cd Inventarios

Crear y activar entorno virtual:

    python -m venv venv

    # Windows
    venv\Scripts\activate

    # Linux / Mac
    source venv/bin/activate

Instalar dependencias:

    pip install -r requirements.txt

---

## Ejecutar la API

    uvicorn main:app --reload

Disponible en `http://127.0.0.1:8000`

---

## Documentación automática

FastAPI genera documentación interactiva automáticamente:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## Autenticación

La API utiliza autenticación basada en JWT. Los endpoints de lectura son públicos, mientras que los de escritura (POST, PUT, DELETE) requieren un token válido.

**1. Registrar un usuario:**

    curl -X POST "http://127.0.0.1:8000/auth/register" \
    -H "Content-Type: application/json" \
    -d '{
      "user_name": "santiago",
      "email": "santiago@test.com",
      "password": "123456",
      "state": "ACTIVE"
    }'

**2. Obtener el token:**

    curl -X POST "http://127.0.0.1:8000/auth/login" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "username=santiago&password=123456"

La respuesta incluye el `access_token` que se debe enviar en el header de cada request protegida:

    Authorization: Bearer <access_token>

---

## Endpoints

### Autenticación

| Método | Endpoint | Descripción | Requiere token |
|--------|----------|-------------|----------------|
| POST | /auth/register | Registrar usuario | No |
| POST | /auth/login | Iniciar sesión y obtener token | No |

### Productos

| Método | Endpoint | Descripción | Requiere token |
|--------|----------|-------------|----------------|
| GET | /products | Listar todos los productos | No |
| GET | /products/{id} | Obtener producto por ID | No |
| POST | /products | Crear producto | Sí |
| PUT | /products/{id} | Actualizar producto | Sí |
| DELETE | /products/{id} | Eliminar producto | Sí |
| GET | /products/low-stock | Productos con stock bajo | No |
| GET | /products/search/text | Buscar por nombre, marca o SKU | No |
| GET | /products/search/equal | Buscar por categoría o condición | No |
| GET | /products/search/range | Buscar por rango de precio, costo o fecha | No |
| GET | /products/search/category | Buscar por nombre de categoría | No |

### Categorías

| Método | Endpoint | Descripción | Requiere token |
|--------|----------|-------------|----------------|
| GET | /categories | Listar todas las categorías | No |
| GET | /categories/{id} | Obtener categoría por ID | No |
| POST | /categories | Crear categoría | Sí |
| DELETE | /categories/{id} | Eliminar categoría | Sí |

### Stock

| Método | Endpoint | Descripción | Requiere token |
|--------|----------|-------------|----------------|
| POST | /stock/in/{sku} | Registrar entrada de stock | Sí |
| POST | /stock/out/{sku} | Registrar salida de stock | Sí |
| GET | /stock/history/{sku} | Ver historial de movimientos | No |

---

## Ejemplos de uso

**Registrar un usuario:**

    curl -X POST "http://127.0.0.1:8000/auth/register" \
    -H "Content-Type: application/json" \
    -d '{"user_name": "santiago", "email": "santiago@test.com", "password": "123456", "state": "ACTIVE"}'

**Obtener token:**

    curl -X POST "http://127.0.0.1:8000/auth/login" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "username=santiago&password=123456"

**Crear una categoría (con token):**

    curl -X POST "http://127.0.0.1:8000/categories/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <token>" \
    -d '{"name": "Electrónica"}'

**Crear un producto (con token):**

    curl -X POST "http://127.0.0.1:8000/products" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <token>" \
    -d '{
      "name": "Laptop",
      "brand": "Dell",
      "description": "Laptop gamer",
      "price": "1500.00",
      "cost": "1000.00",
      "stock": 10,
      "stock_min": 2,
      "condition": "ACTIVO",
      "start_date": "2024-01-01",
      "sku": "LAP-001",
      "category_id": 1
    }'

**Registrar una salida de stock (con token):**

    curl -X POST "http://127.0.0.1:8000/stock/out/LAP-001?quantity=3" \
    -H "Authorization: Bearer <token>"

**Ver historial de movimientos:**

    curl "http://127.0.0.1:8000/stock/history/LAP-001"

---

## Tests

    pytest tests/ -v

Los tests utilizan una base de datos SQLite en memoria para garantizar aislamiento entre ejecuciones. Se testean los endpoints de productos y categorías incluyendo validaciones de negocio como SKU duplicado y categoría inexistente.

---

## Autor

Santiago Abdala Ramos — [LinkedIn](https://www.linkedin.com/in/santiago-abdala-170982340/) · [GitHub](https://github.com/SantiAbdal)