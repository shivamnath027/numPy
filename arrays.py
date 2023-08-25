import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# print(type(arr))
#The array object in NumPy is called ndarray

# print(np.__version__)

#nested array: are arrays that have arrays as their elements.

# 0-D array

# print('0-D ARRAY')
# import numpy as np
# arr0 = np.array(42)
# print(arr0)

# 1-D ARRAY

# print('1D ARRAY')
# arr1 = np.array([1,2,3,4])
# print(arr1)

#2-D ARRAY

# print('2D ARRAY')
# arr2 = np.array(
#             [
#             [1,2,3],
#             [4,5,6]
#             ]     )
# print(arr2)

#3-D ARRAY

# print('3D array')
# arr3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
# print(arr3)


# To check Number of Dimensions
# print(arr0.ndim,arr1.ndim,arr2.ndim,arr3.ndim)


#TO specify Dimensions for explicit creation

# arr_dim = np.array([1,2,3,4],ndmin=5)
# print("array = {},\nNumber of Dimensions= {}".format(arr_dim,arr_dim.ndim))
# print(arr_dim.flags)

#   C_CONTIGUOUS : True
#   F_CONTIGUOUS : True
#   OWNDATA : False
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False


#Accessing the elements
# 1D
# ar = np.array([1, 2, 3, 4])
# print(ar[1])
# print(ar[2] + ar[3])

#2D
# arr = np.array(
#                 [
#                 [1,2,3,4,5], 
#                 [6,7,8,9,10]
#                 ]
#               )

# print('3rd Element on 1st row:{} '.format(arr[0,2]))
# print('2nd row 5th columm: {}'.format(arr[1,4]))


#3D Array
# arr = np.array([
                
#                 [
#                     [1, 2, 3], [4, 5, 6]
#                 ], 
#                 [
#                     [7, 8, 9], [10, 11, 12]
#                 ]
#                 ])

#The first number represents the first dimension, which contains two arrays:
#The second number represents the second dimension, which also contains two arrays:
#The third number represents the third dimension, which contains three values:

# print(arr[1,1,0])  #10

# NEGATIVE INDEXING
# arr = np.array([1,2,3,4,5])
# print(arr[-1])

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('Last element from 2nd dim: ', arr[1, -1])



