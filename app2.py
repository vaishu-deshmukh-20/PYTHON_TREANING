from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>APP2 TESTING 12345</h1>"

@app.route("/about")
def about():
    return "<h1>About Us</h1><p>This is college management system.</p>"

@app.route("/students")
def students():
    return "<h1>Student list</h1><p>Student will show here</p>"

if __name__ == "__main__":
    app.run(debug=True)