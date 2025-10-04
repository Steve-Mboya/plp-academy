 def modify_content(content):
    
    return content.upper()


def main():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify content
        modified_content = modify_content(content)

        # Write to new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied while accessing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
