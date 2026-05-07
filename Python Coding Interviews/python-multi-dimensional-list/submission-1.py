from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_list = []
    max_value = 0
    for i in nested_arr:
        for j in i:
            if j > max_value:
                max_value = j
        
        max_list.append(max_value)
    return max_list



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
