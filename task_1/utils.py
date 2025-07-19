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
                subject_name: str = (input(f"\nEnter {i+1}{pos[i+1]} \
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


def view_students() -> None:
    output: str = """
------------------------------------------------------
===================== STUDENTS =======================
------------------------------------------------------
"""

    json_data = load_from_json()
    Student.In_memory.update(**json_data)

    all_data = Student.In_memory

    if len(all_data) == 0:
        print("\n\t>>> nothing to view...")
        return

    for name in all_data:
        student_name: str = name
        average: float = all_data[name]["average"]
        grade: str = all_data[name]["grade"]
        
        subjects: str = ""
        for subject, score in (all_data[name]["subjects"]).items():
            subject_info: str = f"\t{subject.title()}: {score}\n"
            subjects += subject_info
        
        output += f"""
-----------------------------------------------------
{student_name.title()}'s data
Average: {average}
Remark: {grade}

Subjects:\n{subjects}
-----------------------------------------------------
"""
        
    print(output)



def update_student() -> None:
    """update any student record"""
    json_data = load_from_json()
    Student.In_memory.update(**json_data)

    all_data = Student.In_memory

    if len(all_data) == 0:
        print("\n\t>>> nothing to update...")
        return

    print()
    while True:
        try:
            student_name: str = (
                input("Enter the name of the student to update: ")).lower()
            
            if not student_name.isascii():
                raise TypeError
            elif student_name not in all_data:
                raise NameError
            else:
                print("\n\t>>> student record exist")
                break
        except TypeError:
            print("\n\t\tError: Invalid student name syntax!\n")
        except NameError:
            print("\n\t\tError: Student data doesn't exist!\n")
            return

    print()
    while True:
        try:
            update_data: str = (
                input("Enter the data to update (name or subjects): ")).lower()
            
            if not update_data.isascii():
                raise TypeError
            elif update_data not in ["name", "subjects"]:
                raise NameError
            break
        except TypeError:
            print("\n\t\tError: Invalid data name syntax!\n")
        except NameError:
            print(
                "\n\t\tError: Entry can't be modified!\n")
        
    if update_data == "name":
        print()
        while True:
            try:
                new_name: str = (
                    input("Enter student's new name: ")).lower()
                
                if not new_name.isascii():
                    raise TypeError
                elif new_name in all_data.keys():
                    raise NameError
                break
            except TypeError:
                print("\n\t\tError: Invalid student name syntax!\n")
            except NameError:
                print("\n\t\tError: same student name is present in memory, use another!\n")
        
        all_data[new_name] = all_data[student_name]
        Student(name=new_name,
                subjects=all_data[student_name]["subjects"])
    
    elif update_data == "subjects":
        print()
        while True:
            try:
                subject_name: str = (
                    input("Enter subject to update: ")).lower()
                
                if not subject_name.isascii():
                    raise TypeError
                elif subject_name not in all_data[student_name]["subjects"]:
                    raise NameError
                break
            except TypeError:
                print("\n\t\tError: Invalid subject name syntax!\n")
            except NameError:
                print("\n\t\tError: Entry not present as a subject!\n")
        
        while True:
            try:
                subject_score: float = float(input("Enter new score: "))

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

        all_data[student_name]["subjects"][subject_name] = subject_score
        Student(name=student_name,
                subjects=all_data[student_name]["subjects"])

    save_to_json(data_to_save=all_data)


def is_json_file(file_path: str = "./data.json") -> bool:
    """checks for the existence of the josn file"""
    return os.path.exists(file_path)


def load_from_json(file_path: str = "./data.json") -> dict:
    """loads data from an existing json file"""
    retrieved_data: dict = {}

    if is_json_file(file_path):
        with open(file_path, "r") as file:
            # read data from an existing json file

            print(f"\n\t>>> loading data from {file.name[2:]}...")
            time.sleep(1)

            try:
                # parse existing data in json file
                retrieved_data = json.load(file)
            except Exception:
                # returns an empty dictionary if file is empty
                retrieved_data = {}
            
    else:
        with open(file_path, "w") as file:
            # create and save an empty distionary to json file
            print(f"\n\t>>> creating {file.name[2:]}...")
            save_to_json({}, file_path)
    
    return retrieved_data


def save_to_json(data_to_save: dict, file_path: str = "./data.json") -> None:
    """saves data to json file"""
    existing_data = load_from_json(file_path)
    existing_data.update(data_to_save)

    with open(file_path, "w") as data_file:
        # save to json file
        print(f"\n\t>>> saving to {data_file.name[2:]}...")

        time.sleep(1)
        json.dump(existing_data, data_file, indent=4)


def save_and_exit() -> None:
    print("\n\t>>> saving all changes...")

    try:
        json_data = load_from_json()
        Student.In_memory.update(**json_data)
        if len(Student.In_memory) == 0:
            print("\n\t>>> nothing to save..")
            raise
        save_to_json(data_to_save=Student.In_memory)
        time.sleep(1)
    except Exception:
        print("\n\t\tError: operation failed!")

    print("\n\t>>> exiting student report card app..")
    time.sleep(1)
    sys.exit(0)
