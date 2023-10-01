import os
import sys
import time
directory = r"C:\Users\isaac\Documents\indo-law-main\dataset"
# search = ' '.join(sys.argv[1:])
# if search.startswith('"') and search.endswith('"'):
#     search = search[1:-1]
search = "laptop acer"
strings_found = 0
st = time.time()
for file in os.listdir(directory):
    current_path = os.path.join(directory, file)
    with open(current_path, 'r', encoding='utf-8') as f:
        if search in f.read():
            print(file)
            strings_found += 1
end = time.time()
end - st
print(f"Found {strings_found} files (searched for '{search}' in {end - st} seconds)")
