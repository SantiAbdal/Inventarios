from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.db import Base, engine
from routers.category_router import router as category_router
from routers.product_router import router as product_router
from routers.stock_movement_router import router as stock_movement_router
from routers.auth_router import router as auth_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="E-commerce API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category_router)
app.include_router(product_router)
app.include_router(stock_movement_router)
app.include_router(auth_router)
