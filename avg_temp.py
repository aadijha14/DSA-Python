from array import *
arr1 = array('f', [])
days = int(input("Enter the number of days: "))
for i in range(days):
    temp = float(input(f"enter the temp for day {i + 1}: "))
    arr1.append(temp)
avg_temp = sum(arr1) / len(arr1)
print(f"The average temperature for {days} days is: {avg_temp:.2f}")

for i in arr1:
    if i > avg_temp:
        print(f"{i} is above average")
    elif i < avg_temp:
        print(f"{i} is below average")
    else:
        print(f"{i} is equal to the average")