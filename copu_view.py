import numpy as np

print("----------------COPY------------")
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(f"arr= {arr}")
print(f"x= {x}")


