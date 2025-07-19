from fastapi import FastAPI
from app.database.session import Base, engine
from app.api.routes.routes_user import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)