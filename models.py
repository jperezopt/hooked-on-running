from pydantic import BaseModel


class Submission(BaseModel):
    id: int | None = None
    email: str
    name: str
    org: str
    message: str
    created_at: str | None = None


class Submissions(BaseModel):
    submissions: list[Submission]
