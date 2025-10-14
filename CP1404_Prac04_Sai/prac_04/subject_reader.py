"""
CP1404 - Practical 04
File: subject_reader.py
- Load subject data from a CSV-like text file (code, lecturer, students)
- Return as a list of [code, lecturer, students:int]
- Display details in a friendly format
"""
FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename: str) -> list[list]:
    """
    Read the given file and return a list of [code, lecturer, students:int].
    Each line is CSV with 3 values.
    """
    subjects: list[list] = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) != 3:
                # Ignore malformed lines gracefully
                continue
            code, lecturer, students_str = parts
            try:
                students = int(students_str)
            except ValueError:
                # Skip if student count is not an int
                continue
            subjects.append([code, lecturer, students])
    return subjects


def display_subjects(subjects: list[list]) -> None:
    """Print: CODE is taught by LECTURER and has N students"""
    for code, lecturer, students in subjects:
        print(f"{code} is taught by {lecturer} and has {students} students")


if __name__ == "__main__":
    main()