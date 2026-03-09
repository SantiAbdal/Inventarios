# Inventory API

API REST desarrollada con **FastAPI** para gestionar productos, categorías e inventario con historial de movimientos de stock.

---

## Tecnologías utilizadas

- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic V2
- Uvicorn
- Pytest

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
    ├── db/
    │   ├── db.py
    │   └── dependencies.py
    │
    ├── models/
    │   ├── product_model.py
    │   ├── category_model.py
    │   └── stock_movement_model.py
    │
    ├── schemas/
    │   ├── product_schema.py
    │   ├── product_condition_schema.py
    │   ├── category_schema.py
    │   ├── movement_type_schema.py
    │   └── stock_movement_schema.py
    │
    ├── repository/
    │   ├── product_repository.py
    │   ├── category_repository.py
    │   └── stock_movement_repository.py
    │
    ├── services/
    │   ├── product_services.py
    │   └── category_services.py
    │
    ├── routers/
    │   ├── product_router.py
    │   ├── category_router.py
    │   └── stock_movement_router.py
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

## Endpoints

### Productos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /products | Listar todos los productos |
| GET | /products/{id} | Obtener producto por ID |
| POST | /products | Crear producto |
| PUT | /products/{id} | Actualizar producto |
| DELETE | /products/{id} | Eliminar producto |
| GET | /products/low-stock | Productos con stock bajo |
| GET | /products/search/text | Buscar por nombre, marca o SKU |
| GET | /products/search/equal | Buscar por categoría o condición |
| GET | /products/search/range | Buscar por rango de precio, costo o fecha |
| GET | /products/search/category | Buscar por nombre de categoría |

### Categorías

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /categories | Listar todas las categorías |
| GET | /categories/{id} | Obtener categoría por ID |
| POST | /categories | Crear categoría |
| DELETE | /categories/{id} | Eliminar categoría |

### Stock

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | /stock/in/{sku} | Registrar entrada de stock |
| POST | /stock/out/{sku} | Registrar salida de stock |
| GET | /stock/history/{sku} | Ver historial de movimientos |

---

## Ejemplos de uso

**Crear una categoría:**

    curl -X POST "http://127.0.0.1:8000/categories/" \
    -H "Content-Type: application/json" \
    -d '{"name": "Electrónica"}'

**Crear un producto:**

    curl -X POST "http://127.0.0.1:8000/products" \
    -H "Content-Type: application/json" \
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

**Registrar una salida de stock:**

    curl -X POST "http://127.0.0.1:8000/stock/out/LAP-001?quantity=3"

**Ver historial de movimientos:**

    curl "http://127.0.0.1:8000/stock/history/LAP-001"

---

## Tests

    pytest tests/ -v

---

## Autor

Santiago Abdala Ramos — [LinkedIn](https://www.linkedin.com/in/santiago-abdala-170982340/) · [GitHub](https://github.com/SantiAbdal)
