from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

mycursor = mydb.cursor(dictionary=True)
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request}) 

@app.get("/listtodos", response_class=HTMLResponse)
async def root(request: Request):
    try:
        mycursor.execute("SELECT * FROM todos")
        todos = mycursor.fetchall()
        return templates.TemplateResponse("index.html", {
            "request": request,
            "todos": todos
        })
    except mysql.connector.Error as err:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": f"Database error: {err}"
        })

@app.post("/addtodo")
async def add_todo(title: str):
    try:
        sql = "INSERT INTO todos (title) VALUES (%s)"
        mycursor.execute(sql, (title,))
        mydb.commit()
        return {"message": "Todo added successfully"}
    except mysql.connector.Error as err:
        return {"error": f"Database error: {err}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)





