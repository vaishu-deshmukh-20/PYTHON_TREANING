student = [
    {"name": "Vaishnavi","marks": 85}
    {"name": "Rohit","marks": 90}
    {"name": "pranav","marks":86}
]

def get_ststus (marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


   #partc
   for student in students:
    status = get_status(student["marks"])
    print(f"{student['name']}:{student ['marks']} - {status}")

    #step1-flask
    from flask import Flask, render_template,request,redirect,url_for,flash msg

    app = Flask(__name__)

    app.secret_key = "your_secret_key"

    #step2-get_db()function

    sqlite3
    retur connectionAborted


    import sqlite3
    from flask import Flask,render_templete