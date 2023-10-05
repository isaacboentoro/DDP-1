import os
import sys
import time

directory = r"C:\Users\isaac\Documents\indo-law-main\dataset"  # Set directory to open files from
tag = sys.argv[1]  # Provide system argument for tag to search in
search = sys.argv[2]  # Provide system argument for search keyword
operator = ""  # Arbitrary initialization
search2 = ""
st = time.time()  # Start logging program runtime
files = []  # Initialize list to store results
stringsFound = 0  # Counter for number of files found
if len(sys.argv) == 3:
    for file in os.listdir(directory):
        tag_found = False
        current_path = os.path.join(directory, file)  # Set current path to open file
        with open(current_path, 'r', encoding='utf-8') as f:  # Read file
            for line in f:
                if tag_found and line[0:2] != "</" or tag == "all":  # Search for section while making sure we find
                    # the start, not end of the section
                    if search in line:  # Search for string in currently opened file
                        files.append(file)  # Append file to results list only when string is found
                        stringsFound += 1  # Increment counter
                        break  # Break loop to avoid duplicate increments
                elif tag_found:  # If start of tag is found immediately, jump to this statement and start searching
                    if search in line:
                        files.append(file)
                        stringsFound += 1
                        break
                if line[0] == "<" and tag in line:  # Check if line is a tag, and that tag is the one we're looking for
                    tag_found = True  # Set tag_found to True to start searching for string
                    continue

elif len(sys.argv) == 5:
    operator = sys.argv[3].upper()
    if operator not in ["AND", "OR", "ANDNOT"]:  # Check if operator is valid
        print("Please provide a valid operator (AND, OR, ANDNOT)")
        sys.exit()
    search2 = sys.argv[4]
    for file in os.listdir(directory):
        tag_found = False
        search_found = False
        search2_found = False
        current_path = os.path.join(directory, file)  # Set current path to open file
        with open(current_path, 'r', encoding='utf-8') as f:  # Read file
            for line in f:
                if (tag_found and line[0:2] != "</") or (tag == 'all'):
                    if search in line:
                        search_found = True
                    if search2 in line:
                        search2_found = True
                    if search_found and search2_found:
                        break
                elif tag_found:
                    break
                if line[0] == "<" and tag in line:
                    tag_found = True
                    continue
            if (search_found and (
                    (operator == "AND" and search2_found) or (operator == "ANDNOT" and not search2_found)) or (
                    operator == "OR" and (search_found or search2_found))):
                files.append(file)
                stringsFound += 1
for result in files:  # Read through files and return attributes
    with open(os.path.join(directory, result), 'r', encoding='utf-8') as f:
        data = f.readline().strip("<>")  # Read first line of file and remove tag quantifiers
        attributes = data.split(" ")  # Split attributes into list with double quotes as separator
        attributes = [attribute.split("=") for attribute in attributes]  # List comprehension to split attributes
        # into key-value pairs
        print(f"\033[1m\033[32m{result}\033[0m ", end="")  # print the file name on the same line
        for attr_name in ["provinsi", "klasifikasi", "sub_klasifikasi", "lembaga_peradilan"]:  # Define wanted variables
            for attr in attributes:  # Iterate through found attributes
                if attr[0] == attr_name:  # Check if attribute is wanted
                    attr[1] = attr[1].strip("\"")  # Remove double quotes from attribute value
                    color_code = "\033[94m" if attr_name == "provinsi" else "\033[36m"  # Set color code for attribute
                    print(f"{color_code}{attr[1][:15].rjust(20)}\033[0m", end=" ")  # Print attribute value
                    break
        print()  # add a newline after each file's attributes are printed

if len(sys.argv) == 3:  # Separate print statements for different number of system arguments
    print(f"Found {stringsFound} files (searched for '{search}' in {time.time() - st: .2f} seconds)")
elif len(sys.argv) == 5:
    print(
        f"Found {stringsFound} files (searched for '{search}' "
        f"{operator} '{search2}' in {time.time() - st: .2f} seconds)")
