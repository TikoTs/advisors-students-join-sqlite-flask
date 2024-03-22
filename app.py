from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect("sqlite3.db")
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT Advisor.AdvisorID, Advisor.AdvisorName, COUNT(Advisor_Student.StudentID) AS NumStudents
    FROM Advisor
    LEFT JOIN Advisor_Student ON Advisor.AdvisorID = Advisor_Student.AdvisorID
    GROUP BY Advisor.AdvisorID, Advisor.AdvisorName;
    """
    )

    advisors = cursor.fetchall()
    conn.close()

    return render_template("index.html", advisors=advisors)


@app.route("/students", methods=["GET", "POST"])
def students():
    advisor_id = request.form.get("advisor_id")

    conn = sqlite3.connect("sqlite3.db")
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT Advisor.AdvisorName, Student.StudentName
    FROM Advisor
    INNER JOIN Advisor_Student ON Advisor.AdvisorID = Advisor_Student.AdvisorID
    INNER JOIN Student ON Advisor_Student.StudentID = Student.StudentID
    WHERE Advisor.AdvisorID = ?;
    """,
        (advisor_id,),
    )

    students = cursor.fetchall()
    advisor_name = students[0][0] if students else None
    conn.close()

    return render_template(
        "students.html", advisor_name=advisor_name, students=students
    )


if __name__ == "__main__":
    app.run(debug=True)
