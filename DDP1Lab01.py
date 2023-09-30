# Name: Isaac Jesse Boentoro
# NPM:2306256362
# TA Code: HEZ
# Take input for Student's First and Last Name
name = input("Enter name: ").upper().title()
# Take input for three exams
exam1 = int(input("Enter the score for Exam 1: "))
exam2 = int(input("Enter the score for Exam 2: "))
exam3 = int(input("Enter the score for Exam 3: "))


# Calculate the average and total grade
average_exam = (exam1 + exam2 + exam3 )/3
average_exam = round(average_exam, 2)
total_exam = (exam1 + exam2 + exam3)
# Take the total seconds as input
total_seconds = int(input("Enter the total seconds taken for the exams: "))
# Calculate the hours, minutes, and remaining seconds
# Use the operators // and %
#Using // gives us a number of whole hours (3600 seconds in an hour)
hours = int(total_seconds // 3600) #Get amount of hours from x amount of seconds while also rounding downa
minutes = int((total_seconds %3600 ) / 60) #Take the remainder of the previous operation then divide by 60
seconds = int(total_seconds % 60) #Get remaining seconds left

# Format and print the feedback messages
# Your code here
print(f"--- {name} ---")
print(f"Exam Scores: {exam1} , {exam2} ,{exam3}")
print(f"Total Score: {total_exam}")
print(f"Average Score: {average_exam}")
print(f"Time Taken: {hours} hours {minutes} minutes {seconds} seconds\n")
#Display overview before final "message" using f-strings 
#Also separates the "message" with a newline argument on the previous print statement

print(f"--- Message for {name} ---")
print(f"Hey, {name}. You got exam scores of {exam1}, {exam2}, {exam3}, with total of {total_exam} \
and an average of {average_exam}. The total time taken is {hours} hours, {minutes} minutes, {seconds} seconds.")
#Backstring for better print statement readability


