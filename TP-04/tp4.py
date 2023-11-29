
def calculate_check_digit(barcode):
    barcode = [int(x) for x in str(barcode)]
    odd_sum = sum(barcode[i] for i in range(0, len(barcode), 2))
    even_sum = sum(barcode[i] for i in range(1, len(barcode), 2))
    total = odd_sum + even_sum * 3
    check_digit = 10 - total % 10
    if check_digit == 10:
        check_digit = 0

    return check_digit

def encode(barcode):
    # Define the encoding patterns
    L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', '0111001', '0000101', '0010001', '0001001', '0010111']
    R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100', '1001000', '1110100']

    # Split the barcode into left and right sections
    left_section = [int(x) for x in str(barcode)[:7]]
    right_section = [int(x) for x in str(barcode)[7:]]

    # Encode the left section
    left_codes = [L_codes[left_section[i]] if i % 2 == 0 else G_codes[left_section[i]] for i in range(1, len(left_section))]

    # Encode the right section
    right_codes = [R_codes[x] for x in right_section]

    # Combine the encoded sections with the guard bars
    encoded_barcode = '101' + ''.join(left_codes) + '01010' + ''.join(right_codes) + '101'
    # encoded_barcode =''.join(left_codes)+ ''.join(right_codes)
    return encoded_barcode

import tkinter as tk

def render_barcode(encoded_barcode):
    # Create a new tkinter window
    window = tk.Tk()
    window.title("Barcode")

    # Create a canvas in the window
    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    # Draw rectangles for each bar in the barcode
    x = 10
    for digit in encoded_barcode:
        color = "black" if digit == '1' else "white"
        canvas.create_rectangle(x, 50, x+4, 350, fill=color, outline=color)
        x += 4

    # Display the window
    window.mainloop()

# Test the function
barcode = 899720727001
check_digit = calculate_check_digit(barcode)
encoded_barcode = encode(str(barcode) + str(check_digit))
print(str(barcode) + str(check_digit))
print(encoded_barcode)
render_barcode(encoded_barcode)