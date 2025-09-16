from flask import Flask, render_template, request, redirect, url_for, session
import os  # import os for random key

app = Flask(__name__)

# Generate a secure random secret key
app.secret_key = os.urandom(24)
# Question Bank (20 Questions)
questions = [
    {"question": "What is the capital of France?", "options": ["A. Paris","B. Rome","C. Berlin","D. Madrid"], "answer": "A"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth","B. Mars","C. Jupiter","D. Saturn"], "answer": "B"},
    {"question": "Who wrote 'Hamlet'?", "options": ["A. Dickens","B. Shakespeare","C. Twain","D. Austen"], "answer": "B"},
    {"question": "Which gas do plants absorb?", "options": ["A. Oxygen","B. Nitrogen","C. Carbon Dioxide","D. Hydrogen"], "answer": "C"},
    {"question": "Largest ocean on Earth?", "options": ["A. Atlantic","B. Indian","C. Arctic","D. Pacific"], "answer": "D"},
    {"question": "When did World War II end?", "options": ["A. 1945","B. 1939","C. 1918","D. 1950"], "answer": "A"},
    {"question": "Square root of 144?", "options": ["A. 10","B. 12","C. 14","D. 16"], "answer": "B"},
    {"question": "Which organ purifies blood?", "options": ["A. Heart","B. Liver","C. Kidney","D. Lungs"], "answer": "C"},
    {"question": "Father of Computers?", "options": ["A. Turing","B. Babbage","C. Edison","D. Gates"], "answer": "B"},
    {"question": "Smallest continent?", "options": ["A. Africa","B. Europe","C. Australia","D. South America"], "answer": "C"},
    {"question": "Symbol 'O'?", "options": ["A. Gold","B. Oxygen","C. Osmium","D. Iron"], "answer": "B"},
    {"question": "Who painted Mona Lisa?", "options": ["A. Van Gogh","B. da Vinci","C. Picasso","D. Michelangelo"], "answer": "B"},
    {"question": "Currency of Japan?", "options": ["A. Yen","B. Dollar","C. Won","D. Peso"], "answer": "A"},
    {"question": "Fastest land animal?", "options": ["A. Cheetah","B. Tiger","C. Horse","D. Leopard"], "answer": "A"},
    {"question": "H2O is?", "options": ["A. Oxygen","B. Hydrogen","C. Water","D. Salt"], "answer": "C"},
    {"question": "Festival of Lights (India)?", "options": ["A. Holi","B. Diwali","C. Eid","D. Christmas"], "answer": "B"},
    {"question": "Largest mammal?", "options": ["A. Elephant","B. Whale Shark","C. Blue Whale","D. Giraffe"], "answer": "C"},
    {"question": "How many continents?", "options": ["A. 5","B. 6","C. 7","D. 8"], "answer": "C"},
    {"question": "Instrument for pressure?", "options": ["A. Thermometer","B. Barometer","C. Hygrometer","D. Anemometer"], "answer": "B"},
    {"question": "Longest river?", "options": ["A. Nile","B. Amazon","C. Ganga","D. Yangtze"], "answer": "A"},
]





@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["roll"] = request.form["roll"]
        return redirect(url_for("instructions"))  # go to instructions first
    return render_template("index.html")



@app.route("/instructions", methods=["GET", "POST"])
def instructions():
    if "name" not in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        # Initialize quiz variables when student proceeds
        session["current_q"] = 0
        session["score"] = 0
        session["wrong_count"] = 0
        session["penalty"] = 0
        session["answers"] = []
        return redirect(url_for("quiz"))

    return render_template("instructions.html", name=session["name"])


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "current_q" not in session:
        return redirect(url_for("index"))

    q_index = session["current_q"]

    if request.method == "POST":
        user_answer = request.form.get("answer")  # None if skipped
        correct_answer = questions[q_index]["answer"]

        if not user_answer:  # Skipped question
            session["score"] -= 2  # -2 for skipping
            session["wrong_count"] += 1
            session["penalty"] += 2.5 if session["wrong_count"] > 1 else 0
            session["answers"].append("Skipped")
        elif user_answer == correct_answer:
            session["score"] += 10  # correct answer points
            session["wrong_count"] = 0  # reset wrong streak
            session["penalty"] = 0  # reset penalty
            session["answers"].append(user_answer)
        else:  # wrong answer
            session["wrong_count"] += 1
            if session["wrong_count"] > 1:
                session["penalty"] += 2.5  # incremental penalty
            else:
                session["penalty"] = 0  # first wrong = 0
            session["score"] -= session["penalty"]
            session["answers"].append(user_answer)

        session["current_q"] += 1

        if session["current_q"] >= len(questions):
            return redirect(url_for("result"))

    q_index = session["current_q"]
    return render_template("quiz.html", q=questions[q_index], index=q_index+1, total=len(questions))

@app.route("/result")
def result():
    return render_template("result.html", name=session["name"], roll=session["roll"],
                           questions=questions, answers=session["answers"], score=session["score"])

if __name__ == "__main__":
    app.run(debug=True)
