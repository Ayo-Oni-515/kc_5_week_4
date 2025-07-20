import sys
from utils import is_path, create_subdirectory, oragnize_files

def main() -> None:
    """main application workflow"""
    # sys.argv[0] is the script name
    # sys.argv[1:] are the arguments
    
    # argument count
    argc = len(sys.argv)

    if argc == 1 or argc > 2:
        print("\nError: improper usage\n\t'python main.py \'<directory-path>\''")
        sys.exit(1)
    
    try:
        directory_path = str(sys.argv[1])
    except ValueError:
        print("\nErrror: directory-path must be a string")
        sys.exit(1)

    if not is_path(directory_path):
        print("\nError: directory doesn't exist")
        sys.exit(1)
    
    create_subdirectory(directory_path)
    oragnize_files(directory_path)   


if __name__ == "__main__":
    main()