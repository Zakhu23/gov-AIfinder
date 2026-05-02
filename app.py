from flask import Flask, render_template, request

app = Flask(__name__)

# 🔥 DATABASE WITH APPLY LINKS
schemes = [
    {"name": "PM Kisan", "occupation": "Farmer", "max_income": 600000, "link": "https://pmkisan.gov.in"},
    {"name": "Rythu Bandhu", "occupation": "Farmer", "link": "https://rythubandhu.telangana.gov.in"},
    {"name": "PM Fasal Bima Yojana", "occupation": "Farmer", "link": "https://pmfby.gov.in"},

    {"name": "UP Scholarship", "occupation": "Student", "max_income": 300000, "link": "https://scholarship.up.gov.in"},
    {"name": "National Scholarship", "occupation": "Student", "max_income": 500000, "link": "https://scholarships.gov.in"},
    {"name": "Post Matric Scholarship", "occupation": "Student", "max_income": 250000, "link": "https://scholarships.gov.in"},

    {"name": "MGNREGA", "occupation": "Unemployed", "max_income": 200000, "link": "https://nrega.nic.in"},
    {"name": "PM Rozgar Yojana", "occupation": "Unemployed", "link": "https://pmrpy.gov.in"},

    {"name": "SSC Exams", "education": "Graduate", "link": "https://ssc.nic.in"},
    {"name": "UPSC Exams", "education": "Graduate", "link": "https://upsc.gov.in"},
    {"name": "Banking Exams", "education": "Graduate", "link": "https://ibps.in"},
    {"name": "Railway Exams", "education": "12th Pass", "link": "https://rrbcdg.gov.in"},
    {"name": "Police Exams", "education": "12th Pass", "link": "https://police.gov.in"},
    {"name": "Defense Exams", "education": "12th Pass", "link": "https://joinindianarmy.nic.in"},

    {"name": "Ayushman Bharat", "max_income": 300000, "link": "https://pmjay.gov.in"},
    {"name": "PM Awas Yojana", "max_income": 500000, "link": "https://pmaymis.gov.in"},
    {"name": "Jan Dhan Yojana", "link": "https://pmjdy.gov.in"},
    {"name": "Skill India", "education": "12th Pass", "link": "https://skillindia.gov.in"},
    {"name": "Startup India", "education": "Graduate", "link": "https://startupindia.gov.in"},

    {"name": "State Farmer Scheme", "occupation": "Farmer", "link": "#"},
    {"name": "State Student Scheme", "occupation": "Student", "link": "#"},
    {"name": "Women Welfare Scheme", "link": "#"},
    {"name": "Senior Citizen Scheme", "link": "#"},
    {"name": "Disability Scheme", "link": "#"}
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
                results.append(s)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
