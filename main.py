from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.db import Base, engine
from routers.category_router import router as category_router
from routers.product_router import router as product_router
app = FastAPI(title="E-commerce API", version="1.0.0")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(category_router)
app.include_router(product_router)
