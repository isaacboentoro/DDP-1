# Lab 00 - Programming Foundations 1 International Class 2023
# Name: Isaac Jesse Boentoro
# Student ID: 2306256362
# ==================== START OF THE PROGRAM ====================
# Welcome message using print(), separated using \n.
print("Hello! Welcome to Lab 00 for Programming Foundations 1!""\n")

print("Please record your attendance by entering your name, student ID,and your UI e-mail down below.")

# Get user input using input() and store to variables name, studentId and email

name = input("Name: ")

studentId = input("Student ID: ")

email = input("UI E-mail: ")

#Get additional info before displaying final message using the same method
print("Please feel free to add more info about yourself that you'd like to include!")
hobby = input("Hobby: ")

address = input("Address: ")


print("\nPlease write 1 (one) word that describes programming for you!")
answer = input()

print(f"Attendance recorded for student {name} with student ID {studentId} and e-mail {email}. \n {name} also has a hobby which is  {hobby}, and lives at {address}!\n ")
print("Thank you for coming to today's lab session. See you next week!")
# ==================== END OF THE PROGRAM ====================