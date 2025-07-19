import time
import inventory


def intro() -> str:
    return """
------------------------------------------------

================ Welcome to my =================

============= Book Inventory System ============

------------------------------------------------
"""


def menu() -> str:
    return """
--------------------------------
(select an option from the menu)
--------------------------------
\t1. Add a new book.
\t2. View all books
\t3. Save & Exit.
"""


def menu_operations():
    valid_options: list = [1, 2, 3]

    while True:
        try:
            selected_option: int = int(input("Select an option: "))

            if selected_option not in valid_options:
                raise ValueError
            break
        except ValueError:
            print("\n\t\tError: Invalid menu option!\n")

    if selected_option == 1:
        print("\n\t>>> 'Add a new book' selected.")
        time.sleep(0.5)
        inventory.add_book()
    elif selected_option == 2:
        print("\n\t>>> 'View all books' selected.")
        time.sleep(0.5)
        inventory.view_books()
    elif selected_option == 3:
        inventory.save_and_exit()


def main():
    print(menu())
    menu_operations()


if __name__ == "__main__":
    print(intro())

    while True:
        main()
