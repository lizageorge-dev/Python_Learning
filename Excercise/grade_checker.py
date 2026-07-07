# Grade checker
input_score = float(input("Enter the score: "))

if input_score >= 90:
    Grade = "A"
    print("Your grade is: A")
elif input_score >= 80:
    Grade = "B"
    print("Your grade is: B")
elif input_score >= 70:
    Grade = "C" 
    print("Your grade is: C")
else:
    Grade = "D"
    print("Your grade is: D")
if Grade in ["A", "B", "C"]:
    print("Congratulations! You passed the course.")
else:
    print("Sorry, you did not pass the course. Better luck next time!")