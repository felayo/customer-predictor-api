import pandas as pd
import sqlite3

conn = sqlite3.connect("predictions.db")
df = pd.read_sql("SELECT * FROM prediction_logs", conn)
df.to_csv("prediction_evidence.csv", index=False)
conn.close()
