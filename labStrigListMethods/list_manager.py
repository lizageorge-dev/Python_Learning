num_list=[]

def main():
    while True:
     choice=menu()
     print("choice",choice)
     if choice == 1:
        print("add ")
        addnumber()
     elif (choice==2):
        remove_num()
     elif (choice==3):
        display_list()
     elif (choice==4):
       print("Bye")
       break
     else:
        print("invalid choice")
    
def addnumber():
    try:
        number=int(input("Enter an intger number"))
        num_list.append(number)
        print("num_list")
    except ValueError:
        print("Invalid input. Please enter an integer.")
def remove_num():
    try:
        index=int(input("Enter the index of the number to be removed"))
        num_list.pop(index) 
        print("Updated list",num_list)  
    except IndexError:
        print("Invalid index. Please enter a valid index.")
def display_list():
   print("List is", num_list)

def menu():
    print("\n1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")
    return int(input("Enter your choice: "))
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age must be a positive integer")
    return age

def main():
    while True:
        choice = menu()
        print("choice", choice)
        if choice == 1:
            print("add ")
            addnumber()
        elif choice == 2:
            remove_num()
        elif choice == 3:
            display_list()
        elif choice == 4:
            print("Bye")
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()
