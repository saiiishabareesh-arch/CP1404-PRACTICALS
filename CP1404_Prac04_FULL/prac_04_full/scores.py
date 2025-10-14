"""
CP1404 - Practical 04
Extension Task: scores.py
Fix the broken version so that we read per SUBJECT, not per STUDENT.
Then print each subject's list of 10 scores, plus max/min/average in a table.
"""

FILENAME = "scores.csv"


def main():
    subject_codes, subject_scores = load_scores(FILENAME)
    print_results(subject_codes, subject_scores)


def load_scores(filename):
    """Read CSV file and return (subject_codes, subject_scores_by_subject)."""
    with open(filename, "r", encoding="utf-8") as in_file:
        headers = in_file.readline().strip().split(",")
        student_rows = [list(map(int, line.strip().split(","))) for line in in_file if line.strip()]

    # Transpose rows -> columns (per subject)
    subject_scores = list(zip(*student_rows))
    return headers, subject_scores


def print_results(subjects, scores_by_subject):
    """Print a nicely formatted table of min, max, and average per subject."""
    print(f"{'Subject':<8} {'Scores':<45} {'Min':>5} {'Max':>5} {'Avg':>7}")
    print("-" * 75)
    for subject, scores in zip(subjects, scores_by_subject):
        scores_list = list(scores)
        min_score = min(scores_list)
        max_score = max(scores_list)
        avg_score = sum(scores_list) / len(scores_list)
        print(f"{subject:<8} {str(scores_list):<45} {min_score:>5} {max_score:>5} {avg_score:7.2f}")


if __name__ == "__main__":
    main()