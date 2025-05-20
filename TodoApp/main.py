from fastapi import FastAPI, Request, status
from .database import engine
from .models import Base
from .routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse


app = FastAPI()
Base.metadata.create_all(bind = engine)

app.mount("/static",StaticFiles(directory="TodoApp/static"), name = 'static')# make sure it find the information related to static file while rendering the html files

@app.get("/")
def test(request:Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)

@app.get("/healthy") #Health check, checks application is up & running
def health_check():
    return {'status' : 'Healthy'}
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
