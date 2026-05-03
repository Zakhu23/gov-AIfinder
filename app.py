from flask import Flask, render_template, request

app = Flask(__name__)

# 🔥 FULL DATABASE WITH AGE + ALL FILTERS
schemes = [

    # 👨‍🌾 FARMER SCHEMES
    {"name": "PM Kisan", "occupation": "Farmer", "max_income": 600000, "state": "All", "min_age": 18, "link": "https://pmkisan.gov.in"},
    {"name": "Rythu Bandhu", "occupation": "Farmer", "state": "Telangana", "min_age": 18, "link": "https://rythubandhu.telangana.gov.in"},
    {"name": "YSR Rythu Bharosa", "occupation": "Farmer", "state": "Andhra Pradesh", "min_age": 18, "link": "#"},

    # 🎓 STUDENT SCHEMES
    {"name": "National Scholarship", "occupation": "Student", "max_income": 500000, "state": "All", "min_age": 16, "link": "https://scholarships.gov.in"},
    {"name": "UP Scholarship", "occupation": "Student", "state": "Uttar Pradesh", "min_age": 16, "link": "https://scholarship.up.gov.in"},
    {"name": "Post Matric Scholarship", "occupation": "Student", "max_income": 250000, "min_age": 16, "state": "All", "link": "https://scholarships.gov.in"},

    # 👩 WOMEN SCHEMES
    {"name": "Mahila Shakti Scheme", "gender": "Female", "min_age": 18, "state": "All", "link": "#"},
    {"name": "Beti Bachao Beti Padhao", "gender": "Female", "min_age": 0, "state": "All", "link": "#"},

    # 👨 GENERAL SCHEMES
    {"name": "Ayushman Bharat", "max_income": 300000, "state": "All", "link": "https://pmjay.gov.in"},
    {"name": "PM Awas Yojana", "max_income": 500000, "state": "All", "link": "https://pmaymis.gov.in"},
    {"name": "Jan Dhan Yojana", "state": "All", "link": "https://pmjdy.gov.in"},

    # 👨‍💼 EMPLOYED
    {"name": "EPFO Benefits", "occupation": "Employed", "min_age": 18, "state": "All", "link": "https://epfindia.gov.in"},
    {"name": "Skill Upgrade Program", "occupation": "Employed", "min_age": 18, "state": "All", "link": "https://skillindia.gov.in"},

    # 🧪 COMPETITIVE EXAMS
    {"name": "UPSC Civil Services", "education": "Graduate", "min_age": 21, "max_age": 32, "state": "All", "link": "https://upsc.gov.in"},
    {"name": "SSC Exams", "education": "Graduate", "min_age": 18, "max_age": 30, "state": "All", "link": "https://ssc.nic.in"},
    {"name": "Banking Exams (IBPS)", "education": "Graduate", "min_age": 20, "max_age": 30, "state": "All", "link": "https://ibps.in"},
    {"name": "RRB Railway Exams", "education": "12th Pass", "min_age": 18, "max_age": 30, "state": "All", "link": "https://indianrailways.gov.in"},
    {"name": "Defense Exams", "education": "12th Pass", "gender": "Male", "min_age": 17, "max_age": 23, "state": "All", "link": "https://joinindianarmy.nic.in"},
    {"name": "Teaching Exams (TET)", "education": "Graduate", "min_age": 21, "state": "All", "link": "#"},
    {"name": "State PSC Exams", "education": "Graduate", "min_age": 21, "state": "All", "link": "#"},
    {"name": "Police Exams", "education": "12th Pass", "min_age": 18, "state": "All", "link": "#"},

    # 🌍 STATE SPECIFIC
    {"name": "Delhi Free Electricity Scheme", "state": "Delhi", "link": "#"},
    {"name": "Tamil Nadu Free Laptop Scheme", "state": "Tamil Nadu", "min_age": 16, "link": "#"},
    {"name": "Karnataka Gruha Lakshmi Scheme", "state": "Karnataka", "gender": "Female", "min_age": 18, "link": "#"},

    # 👴 SPECIAL CATEGORY
    {"name": "Senior Citizen Pension", "min_age": 60, "state": "All", "link": "#"},
    {"name": "Disability Support Scheme", "state": "All", "link": "#"}
]


@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    user_name = ""

    if request.method == "POST":
        try:
            user_name = request.form.get("name", "")
            age = int(request.form.get("age", 0))
            income = int(request.form.get("income", 0))
            education = request.form.get("education", "")
            occupation = request.form.get("occupation", "")
            gender = request.form.get("gender", "")
            state = request.form.get("state", "")

            for s in schemes:
                match = True

                # Occupation
                if "occupation" in s and s["occupation"] != occupation:
                    match = False

                # Education
                if "education" in s and s["education"] != education:
                    match = False

                # Gender
                if "gender" in s and s["gender"] != gender:
                    match = False

                # State
                if "state" in s and s["state"] != "All" and s["state"] != state:
                    match = False

                # Income
                if "max_income" in s and income > s["max_income"]:
                    match = False

                # Age (NEW 🔥)
                if "min_age" in s and age < s["min_age"]:
                    match = False

                if "max_age" in s and age > s["max_age"]:
                    match = False

                if match:
                    results.append(s)

        except:
            results = []

    return render_template("index.html", results=results, user_name=user_name)


if __name__ == "__main__":
    app.run(debug=True)
