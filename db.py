import sqlite3

conn = sqlite3.connect("sqlite3.db")
cursor = conn.cursor()

cursor.executescript(
    """
CREATE TABLE IF NOT EXISTS Advisor(
    AdvisorID INTEGER NOT NULL,
    AdvisorName TEXT NOT NULL,
    PRIMARY KEY(AdvisorID)
);

CREATE TABLE IF NOT EXISTS Student(
    StudentID NUMERIC NOT NULL,
    StudentName NUMERIC NOT NULL,
    PRIMARY KEY(StudentID)
);

CREATE TABLE IF NOT EXISTS Advisor_Student(
    AdvisorID INTEGER,
    StudentID INTEGER,
    FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
    PRIMARY KEY(AdvisorID, StudentID)
);

INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
(1,"John Paul"),
(2,"Anthony Roy"),
(3,"Raj Shetty"),
(4,"Sam Reeds"),
(5,"Arthur Clintwood");

INSERT INTO Student(StudentID, StudentName) VALUES
(501,"Geek1"),
(502,"Geek2"),
(503,"Geek3"),
(504,"Geek4"),
(505,"Geek5"),
(506,"Geek6"),
(507,"Geek7"),
(508,"Geek8"),
(509,"Geek9"),
(510,"Geek10");

INSERT INTO Advisor_Student(AdvisorID, StudentID) VALUES
(1, 501),
(1, 502),
(2, 502),
(5, 503),
(2, 504),
(4, 505),
(2, 506),
(2, 507),
(5, 508),
(1, 510),
(4, 501);
"""
)

conn.commit()
conn.close()
