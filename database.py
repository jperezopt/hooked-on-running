import sqlite3
from sqlite3 import Connection


def get_all_submissions(cx: Connection) -> list[tuple]:
    with cx:
        cur = cx.cursor()
        cur.execute(
            """
            SELECT id, sponsor_email, sponsor_name, sponsor_org, sponsor_text
            FROM sponsor_submissions
            """
        )
        return cur.fetchall()


def insert_submission(cx: Connection, submission: dict):
    with cx:
        cur = cx.cursor()
        cur.execute(
            """
            INSERT INTO sponsor_submissions
                (sponsor_email, sponsor_name, sponsor_org, sponsor_text)
            VALUES
                (:sponsor_email, :sponsor_name, :sponsor_org, :sponsor_text)
            """,
            submission,
        )


if __name__ == "__main__":
    cx = sqlite3.connect("app.db")
    cx.row_factory = sqlite3.Row

    test_submission = {
        "sponsor_email": "JTest@gmail.com",
        "sponsor_name": "Jon Test",
        "sponsor_org": "Testing Inc",
        "sponsor_text": "Testing 123",
    }

    for submission in get_all_submissions(cx):
        print(dict(submission))
