from fastapi import FastAPI
from database import get_submissions
from models import Submissions
from sqlite3 import Connection, Row

app = FastAPI()
cx = Connection('app.db')
cx.row_factory = Row

@app.get("/submissions")
async def submissions()->Submissions:
    return get_submissions(cx)
