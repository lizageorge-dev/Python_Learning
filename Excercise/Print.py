import time
"""
print("Hello, Python!")
print("Liza is learning Python.")
"""
"""
print("Programming", "Essentials", "in", sep="***",end="...")
print("Python")
"""
"""
print()
print('Hello, World!')
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
"""
"""
print("        *        "*2)
"""
"""
print(27)
print(89.1)
print(True>False)
print(2+2)
print(6//2)
"""
"""
name="Liza"
age=32
hieght=6
print("My name is ",name,". I am ",age," years old. My height is ",hieght," feet.",sep="")
name=input("What is your name? ")
print("Hello, ",name,"!",sep="")
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
"""
"""
print(" "*2+"*")
print("*"+" "*2+"*")
print("*"+" "*3)
print("*"*2)
print("*")

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)
######################################
income=float(input("Enter your income: "))
if income < 85528:
    tax=round(income*0.18-556.02)
else:
    tax=round(14839.02+(income-85528)*0.32)
print("The tax is:",tax)
  year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,"is a leap year.")
else:    print(year,"is not a leap year.")  
######################################################
Age=int(input("Enter your age: "))
if Age<18:
    print("Access denied.Too young.")
elif (Age>=18 and Age<=20):
    print("You can come in, but no drinking!.")
elif Age>=20 :
    print("Welcome in! Enjoy your night.")
#######################################################
    age = int(input())
print("Your age is ", age, ".", sep="")
for i in range(1, 10,2):
    print(i)
    ######################################################
    for i in range(1, 7):
    if i<=5:
        time.sleep(1)
        print(str(i)+" Mississippi")
     
    elif i==6:
        print("Ready or not, here I come!")
        #break
for i in range(1, 10):
    if i==5:
        break
    print("inside the loop:",i)
print("outside the loop")   

#Continue
for i in range(1, 10):
    if i==5:
        continue
    print("inside the loop:",i)
print("outside the loop") 
while True:
    word=input("Enter the magic password ")
    if word=="chupacabra":
        print("You've successfully left the loop.")
        break
        
    else:
        print("Ha ha! You're stuck in the loop!") 
        user_input=input("Enter a word: ")
word=""
for letter in user_input:
    if letter in "aeiou":
        continue
    else:
        word=word+letter
print(word)
"""
"""
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
    #######################
    for i in range(5):
    print(i)
else:
    print("else:", i)
    i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
    ##############blocks = int(input())

height = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1

print(height)
#Collatz's Hypothesis
number = int(input("Enter a number: "))
count = 0
while number != 1:
    count += 1
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number, end=" ")
print("\nSteps:", count)

#Create a for loop that counts from 0 to 10, and prints odd numbers to the screen
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
#######################################
        word=""
for digit in "0165031806510":
    if digit == "0":
        word=word+"x"
    else:
        word=word+digit
print(word)
##############################################
numbers = [1, 2, 3, 4, 5]
user_input = int(input("Enter a number: "))
list_len=len(numbers)
middle_index=list_len//2
numbers[middle_index] = user_input
print(numbers)
numbers.remove(len(numbers)-1)
print(numbers)
beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")    
beatles.append("George Harrison")
for i in range(1, 3):
    name=input("Enter the name of a beatle: ")
    beatles.append(name)
beatles.remove("Stu Sutcliffe")
beatles.remove("Pete Best")
beatles.insert(0,"Ringo Starr")

print(beatles)
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
bool=True
while bool:
    bool=False
    print(bool)
for i in range(len(my_list)-1):
    print("I",i)
    for j in range(i+1,len(my_list)-1):
            print("j",j)       
            if(j!=len(my_list)):
             print("my_list[i]",my_list[i]) 
             print("my_list[j]",my_list[j])      
             print("len(my_list)",len(my_list))
             if my_list[i] == my_list[j]:
                print("removed",my_list[i])
                print("my_list length",len(my_list))
                bool=True
                my_list.remove(my_list[i]) 
                print(my_list)
print(my_list)
###################################
num_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
multiples_of_3=[]
for i in num_list:
    if i%3==0:
        multiples_of_3.append(i)
print(multiples_of_3)
 
       """
"""
password=input("Enter a password: ")
counter=1

while password!="python123":
    if counter==3:
        print("Account locked! Try again later.")
        break
    print("Access denied! Try again.")
    counter+=1
    password=input("Enter a password: ")
if password=="python123":
    print("Access granted!")
    #######################
    READ = 4
WRITE = 2
EXECUTE = 1

user_permissions =4 # 10 in binary

if user_permissions & WRITE:
    print("WRITE permission is enabled")
else:
    print("WRITE permission is NOT enabled")
    

"""
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])


















