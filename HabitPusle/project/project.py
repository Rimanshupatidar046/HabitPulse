import csv
import os
import sys
from datetime import datetime, date
from tabulate import tabulate

DATA_FILE = "habits.csv"


def main():
    initialize_storage(DATA_FILE)
    while True:
        print("\n=== HabitPulse Tracker ===")
        print("1. Log Habit Completion")
        print("2. View All Habit Logs")
        print("3. View Habit Consistency Summary")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            habit_name = input("Enter habit name: ").strip()
            date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            status = input("Status (completed/missed): ").strip()

            valid, result = validate_habit_entry(habit_name, date_str, status)
            if valid:
                save_habit_log(DATA_FILE, result)
                print(f"Success: Habit '{result['habit']}' logged for {result['date']}.")
            else:
                print(f"Validation Error: {result}")

        elif choice == "2":
            records = read_habit_logs(DATA_FILE)
            if not records:
                print("No habit records found.")
            else:
                print(tabulate(records, headers="keys", tablefmt="grid"))

        elif choice == "3":
            records = read_habit_logs(DATA_FILE)
            if not records:
                print("No habit records found.")
            else:
                summary = calculate_habit_stats(records)
                table_rows = [
                    {
                        "Habit": h,
                        "Total Logged": data["total"],
                        "Completed": data["completed"],
                        "Success Rate (%)": f"{data['rate']:.1f}%",
                    }
                    for h, data in summary.items()
                ]
                print(tabulate(table_rows, headers="keys", tablefmt="grid"))

        elif choice == "4":
            print("Exiting HabitPulse. Keep building great habits!")
            sys.exit(0)
        else:
            print("Invalid option. Please choose between 1 and 4.")


def validate_habit_entry(habit: str, date_str: str, status: str):
    """Validates habit name, date format, and completion status."""
    cleaned_habit = habit.strip()
    if not cleaned_habit:
        return False, "Habit name cannot be empty."

    if not date_str:
        resolved_date = date.today().isoformat()
    else:
        try:
            parsed_date = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
            resolved_date = parsed_date.isoformat()
        except ValueError:
            return False, "Date must be formatted as YYYY-MM-DD."

    cleaned_status = status.strip().lower()
    if cleaned_status not in ["completed", "missed"]:
        return False, "Status must be either 'completed' or 'missed'."

    return True, {
        "habit": cleaned_habit.title(),
        "date": resolved_date,
        "status": cleaned_status,
    }


def calculate_habit_stats(records: list) -> dict:
    """Aggregates logged records to compute completion rates per habit."""
    stats = {}
    for row in records:
        habit = row.get("habit", "Unknown")
        status = row.get("status", "").strip().lower()

        if habit not in stats:
            stats[habit] = {"total": 0, "completed": 0, "rate": 0.0}

        stats[habit]["total"] += 1
        if status == "completed":
            stats[habit]["completed"] += 1

    for habit, data in stats.items():
        if data["total"] > 0:
            data["rate"] = round((data["completed"] / data["total"]) * 100, 2)

    return stats


def filter_logs_by_status(records: list, target_status: str) -> list:
    """Filters records by completion status ('completed' or 'missed')."""
    normalized = target_status.strip().lower()
    return [row for row in records if row.get("status", "").strip().lower() == normalized]


def initialize_storage(filename: str):
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["habit", "date", "status"])
            writer.writeheader()


def read_habit_logs(filename: str) -> list:
    if not os.path.exists(filename):
        return []
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_habit_log(filename: str, row: dict):
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["habit", "date", "status"])
        writer.writerow(row)


if __name__ == "__main__":
    main()
