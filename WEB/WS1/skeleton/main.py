from fastapi import FastAPI
from data.database import init_database
from routers.developers import developer_router
from routers.projects import project_router
import uvicorn

init_database()

app = FastAPI()
app.include_router(developer_router)
app.include_router(project_router)

if __name__ =='__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)