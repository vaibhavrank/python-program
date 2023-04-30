# def three_D_rray(a,b,c,n):
#     l =[]
#     for i in range(a):
#         for j in range(b):
#             for k in range(c):
dim1=3
dim2 = 4
dim3 = 5
value = int(input())
# for _ in range(dim1):
#     for _ in range(dim2):
#         for _ in range(dim3):
#             print(value) 
array_3d = [[[value for i in range(dim3)] for i in range(dim2)] for i in range(dim1)]
print(array_3d)




# import numpy as np

# def create_array(dim1, dim2, dim3, value):
#     """
#     Creates and returns a 3D array with given dimensions, initialized to a given value.
    
#     Args:
#         dim1 (int): Dimension 1 of the 3D array.
#         dim2 (int): Dimension 2 of the 3D array.
#         dim3 (int): Dimension 3 of the 3D array.
#         value (int): Value to initialize each element of the 3D array.
        
#     Returns:
#         numpy.ndarray: A 3D array of dimensions dim1 x dim2 x dim3, initialized with the given value.
#     """
#     # Create a 3D array with given dimensions
#     array = np.full((dim1, dim2, dim3), value)
    
#     return array

# # Example usage
# dim1 = 3
# dim2 = 4
# dim3 = 5
# value = 10

# # Call the function to create a 3D array with dimensions 3x4x5, initialized with value 10
# my_array = create_array(dim1, dim2, dim3, value)

# # Print the created array
# print(my_array)
