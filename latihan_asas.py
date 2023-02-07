
# Jenis kelas
x1 = "halo"           # Ini str
x1 = 'dunia'          # Ini juga str
x1 = """Helo dunia""" # Dan ini juga str
x2 = 1                # Ini int
x2 = 10               # Ini juga int
x3 = 1.1              # Ini float
x3 = 10.1             # Ini juga float
x4 = True             # Ini bool
x4 = False            # Ini juga bool

"""
A:          #   B:
            #
abs()       #   bin()
all()       #   bool()
any()       #   breakpoint()
ascii()     #   bytearray()
            #
            #

INI UNTUK python 3.9

"""


print("ini abs()")
# Fungsi abs() adalah mengembalikan nilai mutlak sesuatu nombor
x1 = 3.21
x2 = abs(1 + 1.1 + 1.11)
x3 = abs(x1 - x2)
x4 = abs(2000 + 24)
print(x2)
# Output 3.21
print(x3)
# Output 0.0
print(x4)
# Output 2024

print("ini all()")
# Fungsi all(x1) adalah, jika x1 adalah str kemudian all(x1) akan memberikan bool True
x1 = "hello dunia"
print(all(x1))
# Output True

print("ini any()")
# Fungsi any(x1) adalah, jika x1 adalah str kemudian any(x1) akan memberikan bool True dan jika x1 = "" kemudian any(x1) akan mengembalikan bool False
print(any(x1))
# Output True
x1 = ""
print(any(x1))
# Output False

print("ini ascii()")
x1 = "hello"
x2 = ascii(x1)
print(x2)
# Output 'hello'

# bin()
# Kekurangan maklumat fungsi bin()

print("ini bool()")
x1 = bool(True or False)
print(x1)
# Output True
x2 = bool(1 or False)
print(x2)
# Output True
x3 = bool(0 or 0)
print(x3)
# Output False
x4 = bool(1 or 0)
print(x4)
# Output True

print("ini breakpoint()")
# Kekurangan maklumat fungsi breakpoint()

print("ini bytearray()")
# Kekurangan maklumat fungsi bytearray()