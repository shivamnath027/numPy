# SLICING

#If we don't pass start its considered 0
#If we don't pass end its considered length of array in that dimension
#If we don't pass step its considered 1


import numpy as np
arr = np.array([1,'a',3,4,'b',6,7])
print("\narr={} \n".format(arr))
print("\narr[1:5]= {}".format(arr[1:5]))

# [ START: END : STEP]

print("\n--------------------STEP SLICING----------------\n")

print("\narr[0:-1:2]= {}".format(arr[0:-1:2]))

print("\n----------------------MISSING START/END SLICING--------------------\n")

print("\narr[4:]= {}".format(arr[4:])) #since no end mentioned, will go till end

print("\narr[:4]= {}".format(arr[:4])) #since no begin mentioned, will include beginning

print("\n",arr[::2])

print("\n---------------NEGATIVE SLICING---------------------\n")
print("\narr[-3,-1]={}".format(arr[-3:-1]))

print("\n\n----------------SLICING 2D ARRAYS-------------------\n")

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("\narr2= {}\n".format(arr2))
print("\narr2[1,1:4]= {}".format(arr2[1,1:4]))

print("1 Se pehla list pkrega fir 1:4 se uss list ka element 1 se 3 tak\n\n")

print("\nTHODA SPECIAL CASE HAI:\narr[0:2,2]={} ".format(arr2[0:2,2]))
print("From both Elements, returns index 2")

