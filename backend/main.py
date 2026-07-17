import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def connect_db():
    connection = sqlite3.connect("notes.db")
    connection.row_factory = sqlite3.Row
    return connection

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:3000",
        "https://notes.anjieyu.net"
    ],
    allow_methods = ["*"],
    allow_headers = ["*"]
)
db = connect_db()
db.close()