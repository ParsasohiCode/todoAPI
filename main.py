from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
import os
from dotenv import load_dotenv
import mysql.connector
from contextlib import contextmanager

load_dotenv()

app = FastAPI()
# Add session middleware with a secret key
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Database connection helper
@contextmanager
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    try:
        yield connection
    finally:
        connection.close()

# Error handler
async def handle_db_error(request: Request, error: Exception):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "error": f"Database error: {error}"
    })

# Routes
@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse )
async def login(request: Request , username: str = Form(...), password: str = Form(...)):
    try:
        with get_db_connection() as mydb:
            mycursor = mydb.cursor(dictionary=True)
            sql = "SELECT * FROM users WHERE username = %s AND password = %s"
            mycursor.execute(sql, (username, password))
            user = mycursor.fetchone()
            if user:
                # Store username in session
                request.session["username"] = username
                return RedirectResponse(url="/listtodos", status_code=303)
            else:
                return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid username or password"})
    except mysql.connector.Error as err:
        return await handle_db_error(request, err)
    
@app.get("/registerpage", response_class=HTMLResponse)
async def registerpage(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, username: str = Form(...), password: str = Form(...)):
    try:
        with get_db_connection() as mydb:
            mycursor = mydb.cursor(dictionary=True)
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            mycursor.execute(sql, (username, password))
            mydb.commit()
            return RedirectResponse(url="/", status_code=303)
    except mysql.connector.Error as err:
        return await handle_db_error(request, err)

@app.get("/listtodos", response_class=HTMLResponse)
async def list_todos(request: Request):
    username = request.session.get("username")
    if username is None:
        return RedirectResponse(url="/", status_code=303)
    try:
        with get_db_connection() as mydb:
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute("SELECT * FROM todos WHERE created_by = %s", (username,))
            todos = mycursor.fetchall()
            return templates.TemplateResponse("index.html", {
                "request": request,
                "todos": todos
            })
    except mysql.connector.Error as err:
        return await handle_db_error(request, err)

@app.post("/addtodo", response_class=HTMLResponse)
async def add_todo(request: Request, title: str = Form(...)):
    username = request.session.get("username")
    if username is None:
        return RedirectResponse(url="/", status_code=303)
    try:
        with get_db_connection() as mydb:
            mycursor = mydb.cursor(dictionary=True)
            sql = "INSERT INTO todos (title,created_by) VALUES (%s,%s)"
            mycursor.execute(sql, (title,username))
            mydb.commit()
            return RedirectResponse(url="/listtodos", status_code=303)
    except mysql.connector.Error as err:
        return await handle_db_error(request, err)

@app.post("/updatetodo/{id}", response_class=HTMLResponse)
async def update_todo(request: Request, id: int):
    try:
        with get_db_connection() as mydb:
            mycursor = mydb.cursor(dictionary=True)
            sql = "UPDATE todos SET completed = NOT completed WHERE id = %s"
            mycursor.execute(sql, (id,))
            mydb.commit()
            return RedirectResponse(url="/listtodos", status_code=303)
    except mysql.connector.Error as err:
        return await handle_db_error(request, err)

@app.post("/deletetodo/{id}", response_class=HTMLResponse)
async def delete_todo(request: Request, id: int):
    try:
        with get_db_connection() as mydb:
            mycursor = mydb.cursor(dictionary=True)
            sql = "DELETE FROM todos WHERE id = %s"
            mycursor.execute(sql, (id,))
            mydb.commit()
            return RedirectResponse(url="/listtodos", status_code=303)
    except mysql.connector.Error as err:
        return await handle_db_error(request, err)

@app.post("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)