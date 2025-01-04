def read_and_write_file(input_filename, output_filename):
    
        # Open and read the input file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content 
        modified_content = content.upper() 
        
        # Write the modified content to a new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"File has been successfully read and written to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' can't be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Prompt the user for filenames
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the new file to write to: ")

# Call the function
read_and_write_file(input_filename, output_filename)
