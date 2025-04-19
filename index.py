import os

# Prompt user for the filename
filename = input("Enter the filename to read: ").strip()

# Attempt to read the file
try:
    with open(filename, 'r') as infile:
        lines = infile.readlines()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read '{filename}'.")
except OSError as e:
    print(f"Error reading the file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    # Process the content by adding line numbers
    modified_lines = []
    for line_num, line in enumerate(lines, 1):
        modified_lines.append(f"{line_num}: {line}")
    
    # Generate the output filename
    original_name, ext = os.path.splitext(filename)
    output_filename = f"{original_name}_modified{ext}"
    
    # Attempt to write the modified content to a new file
    try:
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)
    except PermissionError:
        print(f"Error: Permission denied to write to '{output_filename}'.")
    except OSError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing: {e}")
    else:
        print(f"Modified file successfully saved as '{output_filename}'.")