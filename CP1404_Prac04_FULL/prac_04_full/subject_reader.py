"""
CP1404/CP5632 Practical
File: subject_reader.py
Read subject data from subject_data.txt and display details.
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename):
    """Read file and return a list of [code, lecturer, student_count:int]."""
    subjects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            code, lecturer, students_str = parts
            try:
                students = int(students_str)
            except ValueError:
                continue
            subjects.append([code, lecturer, students])
    return subjects


def display_subjects(subjects):
    """Print: CODE is taught by LECTURER and has N students"""
    for code, lecturer, students in subjects:
        print(f"{code} is taught by {lecturer} and has {students} students")


if __name__ == "__main__":
    main()