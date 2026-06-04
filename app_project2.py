from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"roll": 101, "name": "Pranavi", "marks": 78},
    {"roll": 102, "name": "Gauri", "marks": 92},
    {"roll": 103, "name": "Savi", "marks": 66},
    {"roll": 104, "name": "Tanvi", "marks": 81},
    {"roll": 105, "name": "Neha", "marks": 55}
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/students")
def students_page():
    return render_template("students.html", students=students)

@app.route("/notice")
def notice():
    return render_template("notice.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)