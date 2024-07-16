import os

# Specify the directory path
directory_path = '/Web Development'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
