Value = 7,10,12,14,16,20,29,37
def Linear_Search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return None
def Binary_Search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

print("Linear Search of 14:",Linear_Search(Value, 14))
print("Binary Search of 14:",Binary_Search(Value, 14))
print("Linear Search of 29:",Linear_Search(Value, 29))
print("Binary Search of 29:",Binary_Search(Value, 29))