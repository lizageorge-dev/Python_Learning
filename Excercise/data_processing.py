try:
    def get_average_grade(grades_tuple):
        if not grades_tuple:
            return 0
        return sum(grades_tuple) / len(grades_tuple)
except TypeError:
    print("Error: Please enter a valid tuple of numbers.")
course_grades={"Math": (80, 85, 90), "Science": (75, 80, 85), "IT": (70, 75, 80)}
try:
    for subject, grades in course_grades.items():
        average = get_average_grade(grades)
        print(f"{subject}: {average}")
except Exception as e:
    print(f"Error: {e}")
