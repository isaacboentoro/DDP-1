import os
import sys
import time
directory = r"C:\Users\isaac\Documents\indo-law-main\dataset"
search = sys.argv[1]  # Provide system argument for search keyword
st = time.time() # Start logging program runtime
files = [] # Initialize list to store results
for file in os.listdir(directory):
    current_path = os.path.join(directory, file) # Set current path to open file
    with open(current_path, 'r', encoding='utf-8') as f: # Read file
        if search in f.read(): # Search for string in currently opened file
            files.append(file) # Append file to results list only when string is found

for result in files: # Process the results to include their attributes
    with open(os.path.join(directory, result), 'r', encoding='utf-8') as f: # Open all files contained within the results list
        data = f.readline().strip("<>") # Read the first line and remove tag quantifiers "<>"
        attributes = data.split(" ") # Split the first line into respective tags and their contents using quotes as the separator
        attributes = [attribute.split("=") for attribute in attributes] # Create a list of tags and their contents for every double quote
        print(f"{result} ", end="")  # Print the result filename
        for attr_name in ["provinsi", "klasifikasi", "sub_klasifikasi", "lembaga_peradilan"]: # Filter out other tags/attributes
            for attr in attributes: # Iterate through list of tags
                if attr[0] == attr_name: # Check if tag is one of the four tags we are looking for
                    print(f"{attr[1].strip('\"')}", end=" ") # Print out the tag's contents
                    break # Break loop after printing is finished
        print()  # add a newline after each file's attributes are printed

end = time.time() # End logging program runtime
print(f"Found {len(files)} files (searched for '{search}' in {(end - st)} seconds)") # Print out final message with runtime