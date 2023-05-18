myDict = {1: "apple", 2: "banana", 3: "orange", 4: "apricot", 5: "pear"}

newDict = myDict.copy()

for key, value in myDict.items():
    if value.startswith("a"):
        del newDict[key]

print(newDict)
