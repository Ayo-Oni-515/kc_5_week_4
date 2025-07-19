import os
import json
import sys
import time

from student import Student


def add_student() -> None:
    print()
    while True:
        try:
            student_name: str = (
                input("Enter student's name: ")).lower()
            
            if not student_name.isascii():
                raise TypeError
            elif student_name in load_from_json().keys():
                raise NameError
            elif student_name in Student.In_memory:
                raise ValueError
            break
        except TypeError:
            print("\n\t\tError: Invalid student name syntax!\n")
        except NameError:
            print(
                "\n\t\tError: Student record exists in json file!\n")
        except ValueError:
            print("\n\t\tError: Student has already been added!\n")
    
    while True:
        try:
            subject_number: int = int(input(
                "\nEnter number of subjects to record (10 subjects max): "))
            print()

            if not subject_number.is_integer():
                raise TypeError
            elif subject_number > 10:
                raise ValueError
            break
        except TypeError:
            print("\n\t\tError: Invalid subject count syntax!\n")
        except ValueError:
            print("\n\t\tError: Subject threshold too high!\n")
    
    subjects: dict = {}
        
    for i in range(subject_number):
        pos: dict = {1: "st", 2: "nd", 3: "rd", 4: "th", 5: "th", 6: "th",
                     7: "th", 8: "th", 9: "th", 10: "th"}
        
        while True:
            try:
                subject_name: str = (input(f"Enter {i+1}{pos[i+1]} \
subject's title: ")).lower()

                if not subject_name.isalnum():
                    raise ValueError
                break
            except ValueError:
                print("\n\t\tError: Invalid subject title entered!\n")

        while True:
            try:
                subject_score: float = float(input("Enter score: "))

                if (
                    subject_score <= 0
                    or subject_score > 100
                    or not subject_score.is_integer()
                ):
                    raise ValueError
                break
            except ValueError:
                print(
                    "\n\t\tError: Invalid score or score \
greater 100 entered!\n")

        subjects[subject_name] = subject_score

    try:
        print(f"\n\t>>> adding {student_name.title()}'s data...")
        Student(name=student_name, subjects=subjects)
    except:
        print("\n\t\tError: Student's data creation failed!")
        return

    print()
    print(f"{student_name.title()}'s data stored successfully!")
    print()


def view_students() -> str:
    print(Student.In_memory)


def update_student():
    pass


def laod_from_json():
    pass


def save_to_json():
    pass


def save_and_exit() -> None:
    print("\n\t>>> saving all changes...")

    try:
        # save_to_json(data_to_save=Library.store_to_json())
        time.sleep(1)
    except Exception:
        print("\n\t\tError: operation failed!")

    print("\n\t>>> exiting student report card app..")
    time.sleep(1)
    sys.exit(0)
