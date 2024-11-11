# Define the file path
file_path = "students_data.txt"

# Create a file with some sample data for demonstration purposes
def create_initial_file():
    with open(file_path, 'w') as f:
        f.write("Student Name, Grade\n")
        f.write("Alice, A\n")
        f.write("Bob, B\n")
        f.write("Charlie, C\n")
        f.write("David, A\n")
        f.write("Eva, B+\n")
    print("Initial file created with student data.")

# 1. Read Entire File - 'read()'
def read_entire_file():
    try:
        with open(file_path, 'r') as file:
            content = file.read()  # Read the entire file at once
            print("\n--- Read Entire File ---")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")

# 2. Read Line by Line - 'readline()'
def read_line_by_line():
    try:
        with open(file_path, 'r') as file:
            print("\n--- Read Line by Line ---")
            # Read each line individually
            for line in file:
                print(line.strip())  # .strip() to remove the newline character
    except FileNotFoundError:
        print("The file does not exist.")

# 3. Read All Lines as List - 'readlines()'
def read_all_lines_as_list():
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read all lines and return them as a list
            print("\n--- Read All Lines as List ---")
            print(lines)
    except FileNotFoundError:
        print("The file does not exist.")

# 4. Read Specific Number of Characters - 'read(n)'
def read_specific_characters():
    try:
        with open(file_path, 'r') as file:
            print("\n--- Read Specific Number of Characters ---")
            # Read the first 20 characters from the file
            content = file.read(20)
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")

# 5. Using Context Manager for Automatic Closing
def using_context_manager():
    try:
        print("\n--- Using Context Manager for Automatic Closing ---")
        # Using the context manager automatically closes the file after use
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")

# 6. Read File Using 'for' Loop
def read_file_using_for_loop():
    try:
        print("\n--- Read File Using 'for' Loop ---")
        with open(file_path, 'r') as file:
            # Use 'for' loop to iterate over lines in the file
            for line in file:
                print(line.strip())  # Remove trailing newlines
    except FileNotFoundError:
        print("The file does not exist.")

# Activity Workflow: Students will use different methods to read the file
def file_reading_activity():
    # Step 1: Create the initial file with data
    create_initial_file()

    # Step 2: Demonstrate different ways of reading the file
    read_entire_file()
    read_line_by_line()
    read_all_lines_as_list()
    read_specific_characters()
    using_context_manager()
    read_file_using_for_loop()

# Run the file reading activity
file_reading_activity()
