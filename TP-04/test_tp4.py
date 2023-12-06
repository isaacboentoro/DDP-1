from tp4 import BarcodeApp

def test_check_digit():
    app = BarcodeApp()
    barcode = 899720727001
    assert app.calculate_check_digit(barcode) == 0

def test_encoding():
    app = BarcodeApp()
    barcode = 899720727001
    assert app.encode(barcode) == '1010001011001011101110110011011010011101110110101011011001000100111001011100101100110101'

def test_encoding_2():
    app = BarcodeApp()
    barcode = 30683200550
    assert app.encode(barcode) == '101000110101011110001001010000100110110001101010101110010100111010011101110010101'
