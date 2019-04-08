# TODO: implement binary search iteratively here
if len(array) == 0:
    return None

isFound = False
left = 0
right = len(array) - 1
result = None

while isFound == False:

    if left == right:
        if array[left] == item:
            result = left
            isFound = True
            continue
        return None

    middle_index = (left + right) // 2
    middle_value = array[middle_index]

    if middle_value == item:
        result = middle_index
        isFound = True
    elif middle_value > item:
        right = middle_index - 1
    elif middle_value < item:
        left = middle_index + 1

return result
