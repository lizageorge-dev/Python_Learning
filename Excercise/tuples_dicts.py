try:
    months=("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
    print(months[0],months[-1])
    months[0]="newmonth"
except IndexError:
    print("Error: Index out of range.")
except TypeError:
    print("Error: Tuples are immutable.")
students={"Alice": 80, "Bob": 90, "Charlie": 78}
students["David"]= 85
students["Alice"]=85
for name, grade in students.items():
    print(f"{name}: {grade}")