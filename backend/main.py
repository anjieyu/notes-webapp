import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def connect_db():
    connection = sqlite3.connect("notes.db")
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    db = connect_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            body TEXT NOT NULL DEFAULT '',
            updated_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """
    )
    db.commit()
    db.close()

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
init_db()

@app.get("/notes")
def list_notes():
    return {"message": "return the user's notes"}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    return {"message": "return one note"}