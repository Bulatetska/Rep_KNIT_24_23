def find_sequence(lst, sequence):
    for i in range(len(lst)-len(sequence)+1):
        if lst[i:i+len(sequence)] == sequence:
            return print(i)
    return -1