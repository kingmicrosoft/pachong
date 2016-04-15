__author__ = 'wisdom'


def InsertSort(a) :
    for i in range(len(a)-1) :
        for j in range(i+1,len(a)) :
            if a[i]>a[j] :
                temp=a[i];
                a[i]=a[j]
                a[j]=temp
    return a

a=[1,30,34,2,100,90]
b=InsertSort(a)
print b



def mergeSort(L) :
    print L
    if(len(L)<2) :
        return L[:]
    else :
        middle=len(L)/2
        left=mergeSort(L[:middle])
        right=mergeSort(L[middle:])
        together=merge(left,right)
        print together
        return together


def merge(left,right) :
    resullt= []
    i,j=0,0
    while i<len(left) and j<len(right) :
        if left[i]<= right[j]:
            resullt.append(left[i])
            i=i+1
        else :
            resullt.append(right[j])
            j=j+1
    while(i<len(left)) :
        resullt.append(left[i])
        i=i+1




