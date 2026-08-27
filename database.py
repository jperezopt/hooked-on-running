import sqlite3
from sqlite3 import Connection

from models import Submission, Submissions


def get_submissions(cx: Connection) -> Submissions:
    with cx:
        cur = cx.cursor()
        cur.execute("""
            SELECT id, email, name, org, message, created_at 
            FROM submissions 
            """)
        return Submissions(
            submissions=[
                Submission.model_validate(dict(submission))
                for submission in cur
            ]
        )


def insert_submission(cx: Connection, submission: Submission):
    with cx:
        cur = cx.cursor()
        cur.execute(
            """
            INSERT INTO submissions 
                (email, name, org, message)
            VALUES
                (:email, :name, :org, :message)
            """,
            submission.model_dump(),
        )


if __name__ == "__main__":
    cx = sqlite3.connect("app.db")
    cx.row_factory = sqlite3.Row
    test_submission = Submission(
        email="test@test.com",
        name="john test",
        org="testing inc",
        message="testing123",
    )
    # insert_submission(cx, test_submission)
    print(get_submissions(cx))
