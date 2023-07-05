
sum = 0
count = 0
while True:
    num_input = int(input("Please enter a number: ")) # accept a number from the user
    if num_input == -1:
        break
    sum += num_input
    count += 1
    
if count > 0:
    average = sum/count
    print("The average is: ", average)
    
else:
    print("You have not entered a number!")