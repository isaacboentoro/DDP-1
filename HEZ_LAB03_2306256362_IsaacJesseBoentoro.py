# Isaac Jesse Boentoro
# NPM: 2306256362

print("Lab 03\n")
print("From decimal to hexadecimal\n---------------------------\n")
int_input = int(input("Give a positive integer in decimal representation: "))
int_convert = int_input
hex_chars = "0123456789ABCDEF"
result = ""

if int_input == 0:
    result = "0"

while int_input > 0:
    mod = int_input % 16
    result = hex_chars[mod] + result
    int_input //= 16

print(f"The hexadecimal representation of {int_convert} is 0x{result}")

print("\n---------------------------")
hex_input = input("Give a positive integer in hexadecimal representation: ")
hex_input_stripped = hex_input.replace("0x", "", 1).upper()
decimal_value = 0

for char in hex_input_stripped:
    if char in hex_chars:
        decimal_value = decimal_value * 16 + hex_chars.index(char)
    else:
        print(f"Invalid character '{char}' in the input.")
        break

print(f"The decimal representation of {hex_input} is {decimal_value}\n")

# Find hex_chars in the string input by user, then get its index

print(f"The decimal representation of {hex_input} is {decimal_value}\n")  # Print final answer d
input("Thanks for using this program\nPress Enter to continue ...")  # Wait for final user interaction to exit program
