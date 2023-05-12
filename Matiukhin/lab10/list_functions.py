def sort_asc_cond(a, b):
    '''
    Sorts the array in ascending order
    '''
    return a < b

def sort(arr, condition = sort_asc_cond):
    '''
    Sorts the array
    '''
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if condition(arr[i], arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def find_key(arr:list, key):
    '''
    Finds the index of the key in the array
    '''
    for i, val in enumerate(arr):
        if val == key:
            return i
    return -1

def find_sequence(arr:list, sequence:list):
    '''
    Finds the index of the sequence in the array
    '''
    for i in range(len(arr) - len(sequence) + 1):
        if arr[i:i+len(sequence)] == sequence:
            return i
    return -1

def find_top_5_min(arr:list):
    '''
    Finds the top 5 minimum values in the array
    '''
    arr = sort(arr)
    return arr[0:5]

def find_top_5_max(arr:list):
    '''
    Finds the top 5 maximum values in the array
    '''
    arr = sort(arr, lambda a, b: a > b)
    return arr[0:5]

def avg(arr:list):
    '''
    Finds the average of the array
    '''
    return sum(arr) / len(arr)

def get_list_without_repetitions(arr:list):
    '''
    Returns the list without repetitions
    '''
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr