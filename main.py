from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from dotenv import load_dotenv
import mysql.connector
from contextlib import contextmanager

load_dotenv()

app = FastAPI()
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
                return RedirectResponse(url="/listtodos", status_code=303)
            else:
                return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid username or password"})
    except mysql.connector.Error as err:
        return await handle_db_error(request, err)

@app.get("/listtodos", response_class=HTMLResponse)
async def list_todos(request: Request):
    try:
        with get_db_connection() as mydb:
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute("SELECT * FROM todos")
            todos = mycursor.fetchall()
            return templates.TemplateResponse("index.html", {
                "request": request,
                "todos": todos
            })
    except mysql.connector.Error as err:
        return await handle_db_error(request, err)

@app.post("/addtodo", response_class=HTMLResponse)
async def add_todo(request: Request, title: str = Form(...)):
    try:
        with get_db_connection() as mydb:
            mycursor = mydb.cursor(dictionary=True)
            sql = "INSERT INTO todos (title) VALUES (%s)"
            mycursor.execute(sql, (title,))
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
async def logout():
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)





