# HabitPulse – Terminal Habit Tracker & Consistency Analyzer
#### Video Demo:  https://youtu.be/vuLtQQnACEs
#### Description:

HabitPulse is a comprehensive, command-line habit tracking and consistency analysis tool written entirely in Python. Personal productivity and behavioral change depend heavily on the ability to monitor consistency across daily routines. Traditional habit-tracking applications often present significant friction: they demand account registrations, require active internet connections, display intrusive advertisements, and store personal behavioral data on remote cloud platforms. HabitPulse was developed to solve this problem by offering an offline, local-first, lightweight terminal application that provides transparent storage, structured tracking, and statistical analysis directly within the developer's shell environment.

#### Project Structure and File Breakdown

The architecture of HabitPulse is designed to strictly follow clean code practices, modular decomposition, and the testing specifications mandated by the CS50's Introduction to Programming with Python course:
- **`project.py`**: This serves as the primary script and executable entry point of the entire application. It contains the interactive command-line loop inside `main()`, guiding the user through distinct menus: logging new habits, viewing entire logs in grid tables, inspecting success rates, and exiting gracefully. Beyond the main execution loop, `project.py` defines three primary standalone custom functions—`validate_habit_entry`, `calculate_habit_stats`, and `filter_logs_by_status`—as well as helper utilities for handling persistence through Python's standard `csv` module (`initialize_storage`, `read_habit_logs`, and `save_habit_log`).
- **`test_project.py`**: This module contains automated test suites designed for execution under `pytest`. It tests edge cases thoroughly, verifying that invalid date strings, incorrect status flags, and blank habit names are rejected gracefully with helpful feedback. It also verifies statistical precision by running calculations against mock data dictionaries, ensuring that rates and record filters operate independently of actual disk storage.
- **`requirements.txt`**: Lists all external third-party dependencies required to execute the program. HabitPulse uses `tabulate` to produce structured ASCII tables and `pytest` for executing automated test suites.
- **`habits.csv`**: The local persistent storage file automatically initialized upon the first run of the script. It uses standard comma-separated columns (`habit`, `date`, and `status`) to retain all logged routines across terminal sessions.

#### Core Custom Functions Explained

1. `validate_habit_entry(habit, date_str, status)`: This function guarantees data integrity before any write operation is committed to disk. It normalizes text case, verifies that habit descriptions are non-empty, checks that supplied dates adhere strictly to ISO 8601 formatting (`YYYY-MM-DD`), and ensures that completion states match either `completed` or `missed`. If no date is supplied by the user, it automatically resolves to today's local system date.
2. `calculate_habit_stats(records)`: This function processes lists of log entries to generate aggregated analytical insights. It groups logs by habit name, computes total attempts alongside successful completions, and derives an overall percentage completion rate rounded to two decimal places.
3. `filter_logs_by_status(records, target_status)`: A deterministic filtering utility that parses raw record lists and isolates records matching a specific state (`completed` versus `missed`), enabling focused tracking of slip-ups or accomplishments.

#### Design Choices and Trade-offs

During development, several architectural choices were evaluated:

- **CSV Storage vs SQLite Database**: While an SQLite database provides relational constraints and indexing capabilities, a standard delimited CSV file was intentionally selected. CSV files ensure complete data portability, allowing users to open, inspect, or export their habit logs directly into spreadsheet suites like Microsoft Excel, LibreOffice Calc, or Google Sheets without running secondary migration tools.
- **Decoupled Logic for Testability**: Functions handling mathematical aggregations and data validation were deliberately built as pure functions. By avoiding direct calls to `input()`, `print()`, or file operations inside these three core functions, they can be tested deterministically in `test_project.py` without mocking disk I/O or terminal streams.
- **Graceful Error Handling**: Rather than allowing date parsing or format issues to crash the interpreter with unhandled exceptions, all inputs are sanitized through explicit `try-except` blocks, returning descriptive status tuples that provide actionable error prompts back to the terminal user.
