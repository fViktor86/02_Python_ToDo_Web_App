FILEPATH = r"files/todos.txt"  # Define the file path for the files, r means raw string to avoid escape characters


def get_todos(filepath=FILEPATH):
    """    Reads the items from a file and returns them as a list.
    This is a docstring for the function get_todos. print(help(get_todos)) can be used to see this docstring."""
    try:
        with open(filepath, 'r') as local_file:  # Open the file in read mode, r means read
            local_todos = local_file.readlines()
        return local_todos
    except FileNotFoundError:
        print("File not found. Please ensure the file exists.")
        return []  # Return an empty list if the file does not exist


def write_todos(local_todos, filepath=FILEPATH):
    """    Writes the items to a file."""
    try:
        with open(filepath, 'w') as local_file:
            local_file.writelines(local_todos)
    except FileNotFoundError:
        exit(f"Folder does not exist: {filepath}")
    except PermissionError:
        exit(f"No permission to write to file: {filepath}")
    except OSError as e:
        exit(f"OS error occurred while writing the file: {e}")


# This block will only run if this file is executed directly, not when imported
if __name__ == '__main__':      # This module name is __main__ if this file is executed directly, otherwise it is the name of the module, such as functions
    print("Hello from functions.py!")