def parse_spectrum_file(filepath: str) -> tuple[list[float], list[float]]:
    """
    filepath: A string representing the path to the file
    returns a tuple of (x, y) data
    """
    
    # Open the file
    file = open(filepath, 'r')

    # Create lists to store the x and y data
    x: list[float] = []
    y: list[float] = []

    # Go through the file starting at line 15. Before line 15 is just metadata
    lines = file.readlines()
    for line in lines[14:]:
        # Split by spaces
        words = line.split()

        # The first number is x and the second number is y. Typecast them to floats
        x.append(float(words[0]))
        y.append(float(words[1]))
    
    # Return the x and y data
    return x, y
