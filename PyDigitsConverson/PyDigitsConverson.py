from digit import Digit, DigitType
from decimal_digit import DecimalDigit
from binary_digit import BinaryDigit

digit1 = DecimalDigit()
digit1.digit_value = '12'
print(digit1.get_binary()) #1100
print(digit1.get_octal()) #14
print(digit1.get_hexadecimal()) #C

digit2 = DecimalDigit(digit_value='291,725', digit_type=10, separator=',')
print(digit2.get_binary()) #1100
print(digit2.get_octal()) #443.56314631463146314631463146314631463146314631463146
print(digit2.get_hexadecimal()) #123.B99999999

digit3 = BinaryDigit(digit_value='100100011,1011100110', digit_type=2, separator=',')
print(digit3.get_decimal())

digit4 = DecimalDigit(digit_value='399.564', digit_type=10, separator=',')
print("399.564 = " + digit4.get_binary()) #1100

digit5 = BinaryDigit(digit_value='110011111.1001000001', digit_type=2, separator='.')
print(digit5.get_decimal())