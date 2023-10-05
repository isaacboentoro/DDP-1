import os
import sys
import time

directory = r"C:\Users\isaac\Documents\indo-law-main\dataset"
tag = sys.argv[1]  # Provide system argument for tag to search in
search = sys.argv[2]  # Provide system argument for search keyword
operator = ""  # Arbitrary initialization
search2 = ""
st = time.time()  # Start logging program runtime
files = []  # Initialize list to store results
stringsFound = 0
if len(sys.argv) == 3:
    for file in os.listdir(directory):
        tag_found = False
        current_path = os.path.join(directory, file)  # Set current path to open file
        with open(current_path, 'r', encoding='utf-8') as f:  # Read file
            for line in f:
                if tag_found and line[0:2] != "</" or tag == "all":
                    if search in line:  # Search for string in currently opened file
                        files.append(file)  # Append file to results list only when string is found
                        stringsFound += 1
                        break
                elif tag_found:
                    if search in line:  # Search for string in currently opened file
                        files.append(file)  # Append file to results list only when string is found
                        stringsFound += 1
                        break
                if line[0] == "<":  # Check if tag is 'all'
                    tag_found = True
                    continue

elif len(sys.argv) == 5:
    operator = sys.argv[3].upper()
    if operator not in ["AND", "OR", "ANDNOT"]:
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
                    if search in line:  # Search for string in currently opened file
                        search_found = True
                    if search2 in line:
                        search2_found = True
                    if search_found and search2_found:
                        break
                elif tag_found:  # Check if tag is 'all'
                    break
                if line[0] == "<" and tag in line:  # Check if tag is 'all'
                    tag_found = True
                    continue
            if (search_found and (
                    (operator == "AND" and search2_found) or (operator == "ANDNOT" and not search2_found)) or (
                    operator == "OR" and (search_found or search2_found))):
                files.append(file)  # Append file to results list only when string is found
                stringsFound += 1
for result in files:
    with open(os.path.join(directory, result), 'r', encoding='utf-8') as f:
        data = f.readline().strip("<>")
        attributes = data.split(" ")
        attributes = [attribute.split("=") for attribute in attributes]
        print(f"{result} ", end="")  # print the file name on the same line
        for attr_name in ["provinsi", "klasifikasi", "sub_klasifikasi", "lembaga_peradilan"]:
            for attr in attributes:
                if attr[0] == attr_name:
                    attr[1] = attr[1].strip("\"")
                    print(f"{attr[1].rjust(20)}", end=" ")
                    break
        print()  # add a newline after each file's attributes are printed

if len(sys.argv) == 3:
    print(f"Found {stringsFound} files (searched for '{search}' in {time.time() - st:.2f} seconds)")
elif len(sys.argv) == 5:
    print(
        f"Found {stringsFound} files (searched for '{search}' {operator} '{search2}' in {time.time() - st:.2f} seconds)")
