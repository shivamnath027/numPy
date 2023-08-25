import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype) #int 32

arr2 = np.array(["hi","hello"])

print("\n-----CREATING ARRAYS WITH DEFINED DATA TYPES------\n")
arr3 = np.array(["hi","hello"],dtype="S")
print(arr2.dtype)
print(arr3.dtype)

#Error will occur when Defined data types ie, dtype is specified for an array which contains elements with Different datatypes


print("-------Converting Data Type on Existing Arrays-----=")

print("\n\nThe astype() function creates a copy of the array, and allows you to specify the data type as a parameter.\n\n")
#The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
print("\n\n<<-----FOR EX:  TYPE CASTING AS DONE HERE------->>\n\n")

arro = np.array([1.1, 2.1, 3.1])
print(f"arro= {arro}")
newarr = arro.astype('i')
print(newarr)
print(newarr.dtype)

#  'i' - int32   NUMPY DATA TYPE
#  'int' - int64  PYTHON DATA TYPE
print("---------------------------------------------")