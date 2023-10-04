import os
import sys
import time

directory = r"C:\Users\isaac\Documents\indo-law-main\dataset"
tag = sys.argv[1]  # Provide system argument for tag to search in
search = sys.argv[2]  # Provide system argument for search keyword
st = time.time()  # Start logging program runtime
files = []  # Initialize list to store results
stringsFound = 0
if len(sys.argv) == 3:
    for file in os.listdir(directory):
        tag_found = False
        current_path = os.path.join(directory, file)  # Set current path to open file
        with open(current_path, 'r', encoding='utf-8') as f:  # Read file
            for line in f:
                if tag_found and line[0:2] != "</":
                    if search in f.read():  # Search for string in currently opened file
                        files.append(file)  # Append file to results list only when string is found
                        stringsFound += 1
                        break
                elif tag_found or tag == 'all':  # Check if tag is 'all'
                    if search in f.read():  # Search for string in currently opened file
                        files.append(file)  # Append file to results list only when string is found
                        stringsFound += 1
                        break
                if line[0] == "<" and (tag == 'all' or tag in line):  # Check if tag is 'all'
                    tag_found = True
                    continue
elif len(sys.argv) == 5:
    operator = sys.argv[3].upper()
    search2 = sys.argv[4]
    for file in os.listdir(directory):
        tag_found = False
        current_path = os.path.join(directory, file)  # Set current path to open file
        with open(current_path, 'r', encoding='utf-8') as f:  # Read file
            for line in f:
                if tag_found and line[0:2] != "</":
                    if operator == "AND":
                        if search and search2 in line:  # Search for string in currently opened file
                            files.append(file)  # Append file to results list only when string is found
                            stringsFound += 1
                            break
                elif tag_found or tag == 'all':  # Check if tag is 'all'
                    if search in line:  # Search for string in currently opened file
                        files.append(file)  # Append file to results list only when string is found
                        stringsFound += 1
                        break
                if line[0] == "<" and (tag == 'all' or tag in line):  # Check if tag is 'all'
                    tag_found = True
                    continue
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

end = time.time()
if len(sys.argv) == 3:
    print(f"Found {stringsFound} files (searched for '{search}' in {end - st} seconds)")
elif len(sys.argv) == 5:
    print(f"Found {stringsFound} files (searched for '{search}' {operator} '{search2}' in {end - st} seconds)")