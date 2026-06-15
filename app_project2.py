from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "mysecretkey"

students = [
    {"roll": 101, "name": "Pranavi", "marks": 78, "status": "Pass"},
    {"roll": 102, "name": "Gauri", "marks": 92, "status": "Pass"},
    {"roll": 103, "name": "Savi", "marks": 66, "status": "Pass"},
    {"roll": 104, "name": "Tanvi", "marks": 81, "status": "Pass"},
    {"roll": 105, "name": "Neha", "marks": 55, "status": "Pass"}

]

@app.route("/search")
def search():
    #step 1: Get query from url
    q=request.args.get('q','')
    #request.args - GET parameters
    #step 2: 'q' - from - name = 'q'
    conn = get_db()

    if q:
        students = conn.execute('''SELECT * FROM students 
                              WHERE name LIKE ?
                              OR SUBJECT LIKE?
                              OR ROLL LIKE ?''',
                               ('%'+q+'%', '%'+q+'%', '%'+q+'%')).fetchall()
    
    else:
        students = conn.execute('SELECT * FROM students ORDER BY ID DESC').fetchall()
    conn.close()
    return render_template('students.html', students=students, query=q)


# HOME
@app.route("/")
def home():
    return render_template("home.html")


# STUDENTS PAGE
@app.route("/students")
def students_page():
    return render_template("students.html", students=students)


# NOTICE
@app.route("/notice")
def notice():
    return render_template("notice.html")


# ABOUT
@app.route("/about")
def about():
    return render_template("about.html")


# =========================
# EDIT STUDENT (FIXED)
# =========================
@app.route("/edit/<int:roll>", methods=["GET", "POST"])
def edit_student(roll):

    student = None

    for s in students:
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

        students.append(new_student)

        flash(f"Student {name} added successfully!", "success")
        return redirect(url_for("students_page"))

    return render_template("add_students.html")


# RUN APP
if __name__ == "__main__":
    app.run(debug=True)