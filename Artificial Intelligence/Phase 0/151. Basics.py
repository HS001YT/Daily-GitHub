# Task: Marks Processing System

# Requirements:
# Take input: Number of subjects n

# Using a for loop: Take marks of each subject, Add them to total

# Calculate average marks
# Using if–else, print: Pass if average ≥ 40, Fail otherwise


# Solution:

n = int(input("Enter number of subjects: "))

total = 0
for i in range(1, n+1):
    print("Enter marks for subject[%d]" % i, end=": ")
    # print("Enter marks for subject[{0:1d}]" .format(i), end=": ")
    marks = int(input())
    total += marks

print("Your Average score is: ", total/n)
if ((total/n) >= 40):
    print("Pass!!")
else:
    print("Fail!!")