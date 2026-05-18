import numpy as np;

# array creation
arr = np.array([1,2,3,4]);
print(arr);

# array ops
arr1 = np.array([1,2,3]);
arr2 = np.array([10,20,30]);

print(arr1 + arr2);
# print(arr1 * arr2);
# print(arr1 * 2);
# print(arr1 + 5);

# 0s and 1s
# print(np.zeros([3,4]))
# print(np.ones([5,9]))

# Mean, max, min
data = np.array([10,20,30,40]);

print("Mean:", np.mean(data))
# print("Max", np.max(data));
# print("Min", np.min(data));