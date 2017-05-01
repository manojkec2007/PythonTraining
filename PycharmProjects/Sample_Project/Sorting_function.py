"""  --sorting using sort function
a=[7,1,3,5,2,8]
a.sort()
print a  # [1,2,3,5,7,8]
"""

a = [7,1,3,5,2,8]
print a  # [7,1,3,5,2,8]

# Insertion Sort Algorithm
# Start with 1st Element  --here 1


def insertion_sort(list):
    for index in range(1, len(list)):  # 1 -ist item from the list -always start with 1 element to compare
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i-1
            else:
                break
    return list
sorted_val = insertion_sort(a)
print sorted_val

