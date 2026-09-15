import pytest
from project import validate_habit_entry, calculate_habit_stats, filter_logs_by_status


def test_validate_habit_entry_valid():
    valid, data = validate_habit_entry("reading", "2026-03-15", "completed")
    assert valid is True
    assert data["habit"] == "Reading"
    assert data["date"] == "2026-03-15"
    assert data["status"] == "completed"


def test_validate_habit_entry_invalid():
    # Empty habit name
    valid, err = validate_habit_entry("", "2026-03-15", "completed")
    assert valid is False
    assert err == "Habit name cannot be empty."

    # Invalid date pattern
    valid, err = validate_habit_entry("Workout", "15-03-2026", "completed")
    assert valid is False
    assert err == "Date must be formatted as YYYY-MM-DD."

    # Invalid status
    valid, err = validate_habit_entry("Workout", "2026-03-15", "done")
    assert valid is False
    assert "Status must be either" in err


def test_calculate_habit_stats():
    sample_records = [
        {"habit": "Running", "date": "2026-03-10", "status": "completed"},
        {"habit": "Running", "date": "2026-03-11", "status": "missed"},
        {"habit": "Reading", "date": "2026-03-10", "status": "completed"},
    ]
    stats = calculate_habit_stats(sample_records)
    assert stats["Running"]["total"] == 2
    assert stats["Running"]["completed"] == 1
    assert stats["Running"]["rate"] == 50.0

    assert stats["Reading"]["total"] == 1
    assert stats["Reading"]["completed"] == 1
    assert stats["Reading"]["rate"] == 100.0

    # Empty records
    assert calculate_habit_stats([]) == {}


def test_filter_logs_by_status():
    sample_records = [
        {"habit": "Gym", "date": "2026-03-01", "status": "completed"},
        {"habit": "Gym", "date": "2026-03-02", "status": "missed"},
        {"habit": "Meditation", "date": "2026-03-01", "status": "completed"},
    ]
    completed_only = filter_logs_by_status(sample_records, "completed")
    assert len(completed_only) == 2

    missed_only = filter_logs_by_status(sample_records, "missed")
    assert len(missed_only) == 1
    assert missed_only[0]["habit"] == "Gym"

    none_found = filter_logs_by_status(sample_records, "pending")
    assert len(none_found) == 0
