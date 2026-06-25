from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder="templates")

from database import get_db, search_students, add_student
app.secret_key = "mysecretkey"

students_list = [
    {"roll": 101, "name": "Pranavi", "marks": 96, "status": "Pass"},
    {"roll": 102, "name": "Gauri", "marks":87 , "status": "Pass"},
    {"roll": 103, "name": "Savi", "marks": 66, "status": "Pass"},
    {"roll": 104, "name": "Tanvi", "marks": 30, "status": "Pass"},
    {"roll": 105, "name": "Neha", "marks": 45, "status": "Pass"}

]

@app.route("/search")
def search():
    q = request.args.get('q', '')

    conn = get_db()

    if q:
        students = conn.execute("""
            SELECT * FROM students 
            WHERE name LIKE ? OR roll LIKE ?
        """, ('%' + q + '%', '%' + q + '%')).fetchall()
    else:
        students = conn.execute("""
            SELECT * FROM students ORDER BY id DESC
        """).fetchall()

    conn.close()
    return render_template('students.html', students=students, query=q)

# HOME
@app.route("/")
def home():
    return render_template("home.html")


# STUDENTS PAGE
@app.route("/students")
def students_page():

    # ALWAYS create fresh calculated list (IMPORTANT)
    clean_students = []

    for s in students_list:
        clean_students.append({
            "roll": s["roll"],
            "name": s["name"],
            "marks": int(s["marks"]),
            "status": s["status"]
        })

    excellent = len([s for s in clean_students if s["marks"] >= 75])
    good = len([s for s in clean_students if 40 <= s["marks"] < 75])
    need_improvement = len([s for s in clean_students if s["marks"] < 40])

    return render_template(
        "students.html",
        students=clean_students,
        excellent=excellent,
        good=good,
        need_improvement=need_improvement
    )

# view student details
@app.route("/student/<int:roll>")
def student_detail(roll):
    student = next((s for s in students_list if s["roll"] == roll), None)

    if student:
        return render_template("details.html", student=student)

    flash("Student not found!", "danger")
    return redirect(url_for("students_page"))


# NOTICE
@app.route("/notice")
def notice():
    return render_template("notice.html")


# ABOUT
@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/logout')
def logout():
    session.pop('username',None)
    flash ('you have been logged out.','info')
    return redirect(url_for('home'))

# 404.html
def page_not_found(e):
    return render_template('404.html'),404


# =========================
# EDIT STUDENT (FIXED)
# =========================
@app.route("/edit/<int:roll>", methods=["GET", "POST"])
def edit_student(roll):

    student = None

    for s in students_list:
        if s["roll"] == roll:
            student = s
            break

    if request.method == "POST":
        student["name"] = request.form["student_name"]
        student["marks"] = int(request.form["marks"])
        student["status"] = "Pass" if student["marks"] >= 35 else "Fail"

        flash("Student updated successfully!", "success")
        return redirect(url_for("students_page"))

    return render_template("edit_student.html", student=student)

# =================
# DELETE STUDENT
# =================
@app.route("/delete/<int:roll>")
def delete_student(roll):
    global students_list

    students_list = [s for s in students_list if s["roll"] != roll]

    flash("Student deleted successfully!", "success")
    return redirect(url_for("students_page"))

# =========================
# ADD STUDENT
# =========================
@app.route("/add", methods=["GET", "POST"])
def add_students():

    if request.method == "POST":

        name = request.form["student_name"]
        roll = request.form["roll"]
        marks = request.form["marks"]

        if not name or not roll or not marks:
            flash("Please fill all fields", "danger")
            return render_template("add_students.html")

        status = "Pass" if int(marks) >= 35 else "Fail"

        new_student = {
            "roll": int(roll),
            "name": name,
            "marks": int(marks),
            "status": status
        }

        students_list.append(new_student)

        flash(f"Student {name} added successfully!", "success")
        return redirect(url_for("students_page"))

    return render_template("add_students.html")

# RUN APP
if __name__ == "__main__":

    app.run(debug=True)
    