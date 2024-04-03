#Student_Ethnicites.py
#Created on 4/4/24
#Author: Rain Jones

students_ethnicities = {"NZ European": ["Rain", "Mary"]}


def option_one(user_addition, added_ethnicity):
    user_addition = input("Who would you like to add?")
    added_ethnicity = input("What is their ethnicity?")
    return user_addition, added_ethnicity


print("Hello. Welcome to the student ethnicity database.")
print("There are some options you can choose from.")
print("""1. Add a student
2. Remove a student
3. Edit a student's ethnicity
4. Edit a student's name
5. list all ethnicities
6. Find every student under an ethnicity
7. Find a student's ethnicity using their name""")
try:
    choice = int(input("Please choose an option: "))
except ValueError:
    print("TRY AGAIN, MOTHERFUCKER")
