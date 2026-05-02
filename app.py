from flask import Flask, render_template, request

app = Flask(__name__)

schemes = [
    {"name": "PM Kisan Samman Nidhi", "occupation": "Farmer", "max_income": 600000, "link": "https://pmkisan.gov.in"},
    {"name": "Rythu Bandhu Scheme", "occupation": "Farmer", "max_income": 800000, "link": "https://rythubandhu.telangana.gov.in"},
    {"name": "PM Fasal Bima Yojana", "occupation": "Farmer", "max_income": 1000000, "link": "https://pmfby.gov.in"},
    {"name": "Kisan Credit Card", "occupation": "Farmer", "link": "https://www.nabard.org"},

    {"name": "UP Scholarship", "occupation": "Student", "max_income": 300000, "link": "https://scholarship.up.gov.in"},
    {"name": "National Scholarship Portal", "occupation": "Student", "max_income": 500000, "link": "https://scholarships.gov.in"},
    {"name": "Post Matric Scholarship", "occupation": "Student", "max_income": 250000, "link": "https://scholarships.gov.in"},
    {"name": "AICTE Scholarship", "occupation": "Student", "link": "https://www.aicte-india.org"},

    {"name": "MGNREGA Scheme", "occupation": "Unemployed", "max_income": 200000, "link": "https://nrega.nic.in"},
    {"name": "PM Rozgar Yojana", "occupation": "Unemployed", "max_income": 400000, "link": "https://msme.gov.in"},
    {"name": "Skill India Mission", "occupation": "Unemployed", "link": "https://skillindia.gov.in"},

    {"name": "SSC Exams", "education": "Graduate", "link": "https://ssc.nic.in"},
    {"name": "UPSC Exams", "education": "Graduate", "link": "https://upsc.gov.in"},
    {"name": "Banking Exams (IBPS)", "education": "Graduate", "link": "https://ibps.in"},
    {"name": "State PSC Exams", "education": "Graduate", "link": "#"},

    {"name": "Railway Recruitment", "education": "12th Pass", "link": "https://indianrailways.gov.in"},
    {"name": "Police Recruitment", "education": "12th Pass", "link": "#"},
    {"name": "Defense Jobs (Army/Navy)", "education": "12th Pass", "link": "https://joinindianarmy.nic.in"},

    {"name": "Ayushman Bharat Yojana", "max_income": 300000, "link": "https://pmjay.gov.in"},
    {"name": "PM Awas Yojana", "max_income": 500000, "link": "https://pmaymis.gov.in"},
    {"name": "Jan Dhan Yojana", "link": "https://pmjdy.gov.in"},
    {"name": "Startup India Scheme", "education": "Graduate", "link": "https://startupindia.gov.in"},

    {"name": "Women Welfare Scheme", "link": "#"},
    {"name": "Senior Citizen Pension", "link": "#"},
    {"name": "Disability Support Scheme", "link": "#"}
]

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    user_name = ""

    if request.method == "POST":
        try:
            user_name = request.form.get("name", "")
            income = int(request.form.get("income", 0))
            education = request.form.get("education", "")
            occupation = request.form.get("occupation", "")

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

        except:
            results = []

    return render_template("index.html", results=results, user_name=user_name)


if __name__ == "__main__":
    app.run(debug=True)
