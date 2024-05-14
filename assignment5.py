# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Ryan Seng, 5/13/2024, Assignment05
# ------------------------------------------------------------------------------------------ #


# This is the MENU users will be selecting from
MENU = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""

# This are the other constants
FILE_NAME: str = "Enrollments.csv"

# These are the variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file = None
menu_choice: str = ""
student_data: dict = []
students: list = []

# Defining Functions to call
# Registering a Student
def register_student():
    try:
        student_first_name = input("Please enter the student's first name: ")
        try:
            student_last_name = input("Please enter the student's last name: ")
            course_name = input("Please enter the course name: ")
            new_student = {
                "First_Name": student_first_name,
                "Last_Name": student_last_name,
                "Course": course_name
            }
            student_data.append(new_student)
            print(f"{student_first_name} {student_last_name} in {course_name} has been entered.")
        except Exception as error_details:
            print("There was an error entering the student's last name")
            print(f"Error: {error_details}")
    except Exception as error_details:
        print("There was an error entering the student's first name")
        print(f"Error: {error_details}")

# Printing Current Student Data
def print_data():
    print("The current list of students is:")
    print("Name \t\tLast Name \tCourse")
    for student in student_data:
        print(f"{student["First_Name"]} \t\t {student["Last_Name"]} \t\t{student["Course"]}")

# Saving Current Data
def save_data():
    try:
        file = open(FILE_NAME, "w")
        for student in student_data:
            file.write(f"{student["First_Name"]},{student["Last_Name"]},{student["Course"]}\n")
        file.close()
        print(f"The following list was saved in {FILE_NAME}:")
        for student in student_data:
            print(student)
    except Exception as error_details:
        print("There was an error entering saving the file")
        print(f"Error: {error_details}")

# Once the program starts, Enrollments.csv data is loaded in and the rest of the program runs
try:
    with open(FILE_NAME, 'r') as file:
        students = file.readlines()
        try:
            for user in students:
                cleaned_student_data = user.strip().split(",")
                student_dict = {
                    "First_Name": cleaned_student_data[0],
                    "Last_Name": cleaned_student_data[1],
                    "Course": cleaned_student_data[2]
                }
                student_data.append(student_dict)
            # A While loop that facilitates the Menu and according actions
            while True:
                print(MENU)
                menu_choice = input("Please select an option: ")
                match menu_choice:
                    case "1":
                        register_student()
                    case "2":
                        print_data()
                    case "3":
                        save_data()
                    case "4":
                        print("The program has ended.")
                        exit()
                    case _:
                        print("Please select only 1, 2, 3, or 4.")
        except ValueError:
            print(f"Error: There are corruption issues in {FILE_NAME}")
        except Exception as error_details:
            print(f"Error: {error_details}")
except FileNotFoundError:
    print("Error: File not found")
except ValueError:
    print(f"Error: There are corruption issues in {FILE_NAME}")
except Exception as error_details:
    print(f"Error: {error_details}")


