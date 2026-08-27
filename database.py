import sqlite3
from sqlite3 import Connection

from models import Submission, Submissions


def get_submissions(cx: Connection) -> Submissions:
    with cx:
        cur = cx.cursor()
        cur.execute("""
            SELECT id, sponsor_email, sponsor_name, sponsor_org, sponsor_text
            FROM sponsor_submissions
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
            INSERT INTO sponsor_submissions
                (sponsor_email, sponsor_name, sponsor_org, sponsor_text)
            VALUES
                (:sponsor_email, :sponsor_name, :sponsor_org, :sponsor_text)
            """,
            submission.model_dump(),
        )


if __name__ == "__main__":
    cx = sqlite3.connect("app.db")
    cx.row_factory = sqlite3.Row
    test_submission = Submission(
        sponsor_email="test@test.com",
        sponsor_name="john test",
        sponsor_org="testing inc",
        sponsor_text="testing123",
    )
    # insert_submission(cx, test_submission)
    print(get_submissions(cx))
