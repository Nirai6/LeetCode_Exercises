def Sort_Array_By_Parity(array):
    j=0
    for i in range(len(a)):
        if a[i]%2==0:
            a[i],a[j]=a[j],a[i]
            j+=1
    return(a)
a=[1,3,4,2]
s=Sort_Array_By_Parity(a)
print(s)
