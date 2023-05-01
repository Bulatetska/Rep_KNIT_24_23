def sort_list(lst):
   
    return sorted(lst)

def find_element(lst, elem):
   
    try:
        return lst.index(elem)
    except ValueError:
        return -1

def find_sequence(lst, seq):
   
    n = len(seq)
    for i in range(len(lst)-n+1):
        if lst[i:i+n] == seq:
            return i
    return -1

def find_min(lst, n=5):
   

    return sorted(lst)[:n]

def find_max(lst, n=5):
   
    return sorted(lst, reverse=True)[:n]

def average(lst):
   
    return sum(lst) / len(lst)

def remove_duplicates(lst):
   
    return list(dict.fromkeys(lst))