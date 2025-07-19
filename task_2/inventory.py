import os
import json
import sys
import time

from book import Book


def add_book() -> None:
    """adds book data"""
    print()
    while True:
        try:
            book_title: str = (
                input("Enter book's title: ")).lower()
            
            if not book_title.isascii():
                raise TypeError
            elif book_title in load_from_json().keys():
                raise NameError
            elif book_title in Book.In_memory:
                raise ValueError
            break
        except TypeError:
            print("\n\t\tError: Invalid book title syntax!\n")
        except NameError:
            print(
                "\n\t\tError: Book exists in json file!\n")
        except ValueError:
            print("\n\t\tError: Book has already been added!\n")
    
    print()
    while True:
        try:
            book_author: str = (
                input("Enter author's name: ")).lower()
            
            if not book_author.isascii():
                raise TypeError
            break
        except TypeError:
            print("\n\t\tError: Invalid author name syntax!\n")
    
    print()
    while True:
        try:
            book_price: int = int(
                input("Enter book's price: "))
            
            if not book_price.is_integer():
                raise TypeError
            break
        except TypeError:
            print("\n\t\tError: Invalid book price syntax!\n")
    
    print()
    while True:
        try:
            book_stock: int = int(
                input("Enter quantity in stock: "))
            
            if not book_stock.is_integer():
                raise TypeError
            break
        except TypeError:
            print("\n\t\tError: Invalid book price syntax!\n")
    
    try:
        print(f"\n\t>>> adding {book_title.title()}'s data...")
        Book(title=book_title, author=book_author, price=book_price,
             stock=book_stock)
    except:
        print("\n\t\tError: Book's data creation failed!")
        return

    print()
    print(f"{book_title.title()}'s data stored successfully!")
    print()


def view_books() -> None:
    """returns all book records."""
    output: str = """
------------------------------------------------------
======================= BOOKS ========================
------------------------------------------------------
"""

    json_data = load_from_json()
    Book.In_memory.update(**json_data)

    all_data = Book.In_memory

    if len(all_data) == 0:
        print("\n\t>>> nothing to view...")
        return

    for name in all_data:
        book_title: str = name
        book_author: float = all_data[name]["author"]
        book_price: str = all_data[name]["price"]
        book_stock: str = all_data[name]["stock"]
        
        output += f"""
-----------------------------------------------------
{book_title.title()}'s data
Author: {book_author}
Price: {book_price}
Stock: {book_stock}
-----------------------------------------------------
"""
 
    print(output)


def is_json_file(file_path: str = "./books.json") -> bool:
    """checks for the existence of the josn file"""
    return os.path.exists(file_path)


def load_from_json(file_path: str = "./books.json") -> dict:
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


def save_to_json(data_to_save: dict, file_path: str = "./books.json") -> None:
    """saves data to json file"""
    existing_data = load_from_json(file_path)
    existing_data.update(data_to_save)

    with open(file_path, "w") as data_file:
        # save to json file
        print(f"\n\t>>> saving to {data_file.name[2:]}...")

        time.sleep(1)
        json.dump(existing_data, data_file, indent=4)


def save_and_exit() -> None:
    """saves all changes and exit program"""
    print("\n\t>>> saving all changes...")

    try:
        json_data = load_from_json()
        Book.In_memory.update(**json_data)
        if len(Book.In_memory) == 0:
            print("\n\t>>> nothing to save..")
            raise
        save_to_json(data_to_save=Book.In_memory)
        time.sleep(1)
    except Exception:
        print("\n\t\tError: operation failed!")

    print("\n\t>>> exiting book inventory...")
    time.sleep(1)
    sys.exit(0)
