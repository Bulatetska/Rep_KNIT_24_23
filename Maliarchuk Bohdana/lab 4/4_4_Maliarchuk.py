a = "a14b6fh"

def check(a):
    for i in range(len(a)):
        for j in range(i + 1,len(a)):
            if(a[i] == a[j]):
                return False;
    return True;
 
if(check(a)):
    print("The String ", a," has all unique characters");
else:
    print("The String ", a, " has duplicate characters");
 