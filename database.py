import sqlite3

connection = sqlite3.connect('app.db')

test_submission = {
    'sponsor_email': 'JTest@gmail.com',
    'sponsor_name': 'Jon Test',
    'sponsor_org': 'Testing Inc',
    'sponsor_text': 'Testing 123'
}

with connection:
    cur = connection.cursor()
    cur.execute(
        '''INSERT INTO sponsor_submissions
               (sponsor_email, sponsor_name, sponsor_org, sponsor_text)
           VALUES
               (:sponsor_email, :sponsor_name, :sponsor_org, :sponsor_text)''',
        test_submission,
    )