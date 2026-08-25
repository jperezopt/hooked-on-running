from pydantic import BaseModel


class Submission(BaseModel):
    sponsor_email: str
    sponsor_name: str
    sponsor_org: str
    sponsor_text: str

class Submissions(BaseModel):
    submissions: list[Submission]
