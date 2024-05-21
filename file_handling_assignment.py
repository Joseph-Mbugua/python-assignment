def create_and_write_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, my name is Joseph.\n")
            file.write("0708964590.\n")
            file.write("24 and Two thousand.\n")
        print("File created and initial content written successfully.")
    except PermissionError:
        print("Permission denied: unable to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while writing to the file: {e}")

def read_and_display_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found: please ensure the file exists before reading.")
    except PermissionError:
        print("Permission denied: unable to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("I live in Nairobi.\n")
            file.write("30197 - 00100.\n")
            file.write("42nd street.\n")
        print("Content appended successfully.")
    except PermissionError:
        print("Permission denied: unable to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while appending to the file: {e}")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()
