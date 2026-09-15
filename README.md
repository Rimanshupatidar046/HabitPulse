# HabitPulse ⚡
> A Command-Line Habit Tracker built in Python to log daily habits, track consistency streaks, and analyze productivity metrics.

This project was built and submitted as the **Final Project** for **CS50’s Introduction to Programming with Python (CS50P)**, administered by **Harvard University** through edX.

---

## 📜 Certification & Credential
- **Course:** CS50P (CS50's Introduction to Programming with Python)
- **Institution:** Harvard University
- **Instructor:** David J. Malan
- **Verified Certificate:** [View Harvard CS50P Certificate](https://certificates.cs50.io/3d794ff6-ed70-4206-89c8-059c0aa9ca77.pdf?size=letter)
- **Demo Video:** [Watch on YouTube](https://youtu.be/vuLtQQnACEs)

---

## 🚀 Overview
HabitPulse is designed to eliminate friction in daily habit management. Instead of relying on heavy GUI apps or web dashboards, it provides a lightweight, keyboard-first CLI tool for creating habits, updating completion states, monitoring active streaks, and persisting data locally via CSV storage.

---

## ✨ Features
- **Habit Creation & Categorization:** Add habits with daily goals and designated tracking categories.
- **Streak Calculation Engine:** Automatically checks logs against timestamps to calculate current and best streaks.
- **Data Persistence:** Uses formatted CSV file handling (`habits.csv`) so progress is saved across sessions.
- **Automated Testing Suite:** Built and tested with `pytest` (`test_project.py`) to validate core functions and error handling.

---

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.10+
- **Testing:** `pytest`
- **Libraries/Modules:** `csv`, `datetime`, `sys`, `tabulate` (or your requirements)

---

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Rimanshupatidar046/HabitPulse.git](https://github.com/Rimanshupatidar046/HabitPulse.git)
   cd HabitPulse '''

 2. Install dependencies:
  pip install -r requirements.txt

3. Run the application:
     python project.py

4. Run unit tests:
   pytest test_project.py
   
##Project Architecture

HabitPulse/
├── project.py          # Main entry point and core CLI logic
├── test_project.py     # Pytest unit tests for custom functions
├── habits.csv          # Local storage for habit data and logs
├── requirements.txt    # Project dependencies
└── README.md           # Documentation and credential overview

  ##Author
  Rimanshu Patidar
  GitHub: @Rimanshupatidar046
  
   
