import numpy as np

# create array (vector)
a = np.array([1, 2, 3, 4, 5])

print("Array:", a)
print("Type:", type(a))

# math operation
b = a * 2
print("Multiply:", b)

# Mean (Average)
avg = np.mean(a)
print("Average:", avg)

# matrix (2D array)
m = np.array([
    [1, 2, 3],
    [4, 5, 6]
    
])

print("Matrix:")
print(m)

# Matrix shape
print("Shape:", m.shape)