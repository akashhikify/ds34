def linearsearch(a,key):
    n=len(a)
    for i in range (n):
        if a[i]==key:
            return i;
        return -1
a=[14,5,7,9,0,5,9]
print("the array element",a)
k=int(input("enter the element:"))

    