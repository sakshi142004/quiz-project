
# 🎯 Quiz Application

A simple **Quiz Web Application** built with **Python (Flask)**, **HTML**, **CSS**, and **JavaScript**.
This project allows students to attempt multiple-choice questions with a **custom scoring and penalty system**.

---

## 🚀 Features

* ✅ User login with **Name & Roll Number** before starting quiz
* ✅ **20 Multiple Choice Questions**
* ✅ **Scoring System**:

  * Correct Answer → **+10 points**
  * Skip Answer → **-2 points**
  * Wrong Answer → **Penalty System**:

    * 1st wrong → `0 penalty`
    * 2nd wrong → `-2.5% of one question mark` (i.e., -0.25)
    * 3rd wrong → `-5% of one question mark` (i.e., -0.5)
    * 4th wrong → `-7.5% of one question mark` (i.e., -0.75)
    * (Penalty increases for consecutive wrongs)
    * If the next answer is correct → **penalty resets to 0**
* ✅ Final Results Page:

  * Final Score out of 200
  * Correct answers count
  * Percentage
  * Pass/Fail status (At least **9 correct answers → Pass**)
  * Answer Review (shows correct answer vs user answer)

---

## 📂 Project Structure

```
quiz_project/
│
├── app.py              # Main Flask app
│
├── templates/          # HTML templates
│   ├── index.html      # Student info form
│   ├── instructions.html # Quiz instructions
│   ├── quiz.html       # Quiz page
│   ├── result.html     # Results page
│
├── static/             # CSS & JS
│   ├── style.css       # Styling
│   ├── script.js       # Quiz logic (frontend)
│
└── README.md           # Documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sakshi142004/quiz_project.git
cd quiz_project
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

Go to:

```
http://127.0.0.1:5000
```

---

## 📝 How the Penalty System Works

* Each correct → **+10 points**
* Each skip → **-2 points**
* Wrong answers have a **progressive penalty (percentage-based)**:

  ```
  1st wrong → 0 penalty
  2nd wrong → -2.5% of 10 = -0.25
  3rd wrong → -5% of 10 = -0.5
  4th wrong → -7.5% of 10 = -0.75
  ...
  ```
* If a student gives a **correct answer**, penalty resets to 0 again.

This ensures students are rewarded for accuracy while careless guessing gets punished.

---

## 📊 Pass/Fail Criteria

* If student gets **≥ 9 correct answers**, status = ✅ Pass
* Otherwise, ❌ Fail

---

## 🔧 Customization

You can easily change:

* **Number of questions** → edit `app.py`
* **Penalty values** → adjust logic in `app.py`
* **Pass criteria** → update minimum correct count in `app.py`
* **Design/theme** → modify `static/style.css`

---

## 💡 Future Improvements

* Add a **timer** for each quiz
* Store results in a database (SQLite/MySQL)
* Add an **admin panel** to add/remove questions
* Support **multiple quizzes**

---

✨ **Author**: Sakshi Bhatti
📌 Built for learning Flask + Web Development

