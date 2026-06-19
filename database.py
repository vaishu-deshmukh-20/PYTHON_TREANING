import sqlite3

DB_NAME = "database.db"

# ---------------------------
# DATABASE CONNECTION
# ---------------------------
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------------
# INITIALIZE DATABASE
# ---------------------------
def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll INTEGER NOT NULL,
            marks INTEGER NOT NULL,
            subject TEXT NOT NULL,
            attendance INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


# ---------------------------
# ADD STUDENT
# ---------------------------
def add_student(name, roll, marks, subject, attendance=0):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (name, roll, marks, subject, attendance)
        VALUES (?, ?, ?, ?, ?)
    """, (name, roll, marks, subject, attendance))

    conn.commit()
    conn.close()


# ---------------------------
# GET ALL STUDENTS
# ---------------------------
def get_students():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    conn.close()
    return rows


# ---------------------------
# SEARCH STUDENTS
# ---------------------------
def search_students(query):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM students
        WHERE name LIKE ? OR roll=?
    """, ('%' + query + '%', query))

    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------------------
# DELETE STUDENT
# ---------------------------
def delete_student(student_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()


# ---------------------------
# UPDATE STUDENT
# ---------------------------
def update_student(student_id, name, roll, marks, subject, attendance):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        UPDATE students
        SET name=?, roll=?, marks=?, subject=?, attendance=?
        WHERE id=?
    """, (name, roll, marks, subject, attendance, student_id))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    #  for Data add 
    add_student('Pranavi', 1, 95, 'Math', 90)
    add_student('Rahul', 2, 88, 'Science', 85)
    print("Database ready! Table aani data donhi add zale.")
