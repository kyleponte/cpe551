# myModule.py
"""
Creates a CSV file (scores.csv) without importing any libraries
and defines myScores() to compute the average score per student.

Data columns: Name, Assignment, Homework, Project, Exam
"""

def create_csv():
    # Creates a CSV file named 'scores.csv'
    data = [
        "Name, Assignment, Homework, Project, Exam\n",
        "John, 91, 89, 88, 87\n",
        "Annie, 99, 95, 95, 93\n",
        "Joy, 92, 94, 91, 90\n"
    ]
    file = open("scores.csv", "w")
    for line in data:
        file.write(line)
    file.close()

def myScores():
    # Reads 'scores.csv' and returns a dictionary of name: average_score.
    with open("scores.csv", "r") as f:
        lines = f.readlines()

    scores = {}
    for i in range(1, len(lines)):
        parts = lines[i].strip().split(",")
        name = parts[0]
        numbers = list(map(int, parts[1:]))
        avg = sum(numbers) / len(numbers)
        scores[name] = avg
    return scores

# Create the CSV when module runs
create_csv()
