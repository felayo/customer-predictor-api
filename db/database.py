import sqlite3
from pathlib import Path

DB_PATH = Path("predictions.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            default_value TEXT,
            balance INTEGER,
            housing TEXT,
            day INTEGER,
            month TEXT,
            campaign INTEGER,
            previous INTEGER,
            poutcome TEXT,
            probability REAL,
            prediction INTEGER,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def log_prediction(data, probability, prediction, message):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prediction_logs (
            default_value, balance, housing, day, month,
            campaign, previous, poutcome,
            probability, prediction, message
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["default"],
        data["balance"],
        data["housing"],
        data["day"],
        data["month"],
        data["campaign"],
        data["previous"],
        data["poutcome"],
        probability,
        prediction,
        message
    ))

    conn.commit()
    conn.close()
