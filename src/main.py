import psycopg2
from fastapi import FastAPI, HTTPException

app = FastAPI()

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="test_db",
        user="user",
        password="password"
    )
    return conn

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/data")
def read_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mytable")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    if not rows:
        raise HTTPException(status_code=404, detail="No data found")

    return {"data": rows}
