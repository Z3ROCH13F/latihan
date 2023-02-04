"""
A:          #   B:
            #
abs()       #   bin()
all()       #   bool()
any()       #
ascii()     #


INI UNTUK python 3.9

"""

# abs()
# Fungsi abs() adalah mengembalikan nilai mutlak sesuatu nombor
x1 = 3.21
x2 = abs(1 + 1.1 + 1.11)
x3 = abs(x1 - x2)
print(x2)
# Output 3.21
print(x3)
# Output 0.0

# all()
# Kekurangan maklumat fungsi all()

# any()
# Kekurangan maklumat fungsi any()

# ascii()
x1 = "hello"
x2 = ascii(x1)
print(x2)
# Output 'hello'

# bin()
# Kekurangan maklumat fungsi bin()

# bool()
x1 = bool(True | False)
print(x1)
# Output True
x2 = bool(True or False)
print(x2)
# Output True
x3 = bool(False | False)
print(x3)
# Output False