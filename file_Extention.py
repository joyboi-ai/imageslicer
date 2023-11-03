    

import os
def file_Extention(file):
    file_path = file  # Replace this with your file path

    # Using the os.path.splitext method to get the file extension
    file_extension = os.path.splitext(file_path)[1]

    # Removing the dot (.) from the extension if it's present
    if file_extension:
        file_extension = file_extension[1:]

    return (f"The file extension is: {file_extension}")


