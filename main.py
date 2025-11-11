from fastapi import FastAPI
from .routers import orders
from .db import lifespan


app = FastAPI(lifespan=lifespan)
app.include_router(orders.router)



