# -------------------------------------------------------------------------- #
# Title: Assignment07
# Desc: This assignment demonstrates using instance & class methods
# and the use of version control via GitHub
# Change Log: (Who, When, What)
#   Jeremy Peters, 11/20/2024, Reused code from Assignment06 as base
#   Jeremy Peters, 11/21/2024, Aligning code to assignment requirements
#   Jeremy Peters, 11/23/2024, Additional changes to fix JSON iteration
#   Jeremy Peters, 11/24/2024, Fix to JSON iteration on read & write. Also
#  added docstrings throughout with some help from genAI.
#   Jeremy Peters, 12/01/2024, Formatting changes and final commit
# -------------------------------------------------------------------------- #
import os
import json
from colorama import Fore, Style

# Define the Data Constants
MENU: str = """
---- Course Registration Program --------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str = str()
students: list = list()
student_first_name: str = str()
student_last_name: str = str()
course_name: str = str()
file_status: bool = False

class Person:
    """
    A class that represents a person.

    Attributes:
    __first_name (str): The first name of the person.
    __last_name (str): The last name of the person.

    Methods:
    __init__(first_name, last_name): Initializes the person with a first
    and last name.
    first_name: Gets and sets the first name.
    last_name: Gets and sets the last name.
    __str__(): Returns a string representation of the person.
    """
    __first_name: str = str()
    __last_name: str = str()

    def __init__(self, first_name: str, last_name: str):
        """
        Initializes the person with a first and last name.
        """
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self) -> str:
        """
        Gets the first name.
        """
        return self.__first_name.title().strip()

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """
        Sets the first name.
        """
        if (not first_name.isalpha()) or first_name == "":
            raise ValueError(CustomMessage.alpha_only)
        else:
            self.__first_name = first_name

    @property
    def last_name(self) -> str:
        """
        Gets the last name.
        """
        return self.__last_name.title().strip()

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """
        Sets the last name.
        """
        if (not last_name.isalpha()) or last_name == "":
            raise ValueError(CustomMessage.alpha_only)
        else:
            self.__last_name = last_name

    def __str__(self):
        """
        Returns a string representation of the person.
        """
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    """
    A class that represents a student, inheriting from Person.

    Attributes:
    __course_name (str): The course name the student is enrolled in.

    Methods:
    __init__(first_name, last_name, course_name): Initializes the student
    with a first name, last name, and course name.
    course_name: Gets and sets the course name.
    __str__(): Returns a string representation of the student.
    convert_to_dict(): Converts the student object to a dictionary.
    convert_from_dict(data): Creates a student object from a dictionary.
    """
    __course_name: str = str()

    def __init__(self, first_name: str, last_name: str, course_name: str):
        """
        Initializes the student with a first name, last name, and course name.
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.__course_name = course_name

    @property
    def course_name(self) -> str:
        """
        Gets the course name.
        """
        return self.__course_name.title().strip()

    @course_name.setter
    def course_name(self, course_name: str) -> None:
        """
        Sets the course name.
        """
        if course_name == "":
            raise ValueError(CustomMessage.no_data)
        else:
            self.__course_name = course_name

    def __str__(self) -> str:
        """
        Returns a string representation of the student.
        """
        return f"{self.first_name} {self.last_name} {self.course_name}"

    def convert_to_dict(self) -> dict:
        """
        Converts the student object to a dictionary.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "course_name": self.course_name
        }

    @classmethod
    def convert_from_dict(cls, data: dict):
        """
        Creates a student object from a dictionary.
        """
        return cls(first_name=data["first_name"], last_name=data[
            "last_name"], course_name=data["course_name"])

class CustomMessage:
    """
    A class for storing reusable messages.

    Attributes:
    menu_prompt (str): The menu prompt message.
    file_exists (str): Message indicating that the file already exists.
    no_file_create_it (str): Message indicating that no file exists
     and one will be created.
    prompt_firstname (str): Prompt message for the first name.
    prompt_lastname (str): Prompt message for the last name.
    prompt_coursename (str): Prompt message for the course name.
    no_data (str): Message indicating no data entered.
    alpha_only (str): Message indicating name should only contain
     alphabetic characters.
    ascii_only (str): Message indicating course name should only
     contain ASCII characters.
    valid_choices (str): Message indicating invalid choice.
    registered_students (str): Message indicating registered students.
    read_file_error (str): Message indicating error reading file.
    """
    menu_prompt: str = (
            Fore.LIGHTYELLOW_EX + f"What would you like to do: \
" + Style.RESET_ALL)
    file_exists: str = (Fore.LIGHTYELLOW_EX + f"File {FILE_NAME} already \
exists. Skipping file creation." + Style.RESET_ALL)
    no_file_create_it: str = (Fore.LIGHTYELLOW_EX + f"No existing file \
{FILE_NAME} found. File will be created." + Style.RESET_ALL)
    prompt_firstname: str = (Fore.LIGHTYELLOW_EX + f"Please enter the \
student's first name: " + Style.RESET_ALL)
    prompt_lastname: str = (Fore.LIGHTYELLOW_EX + f"Please enter the \
student's last name: " + Style.RESET_ALL)
    prompt_coursename: str = (Fore.LIGHTYELLOW_EX + f"Please enter the \
course name: " + Style.RESET_ALL)
    no_data: str = (Fore.LIGHTCYAN_EX + f"You have not entered any \
data.\nTry starting with starting option 1." + Style.RESET_ALL)
    alpha_only: str = (Fore.LIGHTCYAN_EX + f"Student name should only \
contain alphabetic characters." + Style.RESET_ALL)
    ascii_only: str = (Fore.LIGHTCYAN_EX + f"Course name should only \
contain ASCII characters." + Style.RESET_ALL)
    valid_choices: str = (Fore.LIGHTCYAN_EX + f"Invalid choice. Please \
try again." + Style.RESET_ALL)
    registered_students: str = (Fore.MAGENTA + f"The following students \
are registered:" + Style.RESET_ALL)
    read_file_error: str = (Fore.RED + f"Error reading contents of \
{FILE_NAME}." + Style.RESET_ALL)


class FileProcessor:
    """
    A collection of functions for processing files.

    Methods:
    file_check(): Checks that the file exists, and if it isn't present,
     it creates an empty file.
    read_data_from_file(file_name, student_data): Reads data from a file
     into a list of students.
    write_data_to_file(file_name, student_data): Writes the list of
     students to a file.
    """

    @staticmethod
    def file_check():
        """
        Checks that the file exists, and if it isn't present,
        it creates an empty file.
        """
        try:
            print(Fore.MAGENTA + f"Checking for existing file \
{FILE_NAME}..." + Style.RESET_ALL)
            if (not os.path.exists(FILE_NAME)) or (os.path.getsize(
                    FILE_NAME) == 0):
                print(CustomMessage.no_file_create_it)
                with open(FILE_NAME, "w") as file:
                    file.write("[]")
            else:
                print(CustomMessage.file_exists)
        finally:
            pass

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads data from a file into a list of students.

        :param file_name: The name of the file.
        :param student_data: The list of students.
        :return: The list of students.
        """
        global file_status
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                if isinstance(data, list) and data:
                    for student_dict in data:
                        student = Student.convert_from_dict(student_dict)
                        student_data.append(student)
                    file_status = True
        except Exception as e:
            IO.output_error_messages(
                message=CustomMessage.read_file_error, error=e
            )
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes the list of students to a file.

        :param file_name: The name of the file.
        :param student_data: The list of students.
        """
        try:
            with open(file_name, "w") as file:
                json_data = [
                    student.convert_to_dict() for student in student_data
                ]
                json.dump(json_data, file)
                print(Fore.LIGHTYELLOW_EX + f"The following was saved \
to file:" + Style.RESET_ALL)
                IO.output_student_courses(student_data=student_data)
        except ValueError as e:
            IO.output_error_messages(e.__str__())
        except Exception as e:
            IO.output_error_messages(e.__str__())

class IO:
    """
    A collection of functions for receiving and storing user data.

    Methods:
    output_error_messages(message, error): Handles error messages.
    output_menu(menu): Presents the menu to the user.
    input_menu_choice(): Handles the user menu input.
    input_student_data(student_data): Handles user input for student data.
    output_student_courses(student_data): Prints the student's courses.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Handles error messages.

        :param message: The message data passed to the function.
        :param error: The exception data passed to the function.
        """
        print(message)
        if error is not None:
            print(Fore.LIGHTRED_EX + "-- Error Message -- ")
            print(error, error.__doc__, type(error), sep="\n" +
                                                         Style.RESET_ALL)
        elif error == ValueError:
            print(Fore.RED + f"-- Error -- " + Style.RESET_ALL)
            print(Fore.RED + error.__str__() + Style.RESET_ALL)

    @staticmethod
    def output_menu(menu: str):
        """
        Presents the menu to the user.

        :param menu: The menu to display.
        """
        print(Fore.MAGENTA + menu + Style.RESET_ALL)

    @staticmethod
    def input_menu_choice():
        """
        Handles the user menu input.

        :return: The menu choice selected by the user.
        """
        try:
            choice = input(CustomMessage.menu_prompt)
            if choice not in ("1", "2", "3", "4"):
                raise Exception(CustomMessage.valid_choices)
            return choice
        except Exception as e:
            IO.output_error_messages(e.__str__())
            return None

    @staticmethod
    def input_student_data(student_data: list):
        """
        Handles user input for student data.

        :param student_data: The list of students.
        """
        try:
            while True:
                try:
                    student_first_name = input(CustomMessage.prompt_firstname)
                    if not student_first_name.isalpha():
                        raise ValueError(CustomMessage.alpha_only)
                    student_first_name = student_first_name
                    break
                except ValueError as e:
                    IO.output_error_messages(e.__str__())

            while True:
                try:
                    student_last_name = input(CustomMessage.prompt_lastname)
                    if not student_last_name.isalpha():
                        raise ValueError(CustomMessage.alpha_only)
                    student_last_name = student_last_name
                    break
                except ValueError as e:
                    IO.output_error_messages(e.__str__())

            while True:
                try:
                    course_name = input(CustomMessage.prompt_coursename)
                    if not course_name.isascii():
                        raise ValueError(CustomMessage.ascii_only)
                    course_name = course_name
                    break
                except ValueError as e:
                    IO.output_error_messages(e.__str__())

            student = Student(
                student_first_name, student_last_name, course_name
            )
            student_data.append(student)
            print(Fore.MAGENTA + f"You have added {student.first_name} \
{student.last_name} for course {student.course_name} to the registration \
list." + Style.RESET_ALL)
        except Exception as e:
            IO.output_error_messages(message=Fore.RED + f"There was a \
non-specific error!\n" + Style.RESET_ALL, error=e)

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Prints the student's courses.

        :param student_data: The list of students.
        """
        try:
            if not student_data:
                raise ValueError(CustomMessage.no_data)
            for student in student_data:
                print(Fore.MAGENTA + f"{student.first_name} \
{student.last_name} is enrolled in {student.course_name}" + Style.RESET_ALL)
        except ValueError as e:
            IO.output_error_messages(e.__str__())

# Check if file exists and if not, create empty file
FileProcessor.file_check()

# Load the students variable with data from JSON, if present
FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    # Present menu to user
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        IO.input_student_data(students)
        continue

    # Present the current data
    elif menu_choice == "2":
        if students or file_status:
            IO.output_student_courses(students)
        else:
            print(CustomMessage.no_data)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        if students or file_status:
            FileProcessor.write_data_to_file(
                file_name=FILE_NAME, student_data=students
            )
        else:
            print(CustomMessage.no_data)
        continue

    # Stop the loop and exit the program
    elif menu_choice == "4":
        print("Program closed successfully")
        exit()
