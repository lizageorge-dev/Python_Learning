# This program calculates the sum of even numbers from 1 to 50
sum=0
for i in range(1, 51):
    if i % 2 == 0:
        sum+= i
print(sum)

#same program using while loop
sum=0
i=1
while i <= 50:
    if i % 2 == 0:
        sum+= i
    i+=1
print(sum)