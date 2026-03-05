# E-commerce API

API REST desarrollada con **FastAPI** para gestionar productos y categorías en un sistema de inventario o e-commerce.

Este proyecto fue creado como práctica de desarrollo backend utilizando una arquitectura en capas para separar responsabilidades.

---

# Tecnologías utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

# Arquitectura del proyecto

El proyecto sigue una arquitectura en capas:

Router → Service → Repository → Database

### Router
Define los endpoints de la API.

### Service
Contiene la lógica de negocio y validaciones.

### Repository
Se encarga de interactuar con la base de datos.

### Models
Representan las tablas de la base de datos.

### Schemas
Validan los datos que entran y salen de la API.

---

# Estructura del proyecto

```
project/
│
├── db/
│   └── db.py
│
├── models/
│   ├── product_model.py
│   └── category_model.py
│
├── schemas/
│   ├── product_schema.py
│   └── category_schema.py
│
├── repository/
│   ├── product_repository.py
│   └── category_repository.py
│
├── services/
│   ├── product_services.py
│   └── category_services.py
│
├── routers/
│   ├── product_router.py
│   └── category_router.py
│
└── main.py
```

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/ecommerce-api.git
cd ecommerce-api
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# Ejecutar la API

```bash
uvicorn main:app --reload
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

---

# Documentación automática

FastAPI genera documentación automática.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# Endpoints principales

## Productos

GET /products  
GET /products/{id}  
POST /products  
PUT /products/{id}  
DELETE /products/{id}

## Categorías

GET /categories  
GET /categories/{id}  
POST /categories  
DELETE /categories/{id}

---

# Autor

Proyecto desarrollado como práctica de backend utilizando FastAPI.