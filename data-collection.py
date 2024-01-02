# Data Type Collection

# List: Data ordered
x = [1, 2.2, "Dicoding"]
print(type(x))
# output : <class "list">

# access Index
y = [1, "Dicoding", True, 1.0]
print(y[2])

# slicing list
"""
sequence[start:stop:step].

Start : indeks pertama yang diambil
Stop : indeks terakhir yang diambil
Step : Jumlah elemen yang ingin dilewati
"""

x = ["laptop", "Monitor", "Mouse", "Mousepad", "Keyboard", "webcam", "Microphone"]

print(x[0:5:2])
# output : ['laptop', 'mouse', 'keyboard']
print(x[1:])
# output : ['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
print(x[:3])
# output : ['laptop', 'monitor', 'mouse']


# Tuple
x = (1, "Dicoding", 1+3j)
print(type(x))
# output : <class 'tuple'>

# Slicing and Indexing Tuple
x = (5, 'program', 1+3j)
print(x[1])
# output : program
print(x[0:3])
# output : (5, 'program', (1+3j))

# Set 
 