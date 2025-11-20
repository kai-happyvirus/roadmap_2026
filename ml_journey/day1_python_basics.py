def square_list(lists):
  return [list^2 for list in lists]

list_data = [1,2,3,4]
print(square_list(list_data))

import numpy as np

np_array = np.array([[1,2,3],[4,5,6]])
np_array_1 = np.arange(1,7).reshape(2,3)

print(np_array)
print(np_array_1)