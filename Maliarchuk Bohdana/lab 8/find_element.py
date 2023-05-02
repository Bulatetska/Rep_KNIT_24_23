def find_element(lst, element):
    try:
        return print(lst.index(element))
    except ValueError:
        return -1