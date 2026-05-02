from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        age = int(request.form["age"])
        income = int(request.form["income"])
        education = request.form["education"]
        occupation = request.form["occupation"]
        state = request.form["state"]

        # TEMP LOGIC (we will upgrade later)
        if occupation == "Student":
            results.append("Scholarship Scheme")

        if occupation == "Farmer":
            results.append("PM Kisan")

        if education == "Graduate":
            results.append("UPSC / SSC Exams")

        if income < 300000:
            results.append("Low Income Scheme")

    return render_template("index.html", results=results)
