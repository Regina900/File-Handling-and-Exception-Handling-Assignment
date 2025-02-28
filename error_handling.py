def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            print("\nFile Contents:\n")
            print(file.read())

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied. You don't have access to '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_file_with_error_handling()
