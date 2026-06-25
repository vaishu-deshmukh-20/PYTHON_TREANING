from flask import Flask

app = Flask(__name__)

# List of dictionaries (5 records)
students = [
    {"name": "Vaishnavi", "marks": 85, "attendance": "92%"},
    {"name": "Vishranti", "marks": 88, "attendance": "90%"},
    {"name": "Dipika", "marks": 82, "attendance": "89%"},
    {"name": "Kailas", "marks": 79, "attendance": "87%"},
    {"name": "Ashwin", "marks": 91, "attendance": "95%"}
]

# Route 1 - Homepage
@app.route("/")
def home():
    return """
    <h1>College Smart Portal</h1>
    <p>Student Login, Marks, Attendance and Notice Board System</p>
    """

# Route 2 - Records Page
@app.route("/records")
def records():
    output = "<h1>Student Records</h1>"
    for s in students:
        output += f"<p>Name: {s['name']} | Marks: {s['marks']} | Attendance: {s['attendance']}</p>"
    return output

# Route 3 - Extra Route
@app.route("/notice")
def notice():
    return """
    <h1>Notice Board</h1>
    <p>Tomorrow college will start at 10:00 AM.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)