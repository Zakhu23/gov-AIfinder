from flask import Flask, render_template, request

app = Flask(__name__)

# 🔥 REAL DATABASE (24 RECORDS)
schemes = [
    {"name": "PM Kisan", "occupation": "Farmer", "max_income": 600000},
    {"name": "Rythu Bandhu", "occupation": "Farmer", "max_income": 800000},
    {"name": "PM Fasal Bima Yojana", "occupation": "Farmer", "max_income": 1000000},

    {"name": "UP Scholarship", "occupation": "Student", "max_income": 300000},
    {"name": "National Scholarship", "occupation": "Student", "max_income": 500000},
    {"name": "Post Matric Scholarship", "occupation": "Student", "max_income": 250000},

    {"name": "MGNREGA", "occupation": "Unemployed", "max_income": 200000},
    {"name": "PM Rozgar Yojana", "occupation": "Unemployed", "max_income": 400000},

    {"name": "SSC Exams", "education": "Graduate"},
    {"name": "UPSC Exams", "education": "Graduate"},
    {"name": "Banking Exams", "education": "Graduate"},
    {"name": "Railway Exams", "education": "12th Pass"},
    {"name": "Police Exams", "education": "12th Pass"},
    {"name": "Defense Exams", "education": "12th Pass"},

    {"name": "Ayushman Bharat", "max_income": 300000},
    {"name": "PM Awas Yojana", "max_income": 500000},
    {"name": "Jan Dhan Yojana"},
    {"name": "Skill India", "education": "12th Pass"},
    {"name": "Startup India", "education": "Graduate"},

    {"name": "State Farmer Scheme", "occupation": "Farmer"},
    {"name": "State Student Scheme", "occupation": "Student"},
    {"name": "Women Welfare Scheme"},
    {"name": "Senior Citizen Scheme"},
    {"name": "Disability Scheme"}
]

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        age = int(request.form["age"])
        income = int(request.form["income"])
        education = request.form["education"]
        occupation = request.form["occupation"]

        for s in schemes:
            match = True

            if "occupation" in s and s["occupation"] != occupation:
                match = False

            if "education" in s and s["education"] != education:
                match = False

            if "max_income" in s and income > s["max_income"]:
                match = False

            if match:
                results.append(s["name"])

    return render_template("index.html", results=results)
