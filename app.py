from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from database import get_submissions, insert_submission
from models import Submissions, Submission
from sqlite3 import Connection, Row

app = FastAPI()
cx = Connection('app.db')
cx.row_factory = Row

templates = Jinja2Templates('./templates')

@app.get('/')
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, './index.html', context={})


@app.get("/submissions")
async def submissions() -> Submissions:
    return get_submissions(cx)

@app.post("/submisson")
async def submit(submission: Submission) -> Submission:
    insert_submission(cx, submission)
    return submission