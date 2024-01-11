import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("NumPy Array 1:")
print(arr1)
print("NumPy Array 2:")
print(arr2)

# Basic array properties
print("\nArray 1 Shape:", arr1.shape)
print("Array 2 Shape:", arr2.shape)
print("Array 1 Dimension:", arr1.ndim)
print("Array 2 Dimension:", arr2.ndim)
print("Array 1 Data Type:", arr1.dtype)
print("Array 2 Data Type:", arr2.dtype)

# Reshaping arrays
arr3 = np.arange(12).reshape(3, 4)
print("\nReshaped Array:")
print(arr3)

# Slicing arrays
print("\nSliced Array:")
print(arr3[1:3, 1:3])

# Array operations
print("\nArray Operations:")
print("Sum of Array 1:", np.sum(arr1))
print("Mean of Array 2:", np.mean(arr2))
print("Max of Array 1:", np.max(arr1))
print("Min of Array 2:", np.min(arr2))

# Broadcasting and element-wise operations
print("\nBroadcasting & Element-wise Operations:")
print("Addition:")
print(arr1 + 10)
print("Multiplication:")
print(arr2 * 2)

# Linear algebra operations
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print("\nMatrix Multiplication:")
print(np.dot(matrix_a, matrix_b))

# Random number generation
random_array = np.random.rand(3, 3)
print("\nRandom Array:")
print(random_array)