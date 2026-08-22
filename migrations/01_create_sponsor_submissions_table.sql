CREATE TABLE sponsors_submissions (
    id INTEGER PRIMARY KEY,
    sponsor_email VARCHAR(50) NOT NULL,
    sponsor_name VARCHAR(50) NOT NULL,
    sponsor_org VARCHAR(50) NOT NULL,
    sponsor_text VARCHAR(300) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)