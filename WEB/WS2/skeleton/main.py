from fastapi import FastAPI
from data.database import init_database
from routers.profiles import profiles_router
from routers.categories import categories_router

init_database()

app = FastAPI()

app.include_router(profiles_router)
app.include_router(categories_router)