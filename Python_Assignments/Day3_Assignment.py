university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

# Q1: Print all student names and their majors
print("Q1: Student Names and Majors")
for student in university_data.values():
    print(f"{student['name']} - {student['major']}")
print()

# Q2: Average score per course per student
print("Q2: Average Score per Course per Student")
for sid, student in university_data.items():
    print(f"{student['name']}:")
    for course, scores in student["courses"].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course}: {avg:.2f}")
print()

# Q3: Find students who scored >90 in final of Python101
print("Q3: Students who scored >90 in final of Python101")
for student in university_data.values():
    python = student["courses"].get("Python101")
    if python and python["final"] > 90:
        print(f"{student['name']}")
print()

# Q4: Add new course AI101 for student S101
print("Q4: Adding AI101 for S101")
university_data["S101"]["courses"]["AI101"] = {"midterm": 90, "final": 95, "project": 92}
print(f"S101 Courses after adding AI101: {university_data['S101']['courses']}")
print()

# Q5: Print average for each course (across all students)
print("Q5: Average for Each Course")
course_totals = {}
course_counts = {}

for student in university_data.values():
    for course, scores in student["courses"].items():
        if course not in course_totals:
            course_totals[course] = {"midterm": 0, "final": 0, "project": 0}
            course_counts[course] = 0
        for key in scores:
            course_totals[course][key] += scores[key]
        course_counts[course] += 1

for course, total_scores in course_totals.items():
    count = course_counts[course]
    avg_score = sum(total_scores.values()) / (3 * count)
    print(f"{course}: {avg_score:.2f}")