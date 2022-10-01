# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan yang gak ada koma nya (integer)

# import library dari bahasa c untuk tipe data double dan char
from ctypes import c_double, c_char, c_long
data_integer = 11
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup makan bakso"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = False
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

# === tipe data khusus ===

# bilangan kompleks
data_complex = complex(5, 6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))

data_c_char = c_char(b'J')
print("data : ", data_c_char)
print("- bertipe : ", type(data_c_char))

data_c_long = c_long(10)
print("data : ", data_c_long)
print("- bertipe : ", type(data_c_long))
