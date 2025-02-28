def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        modified_content = [line.upper() for line in content]
        
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read or write to the file.")

# Run the function
read_and_modify_file('input.txt', 'output.txt')
