DROP TABLE IF EXISTS skills;

CREATE TABLE skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name TEXT NOT NULL,
    skill_desc TEXT NOT NULL,
    skill_level INTEGER NOT NULL
)