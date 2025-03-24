"""

Author: Helen Brazier
Date Written: 03/23/25
Program: gpa.py
Assignment: Module 2 Lab
Description: Program accepts student names and GPAs, checking if they qualify for Dean's List or Honor Roll

"""

QUIT = "ZZZ" # Provide an exit from the loop

last_name = input("Enter student's last name or enter 'ZZZ' to quit:") # variable to store the input of students last name

while last_name != QUIT: # enter loop
    first_name = input("Enter student's first name: ")  # variable to store the input of students first name
    gpa = float(input("Enter student's GPA: ")) # store the sutdent GPA in variable
    if gpa >= 3.5: # check if GPA qualifies for Dean's List and print confirmation
        print(f"{first_name} {last_name} has made the Dean's List")
    elif gpa >= 3.25: # check if GPA qualifies for Honor Roll and print confirmation
        print(f"{first_name} {last_name} has made the Honor Roll")
    else: # print exception if student does not qualify for either
        print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll")
    last_name = input("\nEnter student's last name or enter 'ZZZ' to quit: ") # continue loop
