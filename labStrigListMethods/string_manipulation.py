user_input = input("Enter a sentence: ")
print("Original:", user_input)
print("Uppercase:", user_input.upper())
print("Reverse:", user_input[::-1])
revers_sentence = user_input.split()[::-1]
print("Reversed Words:", ' '.join(revers_sentence))
print("space replaced", user_input.replace(" ", "_"))
count =0
#count vowels
for i in range(len(user_input)):
    if user_input[i]=='a' or user_input[i]=='e' or user_input[i]=='i'or user_input[i]=='o'or user_input[i]=='u':
        count+=1
        print(f"Character: {user_input[i]}, Position: {i}")
print("count of vowels",count)
