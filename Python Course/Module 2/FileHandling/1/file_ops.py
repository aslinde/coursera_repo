def read_file(file_name):
    """ Reads and returns the entire contents of a file as a single string.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function.
        2. Print the contents of the file.
        3. Return the contents of the file.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        str: Entire contents of the file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name) as file:
        return file.read()

def read_file_into_list(file_name):
    """ Reads a file and returns a list where each element is a line in the file.

    [IMPLEMENT ME]
        1. Open the given file.
        2. Read the file line-by-line and append each line to a list.
        3. Return the list.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        list: List where each item is a line from the file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name) as file:
        return file.readlines()


def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a given string to an output file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents.
        2. Use the File write() function to write the first line into a file
           with the name from output_filename.

        The first line is everything in a string before the first newline ('\n') character.

    Args:
        file_contents (str): String containing multiple lines of text.
        output_filename (str): Name of the file to write the first line into.
    """
    ### WRITE SOLUTION HERE
    list_of_lines = file_contents.split("\n")
    with open(output_filename, "w") as output_file:
        output_file.write(list_of_lines[0])

def read_even_numbered_lines(file_name):
    """ Reads even-numbered lines of a file and returns them as a list.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable.
        2. Read the file line-by-line and add the even-numbered lines to a list.
        3. Return the list.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        list: List of even-numbered lines in the file (2, 4, 6, etc.).
    """
    ### WRITE SOLUTION HERE
    '''
    with open(file_name) as file:
        list_of_lines = file.readlines()
    even_list = []
    for line in list_of_lines:
        if (list_of_lines.index(line)+1)%2 == 0:
            even_list.append(line)
    return even_list
    '''
    ### Call function to read file into a list of lines
    list_of_lines = read_file_into_list(file_name)
    ### Expression to add line from the list of lines only if the number of lines
    ### is even as % returns leftover after division
    even_list = [line for line in list_of_lines if (list_of_lines.index(line)+1)%2 == 0]
    return even_list
def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of its lines in reverse order.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable.
        2. Read the file line-by-line and store the lines in a list in reverse order.
        3. Print the list.
        4. Return the list.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        list: List of lines from the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    list_of_lines = read_file_into_list(file_name)
    ''' 
    list_of_lines.reverse() # This code works it's just that I want to write
    print(list_of_lines)    # My own reverse() function
    return list_of_lines
    '''

    ''' # Now I'll try it with an expression
    reverse_list = []
    for line in list_of_lines:
        element = list_of_lines.index(line)+1
        reverse_list.append(list_of_lines[-element])
    return reverse_list
    '''
    reverse_list = [list_of_lines[-(list_of_lines.index(line)+1)] \
    for line in list_of_lines]
    return reverse_list

# Sample commands to run/test your implementations.
def main():
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "output.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
