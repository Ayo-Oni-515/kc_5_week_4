import time
import utils


def intro() -> str:
    return """
------------------------------------------------

================ Welcome to my =================

============ Student Report Card App ===========

------------------------------------------------
"""


def menu() -> str:
    return """
--------------------------------
(select an option from the menu)
--------------------------------
\t1. Add a new student.
\t2. View all students.
\t3. Update an existing student.
\t4. Save & Exit.
"""


def menu_operations():
    valid_options: list = [1, 2, 3, 4]

    while True:
        try:
            selected_option: int = int(input("Select an option: "))

            if selected_option not in valid_options:
                raise ValueError
            break
        except ValueError:
            print("\n\t\tError: Invalid menu option!\n")

    if selected_option == 1:
        print("\n\t>>> 'Add a new student' selected.")
        time.sleep(0.5)
        utils.add_student()
    elif selected_option == 2:
        print("\n\t>>> 'View all students' selected.")
        time.sleep(0.5)
        utils.view_students()
    elif selected_option == 3:
        print("\n\t>>> 'Update an existing student' selected.")
        time.sleep(0.5)
        utils.update_student()
    elif selected_option == 4:
        utils.save_and_exit()


def main():
    print(menu())
    menu_operations()


if __name__ == "__main__":
    print(intro())

    while True:
        main()
