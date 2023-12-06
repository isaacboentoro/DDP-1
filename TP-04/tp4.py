import tkinter as tk
from tkinter import messagebox

class BarcodeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Barcode Generator")
        text = tk.Label(self, text = "Save barcode to PS file: ")
        text.pack()
        self.filename_entry = tk.Entry(self)
        self.filename_entry.pack()
        self.filename_entry.bind('<Return>', self.save_to_eps)  # Bind Enter key to save_to_eps method
        text1 = tk.Label(self, text = "Enter code(first 12 decimal digits): ")
        text1.pack()
        self.barcode_entry = tk.Entry(self)
        self.barcode_entry.pack()
        self.barcode_canvas = tk.Canvas(self, width=500, height=300)
        self.barcode_canvas.pack()
        self.barcode_entry.bind('<Return>', self.barcode)
        self.geometry("300x400")

        self.first_digit = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', 'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']
        self.L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
        self.G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', '0111001', '0000101', '0010001', '0001001', '0010111']
        self.R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100', '1001000', '1110100']

        

    def calculate_check_digit(self, barcode):
        barcode = [int(x) for x in str(barcode)]
        odd_sum = sum(barcode[i] for i in range(0, len(barcode), 2))
        even_sum = sum(barcode[i] for i in range(1, len(barcode), 2))
        total = odd_sum + even_sum * 3
        check_digit = 10 - total % 10
        if check_digit == 10:
            check_digit = 0

        return check_digit
    
    def encode(self, barcode):
        left_section = [int(x) for x in str(barcode)[1:7]]
        right_section = [int(x) for x in str(barcode)[7:]]

        pattern = self.first_digit[int(str(barcode)[0])]
        encoded_barcode = '101'  # Start guard bar
        for i, digit in enumerate(left_section):
            if pattern[i] == 'L':
                encoded_barcode += self.L_codes[digit]
            else:
                encoded_barcode += self.G_codes[digit]
        encoded_barcode += '01010'  # Middle guard bar
        for digit in right_section:
            encoded_barcode += self.R_codes[digit]
        encoded_barcode += '101'  # End guard bar

        return encoded_barcode
    
    def save_to_eps(self, event=None):
        filename = self.filename_entry.get()
        if filename:
            self.barcode_canvas.postscript(file=filename)
        
    def barcode(self, event=None):
        barcode = self.barcode_entry.get()
        if len(barcode) != 12 or barcode.isdigit() == False:
            messagebox.showerror("Wrong Input!", "Please enter correct input code (Numeric 12 bits)")
            return
        
        check_digit = self.calculate_check_digit(barcode)
        complete_barcode = str(barcode) + str(check_digit)
        encoded_barcode = self.encode(complete_barcode)
        print(f"Barcode with check digit: {str(barcode)}{str(check_digit)}")
        print(f"Barcode in binary form:\n{encoded_barcode}")
       
        self.barcode_canvas.delete("all")  # Clear the canvas
        x = 5
        z = 15
        y = 200  # Position for the text
        for i, digit in enumerate(encoded_barcode):
            if digit == '1' and (i < 3 or 45 < i < 50 or i > 91):
                color = "blue"
                height = 200
            else:
                color = "black" if digit == '1' else "white"
                height = 150

            self.barcode_canvas.create_rectangle(x, 0, x+3, height, fill=color, outline='')
            x += 3
        for j in range(len(complete_barcode)):
            text = " " + complete_barcode[j] + "   " if j == 6 else complete_barcode[j]
            self.barcode_canvas.create_text(z+5, y, text=text, fill="black", font="Arial 15 bold")
            z += 20
        self.barcode_canvas.create_text(150, 250, text ="Check Digit: {check_digit}".format(check_digit=check_digit), fill="blue", font="Arial 15 bold")
        self.barcode_canvas.create_text(150, 270, text = "EAN-13 Barcode", fill = "black", font="Arial 15 bold")
def main():
    app = BarcodeApp()
    app.mainloop()

if __name__ == """__main__""":
    main()

