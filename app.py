from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from database import get_submissions, insert_submission
from models import Submissions, Submission
from sqlite3 import Connection, Row

app = FastAPI()
cx = Connection("app.db")
cx.row_factory = Row

templates = Jinja2Templates("./templates")


@app.get("/")
async def home(request: Request) -> HTMLResponse:
    submissions = get_submissions(cx)
    return templates.TemplateResponse(
        request, "./index.html", context=submissions.model_dump()
    )


@app.get("/submissions")
async def submissions(request: Request) -> HTMLResponse:
    submissions = get_submissions(cx)
    return templates.TemplateResponse(request, './submissions.html', context=submissions.model_dump())


@app.post("/submission")
async def submission(request: Request, submission: Submission) -> HTMLResponse:
    insert_submission(cx, submission)
    submissions = get_submissions(cx)
    return templates.TemplateResponse(request, './submissions.html', context=submissions.model_dump())
