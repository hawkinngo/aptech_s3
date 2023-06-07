import numpy as np

list = np.random.randint(1, 1000, 50)

total_elemt_in_list = 0
[total_elemt_in_list := total_elemt_in_list + i for i in list]
mean_list = total_elemt_in_list / len(list)
print(mean_list)
