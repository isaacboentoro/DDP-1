import os
import sys
import time
directory = r"C:\Users\isaac\Documents\indo-law-main\dataset"
search = ' '.join(sys.argv[1:])
if search.startswith('"') and search.endswith('"'):
    search = search[1:-1]
strings_found = 0
st = time.time()
files = []
for file in os.listdir(directory):
    current_path = os.path.join(directory, file)
    with open(current_path, 'r', encoding='utf-8') as f:
        if search in f.read():
            files.append(file)
            strings_found += 1
end = time.time()

for result in files:
    with open(os.path.join(directory, result), 'r', encoding='utf-8') as f:
        data = f.readline().strip("<>")
        attributes = data.split(" ")
        attributes = [attribute.split("=") for attribute in attributes]
        print(f"{result} ", end="")  # print the file name on the same line
        for attr_name in ["provinsi", "klasifikasi", "sub_klasifikasi", "lembaga_peradilan"]:
            for attr in attributes:
                if attr[0] == attr_name:
                    print(f"{attr[0]}: {attr[1].strip('\"')}", end=" ")
                    break
        print()  # add a newline after each file's attributes are printed

print(f"Found {strings_found} files (searched for '{search}' in {end - st} seconds)")


