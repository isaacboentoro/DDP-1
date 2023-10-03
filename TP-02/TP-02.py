import os
import sys
import time

directory = r"C:\Users\isaac\Documents\indo-law-main\dataset"
search = sys.argv[1]  # Provide system argument for search keyword
st = time.time()  # Start logging program runtime
files = []  # Initialize list to store results
for file in os.listdir(directory):
    current_path = os.path.join(directory, file)  # Set current path to open file
    with open(current_path, 'r', encoding='utf-8') as f:  # Read file
        if search in f.read():  # Search for string in currently opened file
            files.append(file)  # Append file to results list only when string is found

for result in files:
    with open(os.path.join(directory, result), 'r', encoding='utf-8') as f:
        data = f.readline().strip("<>")
        attributes = data.split(" ")
        attributes = [attribute.split("=") for attribute in attributes]
        print(f"{result} ", end="")  # print the file name on the same line
        for attr_name in ["provinsi", "klasifikasi", "sub_klasifikasi", "lembaga_peradilan"]:
            for attr in attributes:
                if attr[0] == attr_name:
                    attr_value = attr[1].strip('\"')
                    if len(attr_value) > 14:
                        attr_value = attr_value[:14] + "..."
                    print(f"{attr_value}", end=" ")
                    break
        print()  # add a newline after each file's attributes are printed

end = time.time()  # End logging program runtime
print(
    f"Found {len(files)} files (searched for '{search}' in {(end - st)} seconds)")
# Print out final message with  runtime
